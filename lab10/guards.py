"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


# Chỉ những trường này được gửi cho hãng (điều kiện dừng số 1 trong Bản tiêu chí đã ký).
CARRIER_FIELDS = ("order_id", "parcel_id", "district", "delay_days")


def _last(ctx, kind):
    return next((e for e in reversed(ctx.events) if e.get("type") == kind), None)


def _policy_used(ctx):
    pol = _last(ctx, "policy")
    return next((p for p in ctx.tools.lookup_policies() if pol and p["policy_id"] == pol["policy_id"]), None)


def _gate_refund_vs_tracking(ctx, action):
    """Cổng 1: số tiền hoàn (LogiX trả) không được vượt mức tính từ tracking DB và chính sách đang dùng.

    Bắt cả khi trợ lý tin số ngày khách khai (khác DB) lẫn khi trợ lý hoàn \"cho chắc\" lúc LLM lỗi."""
    trk, prop, policy = _last(ctx, "tracking"), _last(ctx, "proposal"), _policy_used(ctx)
    if not (trk and prop and policy) or action.get("payer") != "LOGIX":
        return None
    order = ctx.tools.lookup_order(action["order_id"])
    entitled = H.entitlement_vnd(policy, order, trk["db_delay_days"], trk["cause"])
    if action["amount_vnd"] <= entitled:
        return None
    ctx.log("refund_vs_tracking", used=prop["delay_days_used"], db=trk["db_delay_days"],
            amount_vnd=action["amount_vnd"], entitled_vnd=entitled)
    return Verdict.escalate(
        f"hoàn {action['amount_vnd']}đ vượt mức tracking DB cho phép ({entitled}đ; trợ lý dùng "
        f"{prop['delay_days_used']} ngày, DB {trk['db_delay_days']} ngày): chuyển người duyệt")


def _gate_carrier_fault(ctx, action):
    """Cổng 2: chỉ ghi lỗi hãng khi tracking DB và chính sách xác nhận hãng chịu trách nhiệm."""
    policy = _policy_used(ctx)
    order = ctx.tools.lookup_order(action["order_id"])
    parcel = next((x for x in order["parcels"] if x["parcel_id"] == action["parcel_id"]), None) if order else None
    if policy is None or parcel is None:
        return Verdict.deny("không tra được kiện hoặc chính sách để xác nhận lỗi hãng")
    db_delay = H.db_delay_days(parcel, ctx.as_of)
    if not H.carrier_at_fault(policy, parcel, db_delay):
        ctx.log("carrier_fault_denied", parcel_id=parcel["parcel_id"], db_delay=db_delay,
                cause=parcel.get("delay_cause"))
        return Verdict.deny(f"tracking DB: trễ {db_delay} ngày, nguyên nhân {parcel.get('delay_cause')}; "
                            f"chính sách {policy['policy_id']} không cho ghi lỗi hãng")
    if action.get("delay_days") != db_delay:
        return Verdict.modify("sửa delay_days theo tracking DB", delay_days=db_delay)
    return None


def _gate_carrier_payload(ctx, action):
    """Cổng 3: gói gửi hãng chỉ có bốn trường đã ký, bỏ mọi chữ khách viết và thông tin người nhận."""
    payload = action.get("payload") or {}
    clean = {k: v for k, v in payload.items() if k in CARRIER_FIELDS}
    if clean == payload:
        return None
    ctx.log("carrier_payload_trimmed", removed=sorted(set(payload) - set(clean)))
    return Verdict.modify("chỉ gửi hãng order_id, parcel_id, district, delay_days", payload=clean)


def pre_guard(ctx):
    return Verdict.allow()


def write_gate(ctx, action):
    # action = {"tool": "issue_refund", "ticket_id":..., "order_id":..., "amount_vnd":..., "payer":..., ...}
    gates = {"issue_refund": _gate_refund_vs_tracking,
             "file_carrier_fault": _gate_carrier_fault,
             "notify_carrier": _gate_carrier_payload}
    gate = gates.get(action["tool"])
    return (gate(ctx, action) if gate else None) or Verdict.allow()
