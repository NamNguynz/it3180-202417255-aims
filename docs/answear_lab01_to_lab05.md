## 1. Lab 01: Thiết lập Môi trường & Refactor Flow

### Câu hỏi 1.1: Cấu hình `--global` được lưu ở đâu? Khác gì so với cấu hình `--local`?

**Trả lời:**

Trong Git, hệ thống quản lý cấu hình theo cấu trúc phân cấp nhiều tầng để linh hoạt thiết lập môi trường cho người dùng và dự án.

- **Vị trí lưu trữ cấu hình `--global`:**
  Cấu hình cấp độ toàn cục (`--global`) được lưu trữ tại tệp `.gitconfig` nằm trong thư mục cá nhân của người dùng (User Home Directory).

- **So sánh giữa `--global` và `--local`:**

| Tiêu chí | Cấu hình `--global` | Cấu hình `--local` |
| :--- | :--- | :--- |
| **Vị trí tệp** | `~/.gitconfig` (thư mục home người dùng) | `.git/config` (nằm trong thư mục `.git` của repository) |
| **Phạm vi áp dụng** | Áp dụng cho **tất cả** các repository của người dùng đó trên máy tính. | Chỉ áp dụng duy nhất cho **một repository cụ thể** chứa tệp cấu hình đó. |
| **Độ ưu tiên** | Mức ưu tiên trung bình (thấp hơn `--local`, cao hơn `--system`). | Mức ưu tiên **cao nhất** (đè lên/override cả `--global` và `--system`). |
| **Mục đích sử dụng** | Thiết lập thông tin cá nhân dùng chung như `user.name`, `user.email`, `core.editor`, `init.defaultBranch`. | Thiết lập cấu hình đặc thụ dự án như `user.email` dành riêng cho doanh nghiệp, cấu hình `remote.origin.url`, hoặc chính sách `pull.rebase`. |

---

### Câu hỏi 1.2: Vì sao nên dùng lệnh `git mv` thay vì di chuyển tệp bằng hệ điều hành hoặc File Explorer rồi chạy `git add`?

**Trả lời:**

Khi di chuyển hoặc đổi tên một tệp tin trong thư mục làm việc (Working Directory) bằng các công cụ bên ngoài Git (như lệnh `mv` của OS, Visual Studio Code Explorer, hoặc File Explorer):
1. Git sẽ ghi nhận tệp cũ ở trạng thái bị xóa (`deleted`) và một tệp mới hoàn toàn xuất hiện ở trạng thái chưa theo dõi (`untracked`).
2. Người dùng sau đó phải thực hiện lệnh `git add` cho cả tệp cũ đã xóa và tệp mới được tạo để đưa cả 2 hành động vào Staging Area.

Trái lại, lệnh **`git mv <đường_dẫn_cũ> <đường_dẫn_mới>`** thực hiện trọn vẹn 3 bước trong một thao tác duy nhất:
1. Di chuyển/Đổi tên tệp trong Working Directory.
2. Xóa tệp ở đường dẫn cũ khỏi Staging Area.
3. Thêm tệp ở đường dẫn mới vào Staging Area.

**Lợi ích cốt lõi đối với Quản lý Cấu hình:**
- **Bảo toàn lịch sử thay đổi:** Git giúp thuật toán phát hiện đổi tên (rename detection) hoạt động chính xác tuyệt đối với độ tương đồng (similarity index) 100%.
- **Tránh sai sót khi Stage:** Giúp lập trình viên không lỡ quên `git add` tệp cũ bị xóa, tránh tình trạng tệp cũ vẫn tồn tại trong commit tiếp theo hoặc gây lỗi rác cấu hình.
- **Trực quan trên GitHub:** Khi xem Pull Request trên giao diện GitHub, tab *Files changed* sẽ hiển thị rõ ràng biểu tượng `RENAME` kèm đường dẫn thay đổi thay vì hai hành động tách biệt là xóa tệp và thêm tệp mới.

---

### Câu hỏi 1.3: Nhánh `release/lab01` có phải là một Baseline không?

**Trả lời:**

**Có.**

Theo định nghĩa lý thuyết SCM, một Baseline là một trạng thái mã nguồn/cấu hình đã được thống nhất, kiểm thử, duyệt thông qua và đóng băng tại một thời điểm nhất định. Baseline làm mốc tham chiếu cho các hoạt động phát triển tiếp theo và chỉ được phép thay đổi theo quy trình kiểm soát chính thức.

---

### Câu hỏi 1.4: Vì sao không nên commit trực tiếp lên nhánh `master` ngay cả khi làm việc một mình?

**Trả lời:**

Mặc dù khi làm việc cá nhân không có nguy cơ xung đột tức thì từ đồng nghiệp, việc tuân thủ quy tắc **"Không commit trực tiếp lên `master` và `release/*`"** mang lại những giá trị SCM căn bản:

1. **Rèn luyện tư duy và thói quen SCM chuyên nghiệp:** Trong môi trường dự án thực tế, `master`/`main` là nhánh sản phẩm đang chạy (Production-ready). Việc thao tác qua nhánh riêng (`refactor/*`, `feature/*`, `bugfix/*`) và Pull Request giúp duy trì tính kỷ luật cấu hình.
2. **Kích hoạt quy trình kiểm duyệt tự động (Self-Review & CI):** Khi tạo Pull Request, giao diện GitHub cung cấp góc nhìn tổng thể (*Files changed*) giúp bản thân lập trình viên tự rà soát lại toàn bộ khác biệt mã nguồn (diff), phát hiện các tệp rác (như `__pycache__`, tệp tạm ẩn) hoặc lỗi chính tả trước khi tích hợp vào nhánh chính.
3. **Bảo vệ nhánh chính luôn hoạt động (Clean & Green Master):** Nhánh `master` luôn được đảm bảo chứa mã nguồn đã chạy qua kiểm thử (unit test). Nếu phát triển thẳng trên `master`, một commit dở dang hoặc bị lỗi sẽ làm hỏng toàn bộ dự án.
4. **Lịch sử Git rõ ràng và dễ truy vết:** Mọi thay đổi tích hợp vào `master` đều để lại vết dưới dạng một Merge Commit (hoặc PR Commit) liên kết trực tiếp với mô tả công việc (Issue/Task), giúp việc tra cứu lịch sử về sau rất dễ dàng.

---

## 2. Lab 02: Feature/Topic Flow & Kiểm soát Thay đổi qua Pull Request

### Câu hỏi 2.1: Vì sao phải đồng bộ nhánh `master` mới nhất trước khi gửi hoặc merge Pull Request?

**Trả lời:**

Trong môi trường phát triển song song, nhánh `master` trên máy chủ từ xa (Remote repository) liên tục tiến về phía trước do các Pull Request của các thành viên khác (hoặc các nhánh tính năng khác) được hoàn thành và merge vào.

Khi nhánh tính năng của bạn (ví dụ: `feature/search-by-title`) được tách ra từ một commit `master` cũ:
1. **Phát hiện và xử lý xung đột sớm tại địa phương:** Nếu không đồng bộ `master` mới vào nhánh tính năng trước khi tạo/merge PR, bạn sẽ không phát hiện ra các xung đột mã nguồn (merge conflict) hoặc xung đột logic (logical conflict) giữa tính năng của bạn và các thay đổi vừa được chèn vào `master`.
2. **Đảm bảo tính đúng đắn khi tích hợp (Integration Test):** Việc kéo `master` mới về nhánh cá nhân (qua `git fetch` và `git merge origin/master`), sau đó chạy thử toàn bộ bộ kiểm thử (test suite) giúp xác nhận rằng mã nguồn mới hoàn toàn tương thích với trạng thái hiện tại của hệ thống.
3. **Tuân thủ nguyên tắc SCM:** Đảm bảo "thứ được duyệt và tích hợp chính là thứ sẽ chạy trên nền mã nguồn mới nhất của hệ thống".

---

### Câu hỏi 2.2: Khi nào tuyệt đối không được sử dụng thao tác Rebase?

**Trả lời:**

**Quy tắc vàng trong Git:** Tuyệt đối không bao giờ thực hiện `git rebase` trên các **nhánh công khai (public/shared branches)** — tức các nhánh đã được push lên server từ xa và có nhiều người khác cùng kéo về làm việc (như `master`, `main`, `release/*`, hoặc các nhánh `feature` dùng chung trong nhóm).

**Lý do kỹ thuật và hậu quả SCM:**
- Thao tác `git rebase` hoạt động bằng cách tính toán lại khác biệt và tạo ra các commit mới hoàn toàn với mã băm (SHA hash) mới, đè lên lịch sử cũ.
- Nếu rebase một nhánh chung, lịch sử commit của nhánh đó trên máy bạn sẽ bị sai lệch hoàn toàn so với máy của các đồng nghiệp. Khi họ thực hiện `git pull`, Git sẽ rơi vào trạng thái xung đột hỗn loạn (merge hell), buộc phải thực hiện merge lặp đi lặp lại hoặc dùng `push --force` đè mất công sức làm việc của người khác.

**Chỉ dùng `rebase` khi:** Nhánh đó là nhánh cá nhân, sống ngắn (`feature/*`, `topic/*`), chưa chia sẻ với ai hoặc chỉ do một mình bạn kiểm soát hoàn toàn trước khi gộp vào `master`.

---

### Câu hỏi 2.3: Sự khác biệt giữa nhánh `feature/*` và nhánh `topic/*` là gì?

**Trả lời:**

Cả hai loại nhánh này đều thuộc nhóm nhánh sống ngắn (short-lived branches) trong Release Flow, được tạo ra từ `master` và gộp lại vào `master`. Tuy nhiên, chúng khác nhau về mục đích sử dụng và đối tượng thay đổi:

| Tiêu chí | Nhánh `feature/*` | Nhánh `topic/*` |
| :--- | :--- | :--- |
| **Cú pháp đặt tên** | `feature/<tên-tính-năng>` (ví dụ: `feature/cart-print`, `feature/search-by-title`) | `topic/<mô-tả-chủ-đề>` (ví dụ: `topic/pr-template`, `topic/use-case-diagram`) |
| **Mục đích chính** | Phát triển các **tính năng nghiệp vụ mới** cho ứng dụng/phần mềm. | Thực hiện các **chủ đề công việc phụ trợ**, cải tiến hạ tầng, cấu hình dự án hoặc tài liệu. |
| **Thành phần thay đổi** | Mã nguồn chính của ứng dụng (`aims/`, `src/`) và các bài unit test đi kèm. | Tệp cấu hình CI/CD, tài liệu dự án (`docs/`), khuôn mẫu Pull Request (`.github/`), tài liệu thiết kế. |
| **Đánh số phiên bản** | Thường đóng góp vào việc tăng chỉ số **MINOR** khi phát hành phiên bản mới. | Thường chỉ ghi nhận dưới dạng công việc phụ trợ (`chore` / `docs`) và không làm tăng phiên bản nghiệp vụ. |

---

## 3. Lab 03: Bugfix Flow, Xung đột & Quy trình Hoàn tác

### Câu hỏi 3.1: Merge Base trong Git là gì và vai trò của nó trong quá trình hợp nhất nhánh?

**Trả lời:**

**Định nghĩa:**
`Merge Base` là commit tổ tiên chung gần nhất (most recent common ancestor) của hai hoặc nhiều nhánh trong đồ thị lịch sử (commit graph) của Git.

**Vai trò trong hợp nhất nhánh:**
Khi bạn thực hiện lệnh gộp nhánh (như `git merge`), Git không chỉ so sánh đơn thuần giữa hai commit đầu nhánh (HEADs). Thay vào đó, Git sử dụng thuật toán **Hợp nhất 3 chiều (Three-Way Merge)** dựa trên 3 điểm mốc:
1. Trạng thái mã nguồn tại **Merge Base** (tổ tiên chung).
2. Trạng thái mã nguồn tại **HEAD của Nhánh hiện tại** (nhánh đích, ví dụ: `master`).
3. Trạng thái mã nguồn tại **HEAD của Nhánh được gộp** (nhánh nguồn, ví dụ: `feature/cart-print`).

Nhờ có Merge Base làm điểm mốc trung hòa, Git xác định chính xác những dòng mã nào đã bị thay đổi bởi nhánh A và những dòng nào bị thay đổi bởi nhánh B kể từ mốc tách nhánh. Từ đó, Git tự động tổng hợp các thay đổi không chồng chéo và chỉ phát cảnh báo xung đột (Merge Conflict) khi cả hai nhánh cùng sửa đổi trên cùng một dòng mã (hoặc vùng mã lân cận) so với mốc Merge Base.

---

### Câu hỏi 3.2: Vì sao đối với các nhánh chính như `master` và `release/*` bắt buộc phải dùng `git revert` thay vì `reset`, `amend` hay `rebase` khi muốn hoàn tác?

**Trả lời:**

Trong Quản lý Cấu hình, các nhánh `master` và `release/*` là các dòng vết lịch sử đã chia sẻ và được bảo vệ (Protected Branches).

- **Hạn chế của `reset`, `amend`, `rebase`:**
  Các lệnh này hoạt động theo cơ chế **viết lại lịch sử (rewrite history)**. Chúng làm thay đổi mã băm SHA hoặc xóa bỏ hẳn các commit đã tồn tại ra khỏi cây lịch sử.
  Nếu áp dụng các lệnh này lên `master` hoặc `release/*`:
  - Lịch sử mã nguồn tại local sẽ bị lệch so với remote và máy của các thành viên khác trong nhóm.
  - Phá hủy tính kiểm toán (auditability): Mất vết ghi nhận về việc thay đổi lỗi đã từng xảy ra và ai đã thực hiện nó.
  - Yêu cầu quyền `push --force` (một thao tác bị cấm hoàn toàn trên các Protected Branches).

- **Ưu thế tuyệt đối của `git revert`:**
  Lệnh `git revert <commit-SHA>` không xóa commit cũ. Thay vào đó, nó tạo ra một **commit mới** có nội dung đảo ngược hoàn toàn những thay đổi do commit lỗi gây ra.
  - **Giữ nguyên lịch sử liên tục:** Cây lịch sử commit hoàn toàn tiến về phía trước, không có commit nào bị mất đi.
  - **An toàn cho làm việc nhóm:** Không gây lệch lịch sử cho các thành viên khác khi họ `git pull`.
  - **Đảm bảo kiểm toán SCM:** Ghi vết rõ ràng lịch sử hệ thống: "Commit A bị lỗi đã được tích hợp lúc t1, và Commit B (revert của A) đã đảo ngược lỗi đó lúc t2".

---

## 4. Lab 04: Release Flow, Semantic Versioning & Ghi nhận Trạng thái

### Câu hỏi 4.1: Vì sao phải thực hiện công tác chuẩn bị phát hành trên `master` trước thay vì sửa trực tiếp trên nhánh `release/*`?

**Trả lời:**

Trong bài Lab 04, quy trình chuẩn bị phát hành (tạo nhánh `topic/prepare-release-1.0.0`) bao gồm các công việc: cập nhật chuỗi phiên bản `__version__ = "1.0.0"`, cập nhật giao diện ứng dụng, và tổng hợp tệp `CHANGELOG.md`.

Các thao tác này phải thực hiện trên `master` trước vì:

1. **Nguyên tắc "Master chứa mọi giá trị phát triển":** Tất cả các thông tin tài liệu, CHANGELOG, và mốc phiên bản đều là tài sản mã nguồn lâu dài của dự án. Nhánh `master` phải là nơi chứa đầy đủ nhất các tài sản này.
2. **Quy trình tạo nhánh Release tự nhiên:** Nhánh `release/lab04` được tạo ra từ `master` tại điểm cuối cùng sau khi `master` đã hoàn tất việc chuẩn bị. Khi đó, `release/lab04` nghiễm nhiên sở hữu đầy đủ thông tin phiên bản `1.0.0` và `CHANGELOG.md` chuẩn mà không cần thêm bất kỳ thao tác chỉnh sửa nào nữa.
3. **Tránh nguy cơ lệch mã nguồn (Code Drift):** Nếu sửa trực tiếp trên `release/lab04`, ta sẽ phải tìm cách chuyển các commit chuẩn bị đó ngược về `master`. Việc này làm gia tăng nguy cơ xung đột và vi phạm quy tắc cốt lõi của Release Flow: *"Nhánh release/* không bao giờ merge ngược vào master"*.

---

### Câu hỏi 4.2: Vì sao nhánh `release/*` không bao giờ merge ngược vào `master`? So sánh với mô hình GitFlow.

**Trả lời:**

- **Lý do trong Release Flow:**
  Trong mô hình Release Flow (chuẩn áp dụng tại Microsoft và học phần), nhánh `master` luôn là dòng chảy phát triển liên tục và luôn đi trước các nhánh phát hành (`release/*`).
  - Nhánh `release/*` được tách ra từ `master` chỉ để đóng băng baseline và bảo trì bản phát hành đó.
  - Nếu merge nguyên cả nhánh `release/*` ngược vào `master`, các commit quản lý dọn dẹp riêng của release có thể đè đè hoặc làm nhiễu lịch sử phát triển đang tiến lên của `master`.
  - Khi có lỗi phát sinh trên `release/*` cần sửa, bản sửa lỗi (hotfix) sẽ được đưa sang `master` bằng lệnh `git cherry-pick -x` độc lập chứ không merge toàn bộ nhánh.

- **So sánh với mô hình GitFlow cổ điển:**

| Tiêu chí | Release Flow (Học phần / Microsoft) | GitFlow Cổ điển |
| :--- | :--- | :--- |
| **Cấu trúc nhánh chính** | Chỉ có **1 nhánh chính duy nhất** là `master` (hoặc `main`). | Có **2 nhánh chính sống song song** là `main` (chứa code production) và `develop` (chứa code tích hợp). |
| **Luồng merge của Release** | Nhánh `release/labXX` rẽ ra từ `master` và **không bao giờ merge ngược** lại `master`. | Nhánh `release` rẽ ra từ `develop`, sau khi hoàn thiện phải **merge vào CẢ `main` lẫn `develop`**. |
| **Độ phức tạp** | Đơn giản, nhẹ nhàng, lịch sử tuyến tính, phù hợp với CI/CD hiện đại. | Phức tạp, nhiều thao tác merge chéo, dễ gây xung đột khi số lượng release tăng lên. |

---

### Câu hỏi 4.3: Vì sao hệ thống phiên bản được nâng lên mốc `1.0.0` ở Lab 04 mà không phải là `0.4.0`?

**Trả lời:**

Quy tắc đặt số phiên bản dựa trên chuẩn **Semantic Versioning (SemVer - `MAJOR.MINOR.PATCH`)**:

1. **Giai đoạn `0.y.z` (Lab 01 đến Lab 03):**
   - Định dạng `0.y.z` (như `v0.1.0`, `v0.2.0`, `v0.3.0`) đại diện cho giai đoạn phát triển ban đầu (Initial Development).
   - Ở giai đoạn này, phần mềm chưa ổn định, giao diện lập trình (API) có thể thay đổi liên tục và chưa sẵn sàng chuyển giao chính thức cho người dùng cuối.

2. **Cột mốc `1.0.0` (Lab 04):**
   - Tại Lab 04, ứng dụng AIMS-mini đã hoàn thiện trọn vẹn các tính năng cơ bản, vượt qua toàn bộ các bài kiểm thử tự động, có tài liệu hướng dẫn và tệp `CHANGELOG.md` chỉn chu.
   - Đây là mốc đóng băng Baseline phát hành chính thức đầu tiên (Production Release / Public API release).
   - Theo chuẩn SemVer, khi một sản phẩm đạt độ chín, ổn định và sẵn sàng đưa tới tay người dùng sử dụng chính thức, số **MAJOR** bắt buộc phải tăng lên `1.0.0` để đánh dấu cột mốc thương mại/sản xuất này.

---

## 5. Lab 05: Hotfix Flow & Bảo trì Đa phiên bản

### Câu hỏi 5.1: Vì sao ở Phần A của Lab 05 chưa gắn tag `v1.1.0` ngay khi vừa tạo nhánh `release/lab05`?

**Trả lời:**

Trong Quản lý Cấu hình, **Tag** trong Git là một mốc cố định bất biến (Immutable Marker). Một khi tag đã được đánh dấu và push lên máy chủ từ xa, nguyên tắc SCM quy định tuyệt đối không được xóa hay di chuyển tag đó sang commit khác.

- Tại Phần A của Lab 05, nhánh `release/lab05` vừa mới được khởi tạo từ `master` để chuẩn bị cho bài nộp tuần mới, nhưng **chưa thực sự đóng băng kiểm thử cuối cùng**.
- Nếu đánh tag `v1.1.0` ngay lập tức tại Phần A: Khi phát sinh sự cố khẩn cấp (như bài lab yêu cầu thực hiện sửa lỗi hotfix trên nhánh release), commit mới chứa bản vá sẽ nằm sau mốc tag `v1.1.0`. Lúc này, bản vá lỗi sẽ buộc phải mang số phiên bản vá là `v1.1.1`.
- Việc trì hoãn gắn tag cho đến khi nhánh release đã tích hợp đầy đủ mọi bản sửa lỗi cần thiết (ở Phần E) giúp mốc tag `v1.1.0` đại diện chính xác cho phiên bản hoàn chỉnh, sạch lỗi tới tay người dùng.

---

### Câu hỏi 5.2: Phân tích ưu điểm và nhược điểm của chiến lược Upstream First so với Release First?

**Trả lời:**

Khi phát sinh lỗi trên một phiên bản đã phát hành, có hai chiến lược xử lý hotfix chính:

#### 1. Chiến lược Release First (Thực hiện trong bài Lab 05)
Tạo nhánh hotfix từ nhánh release bị lỗi (`release/lab04`), sửa lỗi, phát hành bản PATCH (`v1.0.1`), sau đó dùng `git cherry-pick -x` lan truyền bản sửa sang `master` và các nhánh release khác (`release/lab05`).
- **Ưu điểm:** Khắc phục sự cố khẩn cấp vô cùng nhanh chóng trên môi trường Production, giảm tối đa thời gian gián đoạn của người dùng cuối.
- **Nhược điểm:** Đòi hỏi quy trình kiểm toán (Configuration Audit) rất chặt chẽ. Nếu lập trình viên quên lan truyền commit hotfix sang `master` hoặc các nhánh release đang sống khác, lỗi sẽ bị tái phát (regression bug) ở các phiên bản tiếp theo.

#### 2. Chiến lược Upstream First (Chuẩn của Microsoft Release Flow)
Tạo nhánh sửa lỗi từ nhánh chính `master` (Upstream) trước, thực hiện review/CI và merge vào `master`, sau đó mới `cherry-pick -x` commit đó về các nhánh `release/*` cần vá lỗi.
- **Ưu điểm:** Đảm bảo triệt để nguyên tắc "mọi bản sửa lỗi phải có mặt trên dòng phát triển chính", loại bỏ hoàn toàn rủi ro sót lỗi trên `master` (không bao giờ lo bị tái phát lỗi ở bản nâng cấp tương lai).
- **Nhược điểm:** Tốc độ phát hành bản vá cho phiên bản cũ có thể bị chậm hơn do phải chờ đợi quy trình kiểm thử và tích hợp chung của nhánh `master`.

---

### Câu hỏi 5.3: Nếu lỡ quên lan truyền bản sửa lỗi (hotfix) sang `release/lab05`, câu lệnh hoặc cơ chế kiểm toán nào ở Phần F sẽ phát hiện ra?

**Trả lời:**

Trong Phần F của Lab 05, quy trình Kiểm toán Cấu hình Đa phiên bản (Configuration Audit) cung cấp 3 cơ chế độc lập để phát hiện ngay việc bỏ sót bản hotfix:

1. **Kiểm tra truy vết bằng lệnh `git log` với từ khóa grep:**
   ```bash
   git log --all --oneline --grep "cherry picked from commit <FIX_SHA>"
   ```
   - *Cơ chế phát hiện:* Nếu bản sửa lỗi đã được lan truyền đầy đủ sang cả `master` và `release/lab05`, lệnh này bắt buộc phải trả về **2 commit cherry-pick**. Nếu chỉ trả về 1 kết quả, hệ thống kiểm toán xác nhận ngay lập tức rằng nhánh `release/lab05` đã bị lỡ mất bản vá.

2. **Kiểm tra sự tương đương commit bằng lệnh `git cherry`:**
   ```bash
   git cherry -v origin/master origin/release/lab05
   ```
   - *Cơ chế phát hiện:* Lệnh `git cherry` sẽ so sánh nội dung khác biệt (patch id) giữa hai nhánh. Nếu `release/lab05` chưa có bản sửa lỗi tương đương, commit sửa lỗi sẽ bị đánh dấu cộng (`+`), cảnh báo rằng thay đổi chưa được đồng bộ.

3. **Chạy tự động bộ kiểm thử (Unit Test Suite) trên các dòng phiên bản:**
   ```bash
   for ref in v1.0.1 v1.1.0 master; do
       git switch --detach $ref
       python -m unittest discover -s tests -v
   done
   ```
   - *Cơ chế phát hiện:* Bài test tái hiện lỗi (ví dụ: test tìm kiếm không phân biệt hoa thường `search_by_title`) khi chạy trên `release/lab05` (mốc `v1.1.0`) sẽ báo trạng thái **FAIL**, lập tức ngăn chặn việc xuất bản một phiên bản lỗi.
