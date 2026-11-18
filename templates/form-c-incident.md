# Phiếu C · Sự cố và quyết định v2 · Khối 3 (phút 125–200)

**Bàn:** K5-L3A-DAY10-HDT · **Thẻ đã bốc:** S3 *(Lab Coach đối chiếu với sổ; lệnh tự kiểm tra in dòng này trong report.)*

Mở `incidents/Sx/card.md` của đúng số đã bốc. Các bước trên thẻ trỏ về đúng mục trong phiếu này. Mục C3 chỉ điền phần ứng với
số thẻ của bàn; các phần khác để trống.

**Mục lục**
- [C0 · Nhật ký lần chạy vòng 2 (suốt khối)](#c0)
- [C1 · Câu 3.0 · Mốc prepared và đối chiếu pre-mortem · phút 125–135 · bước 0 trên thẻ](#c1)
- [C2 · Câu 3.1 · Bảng soát lỗi của thẻ · phút 135–145 · bước 1–2](#c2)
- [C3 · Câu 3.1 · Phần riêng theo thẻ · phút 135–145 · bước 3](#c3)
- [C4 · Câu 3.1 · HAZOP của thẻ (≥ 3 dòng) · phút 145–150 · bước 4](#c4)
- [C5 · Câu 3.2, 3.3 · Specification và giả định môi trường · phút 145–150 · bước 4](#c5)
- [C6 · Câu 3.4 · Fault tree TRƯỚC khi sửa · phút 150–155 · bước 4](#c6)
- [C7 · Câu 3.5 · Bảng sửa: nguyên nhân → chỗ sửa → giảm hay ngăn · phút 155–180 · bước 5–7](#c7)
- [C8 · Câu 3.6 · Chỉ số theo dõi mới · phút 155–180 · bước 5](#c8)
- [C9 · Câu 3.7 · Fault tree SAU khi sửa · phút 180–185 · bước 8](#c9)
- [C10 · Câu 3.7 · Risk register (≥ 1 dòng) · phút 180–185 · bước 8](#c10)
- [C11 · Câu 3.7 · Cập nhật checklist 9 nhóm việc và Runbook phần 4–5 · phút 180–185 (runbook có thể xong trong 185–200) · bước 8](#c11)
- [C12 · Quyết định Gate 1 · v2 và ba dòng bắt buộc · phút 185–200 · bước 9](#c12)

---

<a id="c0"></a>

## C0 · Nhật ký lần chạy vòng 2

Mỗi lệnh `lab10.eval` và `lab10.grade` tự ghi một dòng vào `runs/journal.jsonl`. Điền cột "Đổi MỘT thứ gì" (tham số `--note`) và "Kết luận".

| # | Mã lần chạy | Bộ ticket · mốc | Đổi MỘT thứ gì so với lần trước | pass_rate (khoảng tin cậy 95%) | pass_k | Hoàn sai (đ) · lỗi hãng oan · lộ dữ liệu | Tỉ lệ chuyển người | Kết luận (một câu) |
|---|---|---|---|---|---|---|---|---|
| 1 | `R-S3-grade-20261118-171432-c94b28` (grade; prepared không chạy được) | S3 · prepared (thiếu snapshot) | Nhận thẻ S3, chưa sửa thêm; grade chỉ tạo mốc base và after vì chưa có checkpoint vòng 1 | — | — | — | — | Chưa có số prepared; cần checkpoint hợp lệ rồi chạy grade lại |
| 2 | | Sx · after | | | | | | |
| 3 | | Sx · after | | | | | | |
| 4 | | base · after | (kiểm không regression) | | | | | |

---

<a id="c1"></a>

## C1 · Câu 3.0 · Mốc prepared và đối chiếu pre-mortem

Chạy **trước khi sửa bất cứ thứ gì**:

```bash
python3 -m lab10.grade --incident Sx
```

- Mã lần chạy grade: `R-S3-grade-20261118-171432-c94b28` · base: `R-S3-before-20261118-171432-c94b28` · prepared: **chưa có** (thiếu `config/round1.lock`, `lab10/guards_round1.py`, `config/operating_gates.round1.json`).
- Cổng vòng 1 đỡ được ô / con số nào (so cột base với cột prepared): **Chưa kết luận được** vì report không có mốc prepared; không lấy mốc after thay cho prepared.
- Khối kinh doanh và vận hành còn dòng nào vượt trần: **Chưa xác định theo prepared**. Grade hiện tại chỉ có base/after; cần chạy lại sau khi khôi phục/chốt đúng snapshot vòng 1.

**Mở lại pre-mortem (Phiếu B mục B6), viết bằng bút khác màu.** Với thẻ S1, S3, S4, S5 đây là một phần của phần riêng theo thẻ.

- Sự cố trên thẻ thuộc lăng kính nào (kỹ thuật, kinh doanh, con người và vận hành, pháp lý)? **Kỹ thuật/dữ liệu** (agent có thể dùng cờ `policies[].index_active` đã cũ thay vì phiên bản theo `effective_from`); **kinh doanh** (hãng bị phạt 120.000đ mỗi lỗi theo thẻ); **pháp lý/đối tác** (ghi lỗi hãng khi nguyên nhân là bão hoặc chưa được tracking ghi nhận).
- Có nằm trong các lý do bàn đã viết không? Nếu có: cổng vòng 1 đã đỡ được bao nhiêu (đọc cột prepared trong report)? Nếu không: vì sao cả bàn không nghĩ tới? **Phiếu B mục B3 đã nhận diện `index_active` là bản sao có thể lệch ngày hiệu lực, nhưng pre-mortem B6 chưa chuyển drift chính sách thành một lý do thất bại/cổng riêng. Chưa định lượng được cổng vòng 1 đã đỡ bao nhiêu vì không có mốc prepared.**
- Lý do còn thiếu, thêm bây giờ:

| Lý do thất bại (viết ở thì quá khứ) | Lăng kính | Kiểm được bằng gì (trace / data / config nào) |
|---|---|---|
| Chính sách REFUND-v4 đã có hiệu lực từ 01-12-2026 nhưng chỉ mục `index_active`/lựa chọn phiên bản chưa cập nhật; một số parcel còn thiếu `delay_cause`, khiến kết luận về lỗi hãng không đủ căn cứ. | Kỹ thuật/dữ liệu; pháp lý/đối tác | `incidents/S3/card.md`, `incidents/S3/world_patch.json`; so `policies[].effective_from` với `index_active`, kiểm `tracking.cause_recorded` trên S3 trace sau khi có mốc prepared |

---

<a id="c2"></a>

## C2 · Câu 3.1 · Bảng soát lỗi của thẻ

Dò ít nhất 2 ticket hỏng theo kiểu KHÁC nhau:

```bash
python3 -m lab10.trace --suite Sx --ticket <ID> --seed 11
```

Ba loại lỗi: **giới hạn của hệ thống** · **lỗi ngữ cảnh** · **lỗi chìm** (cả người dùng lẫn hệ thống đều không nhận ra; nguy hiểm nhất,
người chịu hại thường là bên thứ ba). Định nghĩa đầy đủ và ví dụ: Phiếu B mục B2.

**Tác hại của thẻ:** khách hàng và hãng/tài xế (LogiX chịu tổn thất/đối soát) · đo bằng `wrongful_refund_vnd` và `wrongful_carrier_faults` · mốc base của gói S3: **900.000đ hoàn sai và 35 lỗi hãng oan** (report grade `R-S3-grade-20261118-171432-c94b28`, visible/base, tổng trên các seed)

### Phần 1 · Ghi lỗi (bằng chứng là mã ticket@seed và dòng trace, không tả chung chung)

| # | Lỗi: người ta thấy gì (dán dòng trace / sổ cái) | Ai gặp, ai chịu | Hệ trọng (thấp / cao) | Loại lỗi (giới hạn hệ thống / ngữ cảnh / chìm) |
|---|---|---|---|---|
| 1 | `S3-02@11`: policy trace chọn `REFUND-v3`; `proposal.amount_vnd=0`; agent trả lời “chưa đủ điều kiện”. Nhãn yêu cầu hoàn **18.000đ** (trễ 2 ngày, `REFUND-v4` đã hiệu lực). | Khách C-01 bị từ chối quyền lợi; LogiX mất niềm tin và phải xử lý lại yêu cầu. | Cao | Lỗi ngữ cảnh (chính sách/nguồn bản sao lỗi thời) |
| 2 | `S3-01@11`: `tracking.cause=FORCE_MAJEURE`; `policy=REFUND-v3`; `file_carrier_fault` ghi MKD/TX-MKD-07. Nhãn yêu cầu `faults: []`; v4 không cho ghi lỗi hãng vì bão. | Hãng Mekong Delta Ship và tài xế bị quy lỗi/phạt; LogiX chịu tranh chấp đối tác. | Cao | Lỗi chìm (tác hại cho bên thứ ba, không hiện ra với khách) |
| 3 | `S3-20@11`: tracking có `cause_recorded:false` và `delay_cause:null`, nhưng `tracking.cause` bị mặc định thành `CARRIER`; agent vẫn ghi lỗi MKD. Nhãn yêu cầu `faults: []`. | Hãng/tài xế bị quy lỗi khi chưa có bằng chứng nguyên nhân; kế toán/đối soát phải sửa sai. | Cao | Lỗi chìm (thiếu dữ liệu bị hiểu nhầm thành xác nhận) |

### Phần 2 · Tìm nguồn (đánh dấu câu nào đúng với từng lỗi)

| Câu hỏi | Lỗi 1 | Lỗi 2 | Lỗi 3 |
|---|---|---|---|
| **Đầu vào:** hệ thống có tự diễn giải / sửa đầu vào của người dùng theo cách họ không lường? Có đặt sai trọng số cho một lời nói hay tín hiệu của người dùng? | Có: cue “chính sách mới” không làm agent xác minh phiên bản theo ngày. | Không: ticket nói bão, nhưng lỗi chính là chính sách stale. | Không: lỗi đến từ trạng thái tracking thiếu, không phải câu khách. |
| **Độ liên quan:** hệ thống có thiếu dữ liệu cần để quyết đúng? Dữ liệu vào có nhiễu, thiếu ổn định? | Có: policy v3 được chọn dù `as_of=2026-12-02`, sau ngày v4 hiệu lực. | Có: dùng `fault_causes` của v3 thay vì v4 theo ngày. | Có: `delay_cause` trống và `cause_recorded=false`, nhưng trace vẫn đưa ra `CARRIER`. |
| **Thứ bậc hệ thống:** có hai hệ thống cùng ghi / cùng theo dõi một thứ mà không rõ bên nào là chủ (ví dụ CSKH hoàn tay và trợ lý cùng ghi sổ)? | Có: nguồn sự thật là ngày hiệu lực trong `policies`; cờ bản sao `index_active` lại quyết định policy agent dùng. | Có: `effective_from/effective_to` và `index_active` mâu thuẫn. | Có: tracking chưa xác nhận nguyên nhân nhưng logic suy diễn trong agent biến null thành `CARRIER`. |
| **Trạng thái hỏng:** nhiều lỗi cộng lại có làm tính năng không dùng được (ví dụ LLM lỗi liên tiếp)? | Không phải trạng thái hỏng liên tiếp; là lỗi chọn policy lặp lại trên ticket thuộc thời kỳ mới. | Không; một lỗi cấu hình policy đủ gây quy lỗi oan. | Có nguy cơ lặp trên mọi parcel thiếu `delay_cause`; cần đo riêng số lần thử ghi lỗi khi `cause_recorded=false`. |

### Phần 3 · Hướng xử lý (mỗi lỗi một ô)

| | Lỗi 1 | Lỗi 2 | Lỗi 3 |
|---|---|---|---|
| Vì sao người gặp coi đây là lỗi | Khách đủ điều kiện theo chính sách có hiệu lực nhưng bị từ chối. | Hãng/tài xế bị phạt vì bất khả kháng trong khi v4 loại `FORCE_MAJEURE` khỏi nguyên nhân quy lỗi. | Hãng bị buộc lỗi khi tracking chưa ghi nhận nguyên nhân; “chưa biết” không đồng nghĩa “lỗi hãng”. |
| Kiểu giải pháp: phản hồi cho người dùng / trao quyền kiểm soát cho người / khác | Khác: chọn policy theo ngày hiệu lực, tính lại quyền lợi và gửi lời giải thích/hoàn đúng. | Trao quyền kiểm soát cho người khi policy chưa đồng bộ; không ghi lỗi hãng, vẫn xét hoàn phí theo policy mới. | Trao quyền cho người đối với kết luận nguyên nhân; không phát lệnh `file_carrier_fault` khi `cause_recorded=false`. |
| Đường đi của người sau khi có giải pháp (ví dụ: ticket chuyển sang người duyệt → duyệt → khách được trả lời) | Tính lại với v4; nếu số liệu vẫn mơ hồ thì chuyển NV-HANH duyệt; sau đó trả lời và ghi đúng số tiền. | Tắt/deny thao tác ghi lỗi; NV-OANH đối soát khiếu nại hãng; khách vẫn được xử lý hoàn phí theo điều kiện v4. | Chuyển ca cho NV-HANH xác minh tracking; giữ hoàn phí theo entitlement nếu đủ căn cứ, không ghi lỗi hãng cho tới khi nguyên nhân được ghi nhận. |
| Hệ thống học được gì (tín hiệu ghi lại để theo dõi: tên metric trong `monitors.py`) | Đề xuất `policy_effective_date_mismatch` (đếm policy được dùng ngoài ngày hiệu lực; cần bổ sung ở C8). | Đề xuất `fault_cause_not_allowed_by_effective_policy` (đếm lần thử ghi lỗi khi cause không thuộc policy hiệu lực; cần bổ sung ở C8). | Đề xuất `fault_attempt_without_recorded_cause` (đếm lần thử ghi lỗi khi `cause_recorded=false`; cần bổ sung ở C8). |

Yêu cầu: ít nhất **hai lỗi có nguồn khác nhau** ở phần 2, và ít nhất một lỗi được xếp đúng là **lỗi chìm**.

---

<a id="c3"></a>

## C3 · Câu 3.1 · Phần riêng theo thẻ (chỉ điền phần của số đã bốc; làm trong khoảng 5 phút)

| Thẻ | Điền phần nào |
|---|---|
| S1 | Mục C1 (đối chiếu pre-mortem) + **C3.5** (mở lại bản đồ dữ liệu: các trường của `parcel`) |
| S2 | **C3.1** Mức kiểm soát của con người |
| S3 | Mục C1 + **C3.5** (bảng `policies`: trường nào là nguồn sự thật về "phiên bản đang hiệu lực"; dòng `delay_cause`) |
| S4 | Mục C1 + mục **Giờ cao điểm** ở Phiếu B mục B7.6 (bổ sung bằng bút khác màu nếu đã viết) |
| S5 | Mục C1 + **C3.5** + mục **C8** dùng cho một con số kinh doanh (chi phí mỗi ticket theo kho) |
| S6 | **C3.2** Hình dung của người và của hệ thống |
| S7 | **C3.3** Hiệu chỉnh lòng tin (người đặt hàng, người nhận hàng) |
| S8 | **C3.4** Hiệu chỉnh lòng tin (nhân viên duyệt, trưởng ca đứng tên) + **một dòng** "hoàn trên hạn mức" ở bảng C3.1 Bước 2 |

### C3.1 · Mức kiểm soát của con người ở từng lệnh ghi (S2; S8 chỉ một dòng)

**Cách làm:** (1) soát các dấu hiệu cho thấy con người **cần giữ nhiều quyền kiểm soát hơn**; (2) lập bảng
*ai · ở việc nào · cần mức kiểm soát nào* (thấp / vừa / cao / chưa rõ), thêm một cột: **hệ thống hiện đang cho mức nào**.
Chỗ hai cột lệch nhau chính là nơi đặt gate.

**Bước 1 · Dấu hiệu cần nhiều quyền kiểm soát hơn (đánh dấu, ghi bằng chứng từ thẻ)**

| Dấu hiệu | Có? | Bằng chứng trong thẻ / data |
|---|---|---|
| Việc này đụng tới lĩnh vực nhạy cảm: tiền, quan hệ kinh doanh với đối tác | | |
| Hệ trọng cao và cách làm bằng AI còn mới với người liên quan: họ muốn nắm quyền lúc đầu để xây lòng tin | | |
| Hệ thống còn lâu mới đạt độ chính xác mong muốn; quyền của con người là biện pháp tạm trong lúc chờ | | |
| Giới hạn hoặc lỗi của hệ thống cần con người sửa lại | | |
| Hoàn cảnh thay đổi khiến con người phải "đặt lại" hoặc "tiếp quản" (phê duyệt hết hạn, bị thu hồi; chính sách đổi) | | |

**Bước 2 · Bảng mức kiểm soát**

| Ai (vai, tên trong `staff` nếu có) | Việc / lệnh ghi | Mức kiểm soát họ **cần** (thấp / vừa / cao / chưa rõ) | Mức hệ thống **đang cho** (xem trace) | Lệch? |
|---|---|---|---|---|
| | `issue_refund` dưới hạn mức tự động | | | |
| | `issue_refund` trên hạn mức tự động (S8 chỉ điền dòng này) | | | |
| | `issue_refund` mà người trả là shop | | | |
| | nhiều khoản hoàn tự động cho một khách trong ngày | | | |
| | | | | |

→ Mỗi dòng "Lệch" là một nhánh của fault tree và một ứng viên cho gate. Ghi rõ gate **trả quyền về cho ai** (chuyển người
duyệt, chờ duyệt, trần).

**Ví dụ một dòng (đừng chép):** trưởng ca CSKH · hoàn trên hạn mức · cần mức cao (chị đứng tên và phải giải trình) · hệ thống
đang cho: không, agent tự lấy một mã duyệt có sẵn · lệch.

### C3.2 · Hình dung của người và hình dung của hệ thống (S6)

**Cách làm:** thảo luận theo nhóm rồi ghi cho **từng nhóm người dùng**: họ là ai, mục tiêu chính là gì, và hiện
nay họ làm việc này **từng bước ra sao**, đồng đều hay mỗi nơi một kiểu. Dòng cuối: **hệ thống đang mang hình dung nào**, đọc từ trace.

| | Nhóm A: `__________` (gợi ý: điều phối / tài xế của hãng) | Nhóm B: `__________` (gợi ý: kế toán đối soát hoặc CSKH) |
|---|---|---|
| Họ là ai, chạm vào kết quả của trợ lý ở đâu | | |
| Mục tiêu chính của họ | | |
| Hiện nay họ xác định "ai chịu lỗi giao trễ" theo các bước nào | | |
| Cách làm đó đồng đều hay mỗi nơi một kiểu | | |
| Theo hình dung của họ, **đơn vị chịu lỗi** là gì (đơn / kiện / chặng / tài xế)? | | |

**Hệ thống đang mang hình dung nào?** (đọc trace một ticket hỏng: `tracking.parcels` so với dòng `file_carrier_fault`)

- Với hệ thống, đơn vị chịu lỗi là: `__________`. Bằng chứng: ticket `______@seed ____`, dòng trace: `__________`.
- Chỗ hai hình dung vênh nhau: `__________`.
- Khi đầu vào không đủ để áp hình dung của con người (không biết kiện nào), hệ thống đang làm gì: `__________`; nên làm gì: `__________`.

→ Mỗi chỗ vênh là một nhánh của fault tree. Gate tốt làm cho hệ thống hành xử theo hình dung của người chịu hậu quả.

### C3.3 · Hiệu chỉnh lòng tin · người đặt hàng và người nhận hàng (S7)

**Cách làm:** đặt ba mốc trên một trục: **không tin · tin vừa đủ · tin quá mức**. Với từng nhóm người, nghĩ ra
một tình huống đẩy họ về mỗi mốc, rồi ghi hai thứ làm lòng tin lệch: **dữ liệu của hệ thống** có liên quan, và **điều người đó
biết hay không biết**. Mục tiêu là lòng tin khớp với việc hệ thống thực sự làm. Người nhận hàng không dùng hệ thống, không ký gì với LogiX.
Chỉ cần hai mốc có trong thẻ; mốc còn lại để trống nếu không có bằng chứng.

| Mốc | Nhóm | Tình huống cụ thể (lấy từ thẻ / ticket) | Dữ liệu của hệ thống liên quan (trường nào, đi tới đâu) | Điều người đó biết / không biết |
|---|---|---|---|---|
| **Tin quá mức** | người đặt hàng | | | |
| **Tin quá mức** | người nhận hàng | | | |
| **Không tin** (sau sự cố) | người nhận hàng | | | |
| **Tin vừa đủ** (trạng thái muốn tới) | cả hai | | | |

**Rút ra:**
- Dữ liệu nào rời hệ thống mà người liên quan **không biết** là nó rời đi: `__________` → tới `__________`.
- Để lòng tin khớp thực tế, có hai đường: **giải thích** cho người dùng dữ liệu đi đâu, hoặc **làm cho hệ thống chỉ làm đúng
  điều người ta tưởng**. Với người nhận hàng (không có kênh nào để giải thích), đường khả thi là: `__________`.
- Biện pháp đó là giảm khả năng lộ hay bảo đảm không lộ: `__________`.

### C3.4 · Hiệu chỉnh lòng tin · nhân viên duyệt và trưởng ca đứng tên (S8)

Cùng cách làm như C3.3. Mốc "tin quá mức" là trước kiểm toán, mốc "không tin" là sau kiểm toán.

| Mốc | Nhóm | Tình huống cụ thể (lấy từ thẻ / ticket) | Dữ liệu của hệ thống liên quan (trường nào, đi tới đâu) | Điều người đó biết / không biết |
|---|---|---|---|---|
| **Tin quá mức** (trước kiểm toán) | nhân viên duyệt | | | |
| **Tin quá mức** (trước kiểm toán) | trưởng ca đứng tên | | | |
| **Không tin** (sau kiểm toán) | nhân viên duyệt | | | |
| **Không tin** (sau kiểm toán) | trưởng ca đứng tên | | | |
| **Tin vừa đủ** (trạng thái muốn tới) | cả hai | | | |

**Rút ra:**
- Dữ liệu nào của hệ thống làm lòng tin lệch: `__________`.
- Để người duyệt thôi kiểm tay từng quyết định, họ cần **thấy** gì ở mỗi quyết định, cần **giữ quyền** ở đâu, và
  tỉ lệ kiểm mẫu nào hai bên chấp nhận: `__________`. Ghi các con số đó vào `config/operating_gates.json` mục `operations`.
- Kèm **một dòng** "`issue_refund` trên hạn mức tự động" ở bảng C3.1 Bước 2.

### C3.5 · Mở lại bản đồ dữ liệu (S1, S3, S5; viết bằng bút khác màu)

Mở lại Phiếu B mục B3. Ghi ở đây những dòng đổi so với vòng 1:

| Trường / bảng | Vòng 1 bàn đã coi là (nguồn sự thật / bản sao / chưa hỏi) | Sau khi đọc thẻ thì thấy | Ảnh hưởng tới tiền hay lỗi hãng thế nào |
|---|---|---|---|
| `policies[].effective_from` / `effective_to` | Vòng 1: nguồn sự thật về ngày hiệu lực; `index_active` được ghi là bản sao có thể lệch | S3 cho thấy ngày hiện tại là `2026-12-02`, v4 có hiệu lực từ `2026-12-01`, nhưng `index_active=true` vẫn nằm ở v3 | Agent chọn v3: từ chối hoàn 18.000đ ở S3-02, cho tự hoàn 180.000đ ở S3-04 dù v4 giới hạn tự động 100.000đ; dùng sai `fault_causes` ở S3-01 |
| `policies[].index_active` | Vòng 1: bản sao/cờ bật thủ công, không phải nguồn sự thật theo ngày | Cờ báo v3 active trong khi v4 đã bắt đầu hiệu lực; agent trace ghi `policy_id=REFUND-v3` | Ngưỡng hoàn và nguyên nhân lỗi hãng sai cho khách/hãng; phải chọn policy theo ngày hiệu lực hoặc ghim phiên bản đã xác nhận |
| `parcels[].delay_cause` / `tracking.cause_recorded` | Vòng 1: trường tracking; có thể trống, không được mặc định là bằng chứng lỗi hãng | S3-20 có `delay_cause:null`, `cause_recorded:false`, nhưng trace ghi `cause=CARRIER` | Cấm quy lỗi khi chưa có nguyên nhân được ghi nhận; chuyển người xác minh, tránh phạt oan MKD/tài xế |

---

<a id="c4"></a>

## C4 · Câu 3.1 · HAZOP của thẻ (ít nhất 3 dòng, viết bằng dữ kiện của thẻ)

*Mục riêng, không ghi đè HAZOP vòng 1 ở Phiếu B mục B4. Năm guideword và nghĩa của chúng: xem Phiếu B mục B4.*

Tool chọn phân tích: `file_carrier_fault` (lệnh ghi phạt hãng/tài xế và tạo thông báo đối tác)

| Tham số / dòng dữ liệu | Guideword (WRONG / INVALID / INCOMPLETE / PERTURBED / INCAPABLE) | Lệch cụ thể (mã ticket, trường dữ liệu của thẻ) | Hậu quả, cho ai | Hiện có gì ngăn? | Gate đề xuất + tầng |
|---|---|---|---|---|---|
| `policy_id` / `index_active` | INVALID | `S3-01@11`: `as_of=2026-12-02`, v4 hiệu lực từ 01-12 nhưng event `policy` vẫn là v3; v3 cho `FORCE_MAJEURE` vào `fault_causes`. | Ghi lỗi oan MKD và tài xế vì bão; hãng chịu phạt 120.000đ/lỗi theo thẻ, LogiX chịu tranh chấp. | Guard hiện kiểm theo policy đã chọn; chưa bảo đảm policy được chọn đúng theo ngày hiệu lực. | `pre_guard`: chọn policy duy nhất thỏa `effective_from ≤ as_of` và `effective_to` còn hiệu lực; nếu không duy nhất/không có thì escalate trước khi xử lý ticket (**chặn**). |
| `delay_cause`, `cause_recorded` | INCOMPLETE | `S3-20@11`: `delay_cause=null`, `cause_recorded=false`, nhưng tracking event có `cause=CARRIER` và agent gọi `file_carrier_fault`. | Quy lỗi hãng/tài xế khi thiếu xác nhận nguồn; tác hại chìm với MKD và đối soát. | Guard kiểm `carrier_at_fault` theo cause/policy nhưng chưa kiểm cờ `cause_recorded`. | `write_gate` cho `file_carrier_fault`: bắt buộc `cause_recorded=true` và cause có trong `fault_causes`; nếu thiếu thì deny thao tác ghi và log lý do (**chặn**). |
| `late.min_days_fee`, `auto_limit_vnd` | INVALID | `S3-02@11`: agent dùng v3 (ngưỡng phí 3 ngày), trong khi v4 có ngưỡng 2 ngày; `S3-04@11` dùng trần tự động v3 200.000đ thay vì trần v4 100.000đ. | Khách hợp lệ bị từ chối 18.000đ; ca 180.000đ tự hoàn dù phải escalate. | Không có kiểm tra ngày hiệu lực trước proposal; trần host chỉ chặn vượt tổng tiền đã thanh toán, không chặn vượt auto-limit chính sách. | Chọn policy theo ngày hiệu lực và kiểm `amount_vnd ≤ auto_limit_vnd`; vượt trần thì bắt buộc approver hợp lệ hoặc escalate (**chặn**). |
| `index_active` cập nhật sau ngày ban hành | INCAPABLE | Nhánh chưa thấy riêng trên trace: quy trình triển khai chính sách mới không cập nhật cache/index hoặc không có người xác nhận việc đổi phiên bản lúc 00:00 ngày hiệu lực. | Toàn bộ ca sau ngày đổi bị xử lý theo luật cũ; hoàn sai/thiếu và phạt oan có thể tăng hàng loạt. | Có ngày hiệu lực trong bảng policy, nhưng cờ active do người bật tay và không có cảnh báo lệch. | Monitor so policy đang dùng với policy hiệu lực theo `as_of`; báo động đỏ và tạm dừng `issue_refund`/`file_carrier_fault` nếu lệch (**phát hiện + giới hạn thiệt hại**). |

Bắt buộc: ít nhất ba dòng, trong đó **một dòng là nhánh bàn chưa thấy trên trace** lúc viết.

---

<a id="c5"></a>

## C5 · Câu 3.2, 3.3 · Specification và giả định môi trường

### Câu 3.2 · Một specification mà nếu bị vi phạm thì gây ra tác hại trên thẻ

Kiểm được bằng code hoặc bằng một con số trong report: **Trước mọi lệnh `file_carrier_fault`, phải chọn đúng policy có hiệu lực tại `as_of`; chỉ cho ghi khi `cause_recorded=true`, `delay_cause` thuộc `fault_causes` của policy đó và `delay_days` đạt ngưỡng. Nếu thiếu nguyên nhân hoặc policy hiệu lực không xác định, không ghi lỗi hãng và chuyển người duyệt.**

Kiểm bằng gì (hàm trong `guards.py`, dòng report nào): **`pre_guard(ctx)` xác nhận policy theo `effective_from/effective_to`; `write_gate(ctx, action)` kiểm cause và ngưỡng trước `file_carrier_fault`. Kiểm bằng trace sự kiện `policy`, `tracking.cause_recorded`, `file_carrier_fault` và chỉ số `wrongful_carrier_faults` của report S3.**

### Câu 3.3 · Một giả định về môi trường mà người thiết kế đã ngầm tin, nhưng nhiều khả năng sai ngoài thực tế

Giả định (thứ nằm NGOÀI phần mềm): **Mỗi khi phụ lục/chính sách mới đến ngày hiệu lực, người phụ trách vận hành/chính sách sẽ kịp cập nhật và xác nhận chỉ mục policy đang chạy; tracking của hãng cũng sẽ ghi nguyên nhân chịu trách nhiệm trước khi LogiX ghi lỗi.**

Vì sao có thể sai: **Việc phát hành chính sách và đồng bộ chỉ mục là quy trình người-thật, có thể trễ hoặc thiếu xác nhận; S3 cho thấy ngày 02-12-2026 v4 đã hiệu lực từ 01-12 nhưng `index_active` vẫn trỏ v3. Dữ liệu của hãng cũng có thể đến thiếu: S3-20 có `delay_cause:null` và `cause_recorded:false`. Vì vậy không thể dựa vào giả định rằng policy cache và tracking luôn được cập nhật đúng hạn/đủ trường.**

---

<a id="c6"></a>

## C6 · Câu 3.4 · Fault tree TRƯỚC khi sửa (mã lần chạy: `R-S3-before-20261118-171432-c94b28`)

**Khung tư duy.** Đi từ **tác hại** ngược về nguyên nhân, không đi từ lỗi mình tình cờ thấy. Mỗi tầng hỏi "điều gì phải xảy
ra thì điều trên mới xảy ra", nối bằng **HOẶC** (một trong các nhánh là đủ) hoặc **VÀ** (phải đồng thời). Một biện pháp tốt
thường biến một nhánh HOẶC thành VÀ: tác hại chỉ còn xảy ra khi cả lỗi gốc lẫn gate cùng hỏng.

**Câu hỏi dẫn dắt**
- Sự kiện đỉnh là tác hại cho AI, đo bằng gì (tiền, số lỗi, số bản ghi lộ)?
- Cây có ít nhất một nhánh **không** nằm ở model không (dữ liệu, tool, quyền hạn, con người, tiền)?
- **Specification** nào của phần mềm bị vi phạm ở mỗi lá? **Giả định về môi trường** nào (thứ nằm ngoài phần mềm) đã sai?
- Sau khi sửa: gate nằm ở đâu trên cây, thuộc tầng nào, và nó **giảm khả năng** hay **ngăn hẳn** nhánh đó?

Ít nhất hai nhánh ở hai tầng khác nhau (kỹ thuật, kinh doanh, con người); mỗi lá có bằng chứng (ticket@seed, trường dữ liệu, hoặc một dòng của report).

```
[ĐỈNH] Hãng/tài xế bị quy lỗi và nhận phạt/thông báo oan (cho: Mekong Delta Ship, tài xế, LogiX; đo bằng: wrongful_carrier_faults; S3 base = 35)
 └─ HOẶC
 ├─ [1] Policy cũ được dùng sau ngày policy mới có hiệu lực  tầng: data / hành động
 │ └─ vì: index_active vẫn trỏ REFUND-v3 nên FORCE_MAJEURE còn nằm trong fault_causes; bằng chứng: S3-01@11, as_of=2026-12-02, event policy=REFUND-v3
 ├─ [2] Tracking thiếu cause nhưng agent mặc định thành CARRIER  tầng: data / hành động
 │ └─ vì: cause_recorded=false và delay_cause=null không chặn lệnh ghi; bằng chứng: S3-20@11, tracking rồi file_carrier_fault
 └─ [3] Không có người xác nhận rollout policy MÀ thao tác ghi lỗi vẫn bật theo cache cũ  tầng: vận hành + quyền hạn
   ├─ vì: cờ active cần cập nhật thủ công nhưng thiếu kiểm nhận trước giờ hiệu lực; bằng chứng: policies[].effective_from=2026-12-01, index_active v3, thông điệp S3 card ngày 02-12
   └─ VÀ `file_carrier_fault` vẫn được phép chạy tự động; bằng chứng: `config/switches.json` đang bật thao tác này
```

| Lá | Specification bị vi phạm (phần mềm phải làm gì) | Giả định môi trường đã sai (thế giới ngoài phần mềm) |
|---|---|---|
| [1] | Trước khi dùng policy cho bất kỳ hành động nào, chọn phiên bản thỏa `effective_from ≤ as_of` và `effective_to` còn hiệu lực; không dùng cờ cache làm nguồn quyết định. | Người phụ trách không cập nhật/xác nhận chỉ mục policy đúng ngày hoặc rollout bị trễ. |
| [2] | Chỉ gọi `file_carrier_fault` khi `cause_recorded=true` và `delay_cause` thuộc `fault_causes` của policy hiệu lực; thiếu dữ liệu thì không ghi, chuyển người. | Feed tracking của hãng có thể thiếu nguyên nhân hoặc nhập bù muộn; `null` không có nghĩa là `CARRIER`. |
| [3] | Mọi lần đổi policy phải được kiểm tra hiệu lực và người chịu trách nhiệm trước khi bật tự động; lệnh ghi lỗi cần phê duyệt khi policy/cause chưa xác nhận. | Không có quy trình rollout/đầu mối xác nhận với hãng trước ngày hiệu lực; tin nhắn S3 nêu phụ lục mới nhưng không ai ở LogiX xác nhận. |

**Ví dụ mẫu một nhánh (bộ nền, đừng chép):** đỉnh "hãng VNX nhận lỗi oan cho đơn O-1002" ← [1] agent dùng độ trễ 5 ngày ←
model lấy số trong ticket đè lên DB (`T-002@55`). Spec bị vi phạm: độ trễ dùng để ghi lỗi phải lấy từ tracking DB. Giả định
môi trường sai: "khách ghi đúng số ngày trễ". Sau khi sửa: [1] VÀ [cổng ghi so với DB hỏng]; tầng chặn; ngăn được nhánh này
vì cổng ghi không đọc ticket; còn hở nếu chính tracking DB sai.

---

<a id="c7"></a>

## C7 · Câu 3.5 · Bảng sửa: nguyên nhân → chỗ sửa → giảm hay ngăn

Sửa NGOÀI model, đúng chỗ cho từng nguyên nhân. Code: `lab10/guards.py` (`pre_guard`, `write_gate`). Con số và quy trình:
`config/operating_gates.json` (phạm vi, người trực, trần, ngân sách, kiểm mẫu, ghi chú giải thích, cổng pháp lý). Rồi chạy:

```bash
python3 -m lab10.eval --suite Sx --stage after --note "đổi MỘT thứ: ..."
python3 -m lab10.grade --incident Sx
```

| Nhánh fault tree | Nguyên nhân | Chỗ sửa (hàm + nhánh trong `guards.py`, hoặc khoá trong `operating_gates.json`) | Tầng (phát hiện / chặn / giới hạn thiệt hại / vận hành) | GIẢM khả năng hay NGĂN hẳn? Vì sao | Mã lần chạy sau khi sửa |
|---|---|---|---|---|---|
| [1] | | | | | |
| [2] | | | | | |
| [3] | | | | | |

---

<a id="c8"></a>

## C8 · Câu 3.6 · Chỉ số theo dõi mới (thước đo → dữ liệu → cách tính)

Thêm **ít nhất một hàm** trong `lab10/monitors.py` và đăng ký vào `MONITORS`. Chỉ số `escalation_rate` có sẵn không tính là chỉ số mới.
Thẻ S5 dùng mục này cho một con số kinh doanh: chi phí mỗi ticket theo kho (tách tiền máy, công người, tiền mất).

| | Chỉ số theo dõi mới của bàn |
|---|---|
| **Tên trong `MONITORS`** | |
| **Bước / hành vi được đo** | |
| **Thước đo** (một câu, có đơn vị) | |
| **Dữ liệu** (trường nào của trial, không có nhãn) | |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | |
| **Khung thời gian / ngưỡng báo động** | |
| **Điểm mù** (chỉ số này KHÔNG thấy gì) | |
| Giá trị trên bộ nền · trên thẻ (đọc mục `monitor` của report) | |

---

<a id="c9"></a>

## C9 · Câu 3.7 · Fault tree SAU khi sửa (mã lần chạy: `__________`)

Vẽ lại cây ở C6. Ở mỗi nhánh đã xử lý, thêm một nút `VÀ [gate … hỏng]` và ghi:

```
[ĐỈNH] ______________________________
 └─ HOẶC
 ├─ [1] ______________ VÀ [gate ______ hỏng]
 ├─ [2] ______________ VÀ [gate ______ hỏng]
 └─ [3] ______________ (còn hở?)
```

| Nhánh | Gate (hàm trong `guards.py` / khoá config / metric trong `monitors.py`) | Tầng gate (phát hiện / chặn / giới hạn thiệt hại / vận hành) | Giảm hay ngăn? Vì sao | Nhánh còn hở |
|---|---|---|---|---|
| [1] | | | | |
| [2] | | | | |
| [3] | | | | |

---

<a id="c10"></a>

## C10 · Câu 3.7 · Risk register (thêm ít nhất 1 dòng sau sự cố)

| Rủi ro | Khả năng | Tác động | Người phụ trách (PIC, một người) | Dấu hiệu (metric nào, ngưỡng nào) | Xử lý | Ảnh hưởng bước đánh giá | Nhóm chức năng (GOVERN / MAP / MEASURE / MANAGE) |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

Quy tắc: **mỗi dòng phải đổi được một quyết định.** Cột "Dấu hiệu" phải là một metric có trong `monitors.py` hoặc trong report.

---

<a id="c11"></a>

## C11 · Câu 3.7 · Cập nhật checklist 9 nhóm việc và Runbook phần 4–5

### Cập nhật checklist (bảng gốc ở Phiếu B mục B5)

Ghi các dòng đổi sau sự cố. Mỗi dòng vẫn phải có một PIC có tên.

| # nhóm | Trạng thái mới (Xong / Chưa / Không áp dụng) | Bằng chứng mới (mã lần chạy, mục phiếu, số trong report) | PIC |
|---|---|---|---|
| | | | |
| | | | |

### Runbook 4 · Sau sự cố trên thẻ (vòng 2)

| Câu hỏi | Trả lời |
|---|---|
| Tín hiệu nào ở Runbook 2 (Phiếu B mục B7.5) lẽ ra phải báo trước sự cố này? Nó đã có chưa? | |
| Bàn thêm hoặc đổi ngưỡng nào, từ bao nhiêu thành bao nhiêu? | |
| Bàn đổi gì về **người** (số người trực, ai đứng tên, ai được gọi)? | |
| Bàn đổi gì về **phạm vi** hoặc **quy trình** (kiểm mẫu, ghi chú giải thích, trần)? | |
| Nói gì với bên thứ ba bị ảnh hưởng (hãng, shop, người nhận, nhân viên duyệt), ai nói, trong bao lâu? | |
| Dữ liệu cá nhân nào đã rời hệ thống mà không thu hồi được? Báo cho ai? | |
| Sự cố lộ ra trước qua số máy đo, phản hồi của người, hay đọc nội dung? Nguồn nào bàn chưa có? | |

### Runbook 5 · Ba kịch bản "nếu … thì …" cho tuần đầu chạy thử thật

1. Nếu số ticket tăng gấp ___ lần trong một giờ thì: …
2. Nếu nhà cung cấp LLM lỗi quá ___ phút thì: …
3. Nếu người duyệt báo không tin một quyết định của trợ lý thì: …

---

<a id="c12"></a>

## C12 · Quyết định Gate 1 · v2 (phút 185–200)

Quyết định phải khớp bằng chứng và khớp tiêu chí đã ký. Chọn **Tiếp tục** khi report còn dòng vượt trần, hoặc còn ngưỡng đã ký
chưa đạt, là quyết định không đạt. **Thu hẹp**, **Cải tiến thêm**, **Dừng** có lý do và có số thì đều là quyết định đạt.
Cột v1 nằm ở Phiếu B mục B8; không sửa cột đó.

| | **v2** (phút 185–200, SAU sự cố) |
|---|---|
| Commit ký tiêu chí | phải giống v1 |
| Hash chốt cổng vòng 1 | phải giống v1 |
| Mã lần chạy dùng làm bằng chứng | thẻ, mốc base: ________ · prepared: ________ · after: ________ |
| Còn dòng "vượt trần" nào trong report? (hàng chờ, chi phí, ROI, trần tiền, pháp lý) | |
| Kho hoặc hãng có số xấu nhất: ____. Nếu chỉ nhìn phân khúc này, quyết định có đổi không? *(Khối "theo kho và hãng" trong output `lab10.eval` / `lab10.grade`, hoặc mục `by_segment` trong `report.json`.)* | |
| Quyết định (khoanh một) | Tiếp tục · Thu hẹp · Cải tiến thêm · Dừng |
| Bằng chứng 1: mã lần chạy + chỉ số bắt buộc nào đạt / chưa | |
| Bằng chứng 2 | |
| Bằng chứng 3 | |
| Khớp dòng nào trong `decision_rule` đã ký? | |
| Nếu Thu hẹp: cắt kho nào / còn bao nhiêu phần trăm / mấy người trực, và ticket bị cắt đi đâu | |
| Nếu Cải tiến thêm: giả thuyết cụ thể (nhánh nào của fault tree) + hạn | |
| Nếu Dừng: bài học ghi lại | |
| Ngày quyết định lại (trừ khi Dừng) | |
| PIC ký | |

**Chỉ ở v2**
- Quyết định đổi hay giữ so với v1? Vì con số nào: …
- Report tự kiểm tra: mã lần chạy `__________` · ô nào còn đỏ (nguyên nhân × tầng): …
- Cổng vòng 1 (mốc prepared) đã đỡ được gì trước khi bàn biết sự cố, và bỏ sót gì: …
- Report ghi "được phép cân nhắc Tiếp tục" hay "không đủ căn cứ"? Quyết định của bàn có khớp không: …
- Một thứ bộ thử hôm nay chưa đo, và nó ảnh hưởng quyết định ra sao: …

**Ba dòng bắt buộc** (chép nguyên ba câu này sang `submission/submission.json`, mục `three_lines`)
1. Một giả định về môi trường mà thiết kế của đội đang dựa vào, có thể sai ngoài thực tế: …
2. Gate của đội chỉ GIẢM khả năng hay thực sự NGĂN được tác hại? Vì sao: …
3. Vì data là mock, cần đo lại gì trong pilot thật trước Bước đánh giá 2: …
