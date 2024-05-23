<p align="center">
  <img width="150" src="/readme/logo.svg" alt="Logo">
</p>

---

## Giới Thiệu

Trong thời đại số hóa ngày nay, việc quản lý thời gian và công việc trở thành một thách thức đối với nhiều người. Với sự phát triển của công nghệ thông tin, việc áp dụng các ứng dụng và công cụ kỹ thuật số để hỗ trợ quản lý công việc trở nên cần thiết và quan trọng hơn bao giờ hết. Trong tình hình này, việc phát triển một ứng dụng Todo List trở thành một dự án có ý nghĩa rất lớn, không chỉ đối với việc nâng cao hiệu suất làm việc của cá nhân mà còn là một bước tiến quan trọng trong việc ứng dụng công nghệ để giải quyết các vấn đề thực tiễn của cuộc sống.

Dự án Todo List mà chúng tôi thực hiện nhằm mục đích cung cấp cho người dùng một công cụ hiệu quả để quản lý và tổ chức các công việc hàng ngày một cách khoa học và tiện lợi nhất. Sử dụng các công nghệ web hiện đại, kết hợp với các ngôn ngữ lập trình phổ biến như Python và framework Flask, chúng tôi đã xây dựng một ứng dụng Todo List đáp ứng được nhu cầu của người dùng trong việc quản lý thời gian và công việc.

Trong phần tiếp theo của báo cáo này, chúng tôi sẽ trình bày chi tiết về quy trình phát triển dự án, các chức năng chính của ứng dụng, cũng như những học được và kết quả đạt được từ quá trình thực hiện dự án này.

---

## Lý Do Chọn Đề Tài

Nhu cầu thực tế: Trong xã hội hiện đại, cuộc sống diễn ra với tốc độ nhanh chóng và có nhiều áp lực từ công việc, học tập và cuộc sống cá nhân. Điều này tạo ra một nhu cầu cấp thiết trong việc quản lý thời gian và công việc một cách hiệu quả. Một ứng dụng Todo List có thể giúp người dùng tổ chức công việc của họ, theo dõi tiến độ và ưu tiên nhiệm vụ một cách tự nhiên và khoa học.

1. **Tính Thực Tiễn**: Todo List không chỉ là một ứng dụng phổ biến mà còn là một công cụ hữu ích và cần thiết trong cuộc sống hàng ngày của mọi người. Việc phát triển một ứng dụng Todo List không chỉ mang lại giá trị thực tiễn mà còn giúp chúng tôi hiểu rõ hơn về nhu cầu và mong muốn của người dùng.

2. **Áp Dụng Kiến Thức**: Qua việc thực hiện dự án Todo List, chúng tôi có cơ hội áp dụng và thực hành những kiến thức đã học được trong quá trình học. Từ việc lập trình backend với Python, sử dụng framework Flask, đến phát triển giao diện người dùng với HTML và CSS, chúng tôi có thể áp dụng kiến thức và kỹ năng của mình vào một dự án thực tế.

3. **Phát Triển Kỹ Năng**: Phát triển một ứng dụng Todo List không chỉ đòi hỏi kiến thức chuyên môn mà còn yêu cầu kỹ năng tổ chức, quản lý dự án và làm việc nhóm. Qua quá trình thực hiện dự án, chúng tôi có cơ hội phát triển và cải thiện những kỹ năng này, từ việc phân tích yêu cầu đến việc triển khai và duy trì ứng dụng.

4. **Tiềm Năng Thị Trường**: Với sự phát triển của công nghệ, nhu cầu sử dụng các ứng dụng và công cụ quản lý thời gian và công việc ngày càng tăng cao. Một ứng dụng Todo List có tiềm năng phát triển và thu hút người dùng trong nhiều lĩnh vực khác nhau, từ cá nhân đến doanh nghiệp.

Chính vì những lý do trên, chúng tôi đã quyết định chọn đề tài Todo List cho dự án này, hy vọng rằng dự án sẽ mang lại giá trị thực tiễn và đem lại những trải nghiệm hữu ích cho cả người dùng lẫn nhóm phát triển.

---

## Chức Năng

Dưới đây là các chức năng chính của ứng dụng Todo List:

1. **Đăng Nhập (Login)**: Người dùng có thể đăng nhập vào hệ thống để quản lý các nhiệm vụ cá nhân.
2. **Đăng Ký (Register)**: Người dùng mới có thể tạo tài khoản để sử dụng ứng dụng.
3. **Trang Chủ (Home)**: Hiển thị danh sách các nhiệm vụ và các chức năng chính.
4. **Thêm Nhiệm Vụ (Add Task)**: Người dùng có thể thêm nhiệm vụ mới.
5. **Sửa Nhiệm Vụ (Edit Task)**: Cho phép chỉnh sửa chi tiết của một nhiệm vụ.
6. **Hoàn Thành Nhiệm Vụ (Complete Task)**: Đánh dấu nhiệm vụ đã hoàn thành.
7. **Chưa Hoàn Thành Nhiệm Vụ (Incomplete Task)**: Đánh dấu nhiệm vụ chưa hoàn thành.
8. **Cập Nhật Tiến Độ (Update Progress)**: Cập nhật tiến độ thực hiện của một nhiệm vụ.
9. **Xoá Nhiệm Vụ (Delete Task)**: Xóa nhiệm vụ khỏi danh sách.
10. **Thêm Danh Mục (Add Category)**: Tạo danh mục mới để phân loại nhiệm vụ.
11. **Xoá Danh Mục (Delete Category)**: Xóa một danh mục và tất cả các nhiệm vụ liên quan.

---

## Màn Hình Ứng Dụng

### Đăng Nhập (Login)

Màn hình đăng nhập cho phép người dùng nhập tên đăng nhập và mật khẩu để truy cập vào hệ thống.

![Logo](/readme/login.png)

### Đăng Ký (Register)

Màn hình đăng ký cho phép người dùng mới tạo tài khoản bằng cách nhập thông tin cá nhân.

![Register](/readme/register.png)

### Trang Chủ (Home)

Trang chủ hiển thị danh sách tất cả các nhiệm vụ của người dùng, bao gồm các nhiệm vụ hoàn thành và chưa hoàn thành.

![Home](/readme/home.png)

### Thêm Nhiệm Vụ (Add Task)

Màn hình thêm nhiệm vụ cho phép người dùng nhập tiêu đề, mô tả, thời hạn và danh mục cho nhiệm vụ mới.

![Add Task](/readme/create_task.png)

### Sửa Nhiệm Vụ (Edit Task)

Màn hình sửa nhiệm vụ cho phép người dùng chỉnh sửa thông tin của một nhiệm vụ đã có.

![Edit Task](/readme/update_task.png)

### Thêm Danh Mục (Add Category)

Màn hình thêm danh mục cho phép người dùng tạo danh mục mới để phân loại nhiệm vụ.

![Add Category](/readme/create_category.png)

---

## Database Schema

### Bảng categories
Bảng này lưu trữ thông tin về các danh mục của các nhiệm vụ.
- **slug**: Định danh duy nhất của danh mục.
- **name**: Tên của danh mục.
- **created_by**: Người tạo danh mục.

### Bảng user
Bảng này chứa thông tin về người dùng của hệ thống.
- **username**: Tên đăng nhập của người dùng.
- **password**: Mật khẩu của người dùng.
- **role**: Quyền hạn của người dùng trong hệ thống.

### Bảng tasks
Bảng này lưu trữ thông tin về các nhiệm vụ.
- **id**: Định danh duy nhất của nhiệm vụ.
- **title**: Tiêu đề của nhiệm vụ.
- **description**: Mô tả chi tiết về nhiệm vụ.
- **priority**: Mức độ ưu tiên của nhiệm vụ.
- **category**: Danh mục của nhiệm vụ.
- **created_by**: Người tạo nhiệm vụ.
- **completed**: Trạng thái hoàn thành của nhiệm vụ.
- **progress**: Tiến độ thực hiện của nhiệm vụ.
- **created_date**: Ngày tạo nhiệm vụ.

### Sử Dụng File
Trong dự án này, sử dụng file để lưu trữ dữ liệu. Cụ thể, mỗi bảng sẽ được lưu trong một file với định dạng CSV.
- **categories.csv**: Lưu trữ thông tin về các danh mục.
- **users.csv**: Lưu trữ thông tin về người dùng.
- **tasks.csv**: Lưu trữ thông tin về các nhiệm vụ.

Mỗi dòng trong file CSV sẽ tương ứng với một bản ghi trong bảng tương ứng. Các trường dữ liệu sẽ được phân tách bằng dấu phẩy (,).

Để đảm bảo tính nhất quán và an toàn của dữ liệu, việc thao tác với file sẽ được thực hiện thông qua các hàm và phương thức xử lý dữ liệu.

---

## Cách Sử Dụng

### Đăng Ký hoặc Đăng Nhập
1. Truy cập vào trang web của ứng dụng.
2. Nếu bạn đã có tài khoản, hãy đăng nhập bằng cách nhập tên đăng nhập và mật khẩu vào form đăng nhập.
3. Nếu bạn chưa có tài khoản, hãy đăng ký bằng cách điền thông tin vào form đăng ký và nhấn nút đăng ký.

### Tạo Danh Mục (Category)
1. Sau khi đăng nhập thành công, truy cập vào trang quản lý danh mục.
2. Nhấn vào nút "Tạo Danh Mục" hoặc điền thông tin vào form tạo danh mục.
3. Nhập tên và mô tả cho danh mục mới và nhấn nút "Lưu" để tạo danh mục.

### Tạo Nhiệm Vụ (Task)
1. Truy cập vào trang quản lý nhiệm vụ.
2. Nhấn vào nút "Tạo Nhiệm Vụ" hoặc điền thông tin vào form tạo nhiệm vụ.
3. Nhập tiêu đề, mô tả và các thông tin khác cho nhiệm vụ mới.
4. Chọn danh mục cho nhiệm vụ từ danh sách đã tạo trước đó (nếu cần).
5. Nhấn nút "Lưu" để tạo nhiệm vụ mới.

### Cập Nhật Tiến Độ (Update Progress)
1. Truy cập vào phần chi tiết của nhiệm vụ cần cập nhật tiến độ.
2. Kéo nút "Cập Nhật Tiến Độ" để cập nhậ.

### Hoàn Thành Nhiệm Vụ
1. Truy cập vào phần chi tiết của nhiệm vụ cần hoàn thành.
2. Nhấn vào nút "Hoàn Thành" để đánh dấu nhiệm vụ đã hoàn thành.

---

## Cách Triển Khai Ứng Dụng

### 1. Chuẩn Bị Môi Trường Phát Triển
- Đảm bảo máy tính đang sử dụng có Python cài đặt và các công cụ phát triển cần thiết như pip.

### 2. Tải Mã Nguồn và Cài Đặt
- Tải mã nguồn của ứng dụng từ kho lưu trữ Git hoặc tệp nén từ một nguồn tin cậy.
- Giải nén tệp nếu cần và chuyển vào thư mục dự án.

### 3. Cài Đặt Môi Trường Ảo (Nếu Cần)
- Tạo một môi trường ảo Python bằng cách sử dụng công cụ như `virtualenv` hoặc `conda`.
- Kích hoạt môi trường ảo và cài đặt các gói cần thiết bằng pip.

### 4. Cấu Hình Ứng Dụng
- Cấu hình cơ sở dữ liệu: Đảm bảo rằng thông tin kết nối đến cơ sở dữ liệu được cung cấp đúng và được cấu hình trong ứng dụng.

### 5. Khởi Động Ứng Dụng
- Mở terminal và di chuyển đến thư mục dự án.
- Chạy lệnh `python app.py` để khởi động máy chủ phát triển của Flask.

### 6. Kiểm Tra và Debug
- Mở trình duyệt web và truy cập vào địa chỉ localhost:port (port mặc định thường là 5000) để kiểm tra ứng dụng.
- Theo dõi bất kỳ thông báo lỗi nào xuất hiện và debug nếu cần thiết.

### 7. Phát Triển và Kiểm Thử
- Phát triển và kiểm thử ứng dụng trên môi trường phát triển.
- Sử dụng các công cụ như Flask Debug Toolbar hoặc các logger để theo dõi lỗi và hiệu suất.

### 8. Bảo Dưỡng và Nâng Cấp
- Thực hiện bảo dưỡng định kỳ để đảm bảo tính ổn định và bảo mật của ứng dụng.
- Cập nhật và nâng cấp ứng dụng theo nhu cầu và tiêu chuẩn mới.

---

## Đội Ngũ Phát Triển

- **Người Sáng Lập:** [Dubravko Luka](https://github.com/dubravko-luka)
- **Lập Trình Viên:** [Dubravko Luka](https://github.com/dubravko-luka)
- **Thiết Kế Giao Diện:** [Dubravko Luka](https://github.com/dubravko-luka)

--- 

## Kết Luận và Cảm Ơn

Trong quá trình phát triển dự án Todo List, chúng tôi đã học được rất nhiều và có những trải nghiệm đáng giá. Dự án này không chỉ là một bước tiến quan trọng trong việc nâng cao kỹ năng lập trình và phát triển ứng dụng web của chúng tôi, mà còn là một cơ hội để chúng tôi áp dụng các kiến thức đã học vào thực tế.

Chúng tôi muốn bày tỏ lòng biết ơn sâu sắc đến những người đã hỗ trợ và động viên chúng tôi trong suốt quá trình phát triển dự án này. Đặc biệt, chúng tôi muốn gửi lời cảm ơn đặc biệt đến các thành viên trong nhóm, người thầy hướng dẫn, bạn bè và gia đình.

Dự án Todo List không chỉ là sản phẩm của chúng tôi, mà còn là một phần nhỏ bé trong cộng đồng lập trình và sử dụng ứng dụng web. Chúng tôi hy vọng rằng ứng dụng này sẽ mang lại giá trị và hữu ích cho người dùng, và chúng tôi sẽ tiếp tục phát triển và cải thiện nó trong tương lai.

Xin chân thành cảm ơn!

---

## Liên Hệ

Nếu bạn có bất kỳ câu hỏi, đề xuất hoặc gặp vấn đề về ứng dụng, vui lòng liên hệ với chúng tôi qua thông tin sau:

- Email: [dev.richard.npm98@gmail.com](mailto:dev.richard.npm98@gmail.com)
- Điện thoại: +84 3xx xxx xxx
- Địa chỉ: Số 000, Thành phố XYZ, Quốc gia ABC

Chúng tôi luôn sẵn lòng lắng nghe và hỗ trợ bạn.

## Bản Quyền

Ứng dụng Todo List được phát triển và bảo vệ bởi luật bản quyền. Mọi quyền được bảo lưu.

Đây là ứng dụng mã nguồn mở và miễn phí để sử dụng. Bạn có thể sử dụng, sao chép, sửa đổi và phân phối lại ứng dụng theo các điều khoản của giấy phép mở.

Để biết thêm thông tin về các điều khoản và điều kiện, vui lòng xem tệp LICENSE trong mã nguồn của ứng dụng.

## Phiên Bản

Phiên bản hiện tại: 1.0.0