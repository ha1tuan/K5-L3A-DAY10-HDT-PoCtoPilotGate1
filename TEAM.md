# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng):
- Lớp: `L3A` / `L3B`
- Repo của bàn: `K5-<L3A|L3B>-DAY10-<TenNhom>-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8):

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

Vai: Kỹ sư cổng. Vòng 1: câu 1.3 (Phiếu A, mục A2 cột Offline: offline metric cho bước ghi lỗi hãng), câu 2.1 và 2.2 (chạy mốc base, dò trace T-002@55), câu 2.6 đến 2.8 (code cổng trong lab10/guards.py, hai bước tránh rò rỉ dữ liệu, behavioral test). Vòng 2: dò trace sự cố, sửa lab10/guards.py, thêm chỉ số theo dõi trong lab10/monitors.py, chạy ba mốc.

### Đóng góp cụ thể

Thiết kế offline metric cho bước ghi lỗi hãng (file_carrier_fault): thước đo, dữ liệu (trace và label.faults trong data/tickets.jsonl), cách tính, điểm mù. Dùng AI (Claude) để đọc lab10/agent.py, lab10/tools.py, data/tickets.jsonl và soạn bản nháp câu 1.3 cùng khung mục cá nhân này.

### Bằng chứng

Nhánh lab10-dev, các commit: Phiếu A câu 1.3: offline metric cho bước ghi lỗi hãng; Add Nguyễn Thị Thu Hà to TEAM.md. Mã commit trên main: điền sau khi merge.

### Exit ticket

Chưa viết.
