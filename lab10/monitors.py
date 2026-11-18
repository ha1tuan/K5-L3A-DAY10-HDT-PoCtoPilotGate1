"""★ FILE ĐỘI SỬA (2/3): chỉ số theo dõi (monitor). Thêm ÍT NHẤT MỘT chỉ số bắt được sự cố của bàn.

Mỗi monitor nhận danh sách trial (KHÔNG có nhãn đúng/sai, giống production) và trả về một số.
Một trial = {"ticket_id", "seed", "day", "status", "amount_vnd", "ticket", "events", "ledger", "faults", "outbound",
             "arrive_min", "warehouse", "cost_vnd", "review_kind", "queue_wait_min", "queue_stuck"}
  "day"            một ngày vận hành giả lập: các ticket cùng "day" và cùng "seed" chạy nối nhau trên cùng một sổ cái
  "arrive_min"     phút ticket tới trong ca (0..480)          "warehouse"   kho của đơn
  "cost_vnd"       tiền LLM + nền tảng đã tốn cho ticket      "review_kind" None / "escalated" (trợ lý chuyển người) /
  "queue_wait_min" số phút chờ người duyệt (None nếu không vào hàng chờ)     "recheck" (nhân viên tự kiểm lại)
Chỉ số có thể là kỹ thuật (tỉ lệ model đè số trong ticket lên DB), vận hành (số ca cần người trong giờ đông nhất),
hay kinh doanh (tỉ lệ ticket trợ lý đọc xong vẫn phải chuyển người).

lab10.grade kiểm: monitor chạy không lỗi, và giá trị trên gói sự cố khác giá trị trên bộ nền,
tức là monitor "sáng đèn" khi sự cố xảy ra.
"""


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


def _events(t, kind, guard_kind=None):
    return [e for e in t.get("events") or [] if e.get("type") == kind
            and (guard_kind is None or e.get("kind") == guard_kind)]


def policy_drift_rate(trials):
    """Thẻ S3 (kỹ thuật/dữ liệu): tỉ lệ ticket mà cờ `index_active` KHÁC chính sách hiệu lực theo ngày.

    Dữ liệu: sự kiện guard `policy_drift` do pre_guard ghi (so effective_from/effective_to với ctx.as_of).
    Mẫu số: mọi trial. Bình thường = 0; > 0 nghĩa là chỉ mục chính sách chưa được cập nhật theo ngày hiệu lực."""
    return sum(bool(_events(t, "guard", "policy_drift")) for t in trials) / max(1, len(trials))


def fault_attempt_without_cause_rate(trials):
    """Thẻ S3 (pháp lý/đối tác): trong các ticket trợ lý ĐỊNH ghi lỗi hãng, tỉ lệ tracking chưa ghi nguyên nhân trễ.

    Dữ liệu: `proposal.do_fault` và `tracking.cause_recorded`. Đo ý định của trợ lý trước cổng, nên vẫn sáng đèn
    khi cổng đã chặn. Mẫu số: số ticket có do_fault=True; không có ca nào thì trả 0."""
    attempts = [t for t in trials if any(e.get("do_fault") for e in _events(t, "proposal"))]
    unrecorded = sum(any(e.get("cause_recorded") is False for e in _events(t, "tracking")) for t in attempts)
    return unrecorded / max(1, len(attempts))


def max_strikes_per_carrier_day(trials):
    """Thẻ S3 (vận hành): số lần trợ lý định ghi lỗi cho CÙNG một hãng trong CÙNG một ngày (seed, day), lấy max.

    Dữ liệu: lệnh `file_carrier_fault` trong events (cả khi bị cổng chặn) gom theo (seed, day, carrier_id).
    So với ops_limits.max_auto_strikes_per_carrier_per_day = 2: vượt 2 là dấu hiệu dồn lỗi cho một hãng."""
    count = {}
    for t in trials:
        for e in _events(t, "tool"):
            if e.get("tool") == "file_carrier_fault":
                k = (t.get("seed"), t.get("day"), e.get("carrier_id"))
                count[k] = count.get(k, 0) + 1
    return max(count.values(), default=0)


MONITORS = {
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
    "policy_drift_rate": policy_drift_rate,
    "fault_attempt_without_cause_rate": fault_attempt_without_cause_rate,
    "max_strikes_per_carrier_day": max_strikes_per_carrier_day,
}
STARTER_MONITORS = ("escalation_rate",)
