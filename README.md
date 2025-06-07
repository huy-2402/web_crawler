# Web Crawler
Dự án nhỏ để crawl tiêu đề bài viết từ một trang web và lưu vào file JSON.

## Cài đặt
1. Kích hoạt môi trường ảo:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
2. Cài đặt thư viện: `pip install -r requirements.txt`
3. Chạy chương trình: `python main.py`

## Đầu ra
Dữ liệu được lưu trong thư mục `data/output.json`.

## Mục đích
Mục đích của project
Project này là một web crawler (trình thu thập dữ liệu web), có nhiệm vụ tự động lấy dữ liệu từ các trang web mà bạn chỉ định (URLs).

Công việc chính của project
Gửi yêu cầu (request) tới từng URL
Sử dụng thư viện requests để gửi yêu cầu HTTP tới các địa chỉ web.

Phân tích nội dung HTML của trang web
Dùng BeautifulSoup để đọc và xử lý cấu trúc HTML của trang web vừa tải về.

Trích xuất dữ liệu cần thiết

Lấy tiêu đề trang (ví dụ thẻ <h1> hoặc <h2> đầu tiên)

Lấy đoạn mô tả (ví dụ thẻ <p> đầu tiên)

Lấy tất cả các liên kết (href) trong trang

Lưu trữ dữ liệu
Tổng hợp dữ liệu thu thập được thành một cấu trúc danh sách các dicts (mỗi dict tương ứng một trang), rồi lưu vào file JSON (data/output.json).

Có thể mở rộng
Bạn có thể thêm nhiều URL để crawl nhiều trang hơn, hoặc mở rộng để lấy thêm các thông tin khác theo mục đích.

