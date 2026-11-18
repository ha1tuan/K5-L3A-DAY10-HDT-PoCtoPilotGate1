# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): HDT
- Lớp: `L3A`
- Repo của bàn: `K5-L3A-DAY10-HDT-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): S3

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Vũ Hải Tuấn | 2A202603689 | Sản phẩm và kinh doanh | x |
|   2 | Phan Văn Diện | 2A202603653 | Vận hành và pháp lý |             |
|   3 | Nguyễn Thị Thu Hà | 2A202603719 | Kỹ sư cổng |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## HoVaTen-MSSV

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.


## NguyenThiThuHa-2A202603719

### Phần việc phụ trách

Vai: Kỹ sư cổng. Vòng 1: câu 2.1 và 2.2 (chạy mốc base, dò trace T-002@55), câu 2.6 đến 2.8 (code cổng trong lab10/guards.py, hai bước tránh rò rỉ dữ liệu, behavioral test). Vòng 2: dò trace sự cố, sửa lab10/guards.py, thêm chỉ số theo dõi trong lab10/monitors.py, chạy ba mốc.

### Đóng góp cụ thể

Chạy mốc base (R-base-before-20261118-085909-b45eeb) và dò trace T-002@55: khách khai trễ 5 ngày, tracking ghi 2 ngày, trợ lý hoàn 20.000đ và ghi lỗi oan cho hãng VNX. Viết 3 cổng trong lab10/guards.py (số tiền hoàn không vượt mức tính từ tracking DB; chỉ ghi lỗi hãng khi tracking và chính sách xác nhận; gói gửi hãng chỉ có order_id, parcel_id, district, delay_days). Mốc after R-base-after-20261118-090300-5b32a2: pass_rate 1,0, hoàn sai 0đ, lỗi hãng oan 0, không ca đúng nào bị hỏng. Viết hai bước tránh rò rỉ dữ liệu và một behavioral test với hai ticket hiểm (O-1024, O-1026).

Dùng AI (Claude): đọc lab10/agent.py, lab10/tools.py, lab10/helpers.py, data/world.json, data/tickets.jsonl; chạy lab10.eval, lab10.gate, lab10.trace; soạn nháp Phiếu B mục B0, B1, B2, B7 và code ba cổng trong lab10/guards.py.

### Bằng chứng

Commit trên main: b4ae3d7 (Phiếu B câu 2.1, 2.2, 2.6, 2.7, 2.8 và 3 cổng vòng 1); 1b5ec92 và 8b56f77 (mục cá nhân và vai trong TEAM.md).

### Exit ticket

Chưa viết.


## VuHaiTuan-2A202603689

### Phần việc phụ trách

Vai: Sản phẩm và kinh doanh, trưởng nhóm (tạo repo của bàn, gộp nhánh `phanvandien` vào `main`). Vòng 1: Phiếu A (A1, ký tiêu chí trong `config/acceptance_criteria.json`), Phiếu B câu 2.3 (bản đồ dữ liệu B3), B7.1–B7.2 (đối chiếu cổng với B3–B6), câu 2.9 (cổng kinh doanh `business` trong `config/operating_gates.json`), chốt cổng vòng 1. Vòng 2 (thẻ S3): câu 3.5 và 3.6 (sửa `lab10/guards.py`, thêm chỉ số trong `lab10/monitors.py`, thêm điều kiện dừng trong `config/operating_gates.json`), nhật ký lần chạy C0.

### Đóng góp cụ thể

- Điền Phiếu A mục A1 và bắt đầu checkpoint 2 (phần quyết định và `decision_rule`); ký tiêu chí và tạo `config/acceptance_criteria.lock` trước lần đánh giá đầu tiên.
- Phiếu B: câu 2.3 (bản đồ dữ liệu và ví dụ drift `index_active` của chính sách), B7.1–B7.2 (ghi phạm vi và giới hạn của ba cổng vòng 1), câu 2.9 (`business.daily_refund_cap_vnd` = 2.000.000đ, khớp `ops_limits.daily_auto_refund_budget_vnd`; lần chạy `R-base-after-20261118-165303-e754ad` ngày cao nhất mới hoàn 155.000đ).
- Chốt cổng vòng 1: `config/round1.lock`, `lab10/guards_round1.py`, `config/operating_gates.round1.json` (sha256 `6c72f47a…`, lúc 17:04).
- Vòng 2, thẻ S3 (drift chính sách và ghi lỗi hãng khi tracking chưa có nguyên nhân):
  - `pre_guard`: ghim chính sách theo `effective_from`/`effective_to` so với ngày hôm nay, không theo cờ `index_active`; không có chính sách hiệu lực thì chuyển người.
  - `_gate_carrier_fault`: chặn ghi lỗi hãng khi `delay_cause` rỗng; từ lỗi thứ 3 của cùng một hãng trong ngày thì không ghi tự động mà chờ người duyệt (`ops_limits.max_auto_strikes_per_carrier_per_day`).
  - Ba chỉ số mới trong `lab10/monitors.py`: `policy_drift_rate`, `fault_attempt_without_cause_rate`, `max_strikes_per_carrier_day`.
  - Hai điều kiện dừng mới trong `config/operating_gates.json` gắn với hai chỉ số trên.
- Kết quả trên S3: mốc before `R-S3-before-20261118-173200-b4e5a0` pass_rate 0,25, hoàn sai 900.000đ, 35 lỗi hãng oan; mốc prepared (cổng vòng 1) pass_rate 0,5, 15 lỗi hãng oan; mốc after `R-S3-after-20261118-173200-b4e5a0` pass_rate 1,0, hoàn sai 0đ, lỗi hãng oan 0, lộ dữ liệu 0, ROI 1,27. Bộ nền không hỏng ca nào (`R-base-after-20261118-173142-2fc64c`, 110/110). `lab10.grade`: `PASS-VISIBLE` (integrity, criteria, visible, regression, monitor đều đạt; chưa chạy test ẩn).

### Bằng chứng

- Commit: `8319f38` (A1), `e8290b9` (Sign acceptance criteria), `3306671` (checkpoint 2, Phiếu A), `f96e72c` (câu 2.3), `3ce136a` (B7.1, B7.2), `a8ff3e2` (câu 2.9), `1de8e6d` (chốt cổng vòng 1), `3dd45b7` (câu 3.5, 3.6 cho thẻ S3); các merge `1eaa7fa`, `6a1a19c`, `66b3988`, `0498a6a`.
- Lần chạy: `R-base-after-20261118-165303-e754ad`, `R-S3-before-20261118-173200-b4e5a0`, `R-S3-prepared-20261118-173200-b4e5a0`, `R-S3-after-20261118-173200-b4e5a0`, `R-S3-grade-20261118-173200-b4e5a0`.
- Phiếu B mục B3, B7.1, B7.2, B7.4; Phiếu C mục C0, C7, C8.

### Exit ticket

Học được: cổng phải dựa vào nguồn sự thật (ngày hiệu lực của chính sách, tracking DB), không dựa vào cờ do người bật tay; cổng vòng 1 chỉ đỡ được một nửa thẻ S3 vì nó vẫn tin `index_active`.
Còn chưa chắc: trần 2 lỗi/hãng/ngày có hợp lý khi lượng ticket thật dồn lên, và test ẩn có ca nào cổng mới chưa phủ không.

## PhanVanDien-2A202603653

### Phần việc phụ trách

Vai: Vận hành và pháp lý. Vòng 1: Phiếu A (chỉnh câu về thiệt hại cho bên ngoài LogiX), Phiếu B câu 2.4–2.5 (HAZOP B4, checklist go-live B5, pre-mortem B6), câu 2.10 (cổng con người, vận hành, pháp lý trong `config/operating_gates.json` và Runbook phần 1–3), mục giờ cao điểm. Vòng 2 (thẻ S3): Phiếu C phần phân tích (C1–C6, C9–C11).

### Đóng góp cụ thể

- Phiếu B: HAZOP vòng 1 trên tool của agent, checklist go-live 9 nhóm việc lần 1, pre-mortem bốn lăng kính dẫn ra cổng phòng ngừa.
- `config/operating_gates.json`: mục con người, vận hành, pháp lý (người duyệt, điều kiện dừng, kênh cảnh báo), mỗi con số kèm lý do lấy từ `data/world.json` → `ops_limits`; Runbook 1–3 và mục giờ cao điểm.
- Đưa thẻ sự cố S3 và các thẻ S1–S8 vào `incidents/` để bàn chạy vòng 2.
- Phiếu C cho thẻ S3: nhật ký lần chạy, mốc prepared và đối chiếu pre-mortem (C1), bảng soát lỗi (C2), mở lại bản đồ dữ liệu (C3.5), HAZOP của thẻ (C4), specification và giả định môi trường (C5), fault tree trước khi sửa (C6), fault tree sau khi sửa (C9), risk register (C10), cập nhật checklist và Runbook 4–5 (C11).

### Bằng chứng

- Commit: `39294d5`/`86f8def` (v1, Phiếu A), `3aea186` (v2, Phiếu B B4–B6), `7cf8f49` (v3, thẻ S3, cổng vận hành, Phiếu B B7.5–B7.6), `e96fbc6` (v4, thẻ sự cố, Phiếu B), `15c78cb` (v4, TEAM.md, Phiếu C C0), `f8d7e22` (v5, Phiếu C C3.5–C4), `5499b00` (v6, Phiếu C C5–C6), `657c092` (v7, Phiếu C C9–C11).
- Lần chạy dùng cho fault tree (C6, C9): `R-S3-before-20261118-173200-b4e5a0`, `R-S3-after-20261118-173200-b4e5a0`.
- Phiếu B mục B4, B5, B6, B7.5, B7.6; Phiếu C mục C1–C6, C9–C11.

### Exit ticket

Học được: điều kiện dừng chỉ có ích khi gắn với một con số đo được và một người có tên chịu trách nhiệm.
Còn chưa chắc: dữ liệu mock có phản ánh đúng tốc độ các hãng cập nhật nguyên nhân trễ trong thực tế không.
