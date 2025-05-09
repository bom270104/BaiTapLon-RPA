# 📰 Crawl dữ liệu website - Kenh14.vn (Xã Hội)

Dự án này tự động thu thập tin tức từ chuyên mục **Xã hội** của trang Kenh14.vn. Dữ liệu gồm: tiêu đề, mô tả, hình ảnh, và nội dung chi tiết của bài viết, được lưu lại dưới dạng file Excel.

## 📌 Tính năng chính

- Thu thập các bài viết mới từ https://kenh14.vn/xa-hoi.chn
- Trích xuất tiêu đề, mô tả, hình ảnh và nội dung.
- Lưu trữ dữ liệu vào file Excel (`output_kenh14.xlsx`)
- Tự động chạy hàng ngày vào lúc 06:00 sáng (có thể thay đổi).

---

## ⚙️ Yêu cầu hệ thống

- Python >= 3.7
- Trình duyệt Chrome
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) phù hợp với phiên bản Chrome

---

## 🧩 Cài đặt

### 1. Clone project

```bash
git clone git@github.com:bom270104/BaiTapLon-RPA.git
cd web-crawler-kenh14

```

### ✅ 2. Cài đặt các thư viện cần thiết

Cài đặt lần lượt các thư viện sau bằng lệnh `pip`:

- 📦 **requests**:  
  `pip install requests`

- 🍜 **beautifulsoup4**:  
  `pip install beautifulsoup4`

- 📊 **pandas**:  
  `pip install pandas`

- ⏰ **schedule**:  
  `pip install schedule`

- 🌐 **selenium**:  
  `pip install selenium`

- 📘 **openpyxl** _(để lưu file Excel)_:  
  `pip install openpyxl`

### 3. Chạy project với lệnh sau

```bash
python BaiTapLon.py
```
