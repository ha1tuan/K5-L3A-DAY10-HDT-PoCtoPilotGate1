# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng):
- Lớp: `L3A` / `L3B`
- Repo của bàn: `K5-<L3A|L3B>-DAY10-<TenNhom>-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): S3

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Vũ Hải Tuấn          | 2A202603689     |     |             |
|   2 | Phan Văn Diện       |   2A202603653   |     |             |
|   3 | Nguyễn Thị Thu Hà | 2A202603719 | Kỹ sư cổng |             |
|   4 |           |      |     |             |
|   5 |           |      |     |             |

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
