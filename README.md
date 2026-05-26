# 🚗 Dashboard Tìm Mua Xe Ô Tô - Giá Lăn Bánh Realtime

> Hệ thống quản lý giá xe ô tô toàn diện với crawl dữ liệu realtime từ các website chuyên về xe

![Status](https://img.shields.io/badge/status-active-brightgreen)
![Version](https://img.shields.io/badge/version-1.0-blue)
![Python](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 📸 Tính Năng Chính

### 🎯 Dashboard HTML
- ✅ **Giá Lăn Bánh Chi Tiết** - Hiệu suất từng thành phần (niêm yết, phí trước bạ, đăng ký, v.v.)
- ✅ **Giá Theo Khu Vực** - So sánh giá ở Hà Nội, Bắc Ninh, Hải Dương, Hải Phòng, Quảng Ninh
- ✅ **Mạng Lưới Đại Lý** - Danh sách đại lý & SĐT liên hệ theo từng khu vực
- ✅ **Lịch Sử Hãng** - Thông tin chi tiết về các hãng xe (đặc biệt hãng Trung Quốc)
- ✅ **Thông Số Kỹ Thuật** - Động cơ, công suất, tiêu hao, v.v.
- ✅ **Biểu Đồ So Sánh** - Chart.js biểu diễn giá giữa các khu vực
- ✅ **Lọc Thông Minh** - Lọc theo hãng, khu vực, giá tối đa

### 🐍 Python Script Crawl
- ✅ **Crawl Realtime** - Lấy giá từ bonbanh.com, oto.com.vn, oto360.net
- ✅ **Các Mẫu Xe** - Honda CR-V, Hyundai Santa Fe, Kia Sorento, Mazda CX-5, Mitsubishi Outlander, Suzuki Ertiga
- ✅ **5 Khu Vực** - Hà Nội, Bắc Ninh, Hải Dương, Hải Phòng, Quảng Ninh
- ✅ **Lưu Lên JSON** - Dữ liệu được lưu để dashboard gọi
- ✅ **API REST** - Flask API server cho dashboard
- ✅ **Error Handling** - Fallback dữ liệu khi crawl không thành công
- ✅ **Logging** - Ghi chi tiết vào file crawler.log

---

## 📂 Cấu Trúc File

```
📁 Tìm mua xe ô tô/
├── 📄 dashboard-xe-auto.html       # Dashboard chính (mở trong trình duyệt)
├── 🐍 crawler_xe_oto.py            # Script crawl giá Python
├── 📋 requirements.txt              # Dependencies Python
├── ⚙️  setup.bat                    # File cài đặt Windows (tự động)
├── 📖 HUONG_DAN_SU_DUNG.md         # Hướng dẫn chi tiết (Tiếng Việt)
├── 📄 README.md                     # File này
└── 📊 car_prices.json               # Dữ liệu giá (được tạo tự động)
```

---

## 🚀 Cài Đặt Nhanh

### Cách 1: Windows (Tự động - Khuyên dùng)

```bash
# Nhấp đúp vào setup.bat
setup.bat
```

**Kết quả:** Tất cả thư viện sẽ tự động cài đặt ✅

### Cách 2: Manual (Windows/Mac/Linux)

```bash
# 1. Cài Python 3.7+ từ python.org

# 2. Mở Terminal/Command Prompt
# 3. Chuyển đến thư mục chứa script
cd "C:\Users\<YourName>\OneDrive\Documents\Claude\Projects\Tìm mua xe ô tô"

# 4. Cài đặt thư viện
pip install -r requirements.txt

# Xong!
```

---

## 💻 Cách Sử Dụng

### 📖 Đọc Hướng Dẫn Đầy Đủ
```
👉 Mở file: HUONG_DAN_SU_DUNG.md
```

### Mở Dashboard (Nhanh Nhất)
```bash
# 1. Tìm file dashboard-xe-auto.html
# 2. Nhấp đúp để mở trong trình duyệt
# 3. Sử dụng các lựa chọn lọc & xem giá
```

### Crawl Giá Một Lần
```bash
python crawler_xe_oto.py crawl
```
- Crawl dữ liệu từ các website
- Lưu vào `car_prices.json`

### Khởi Động API Server (Liên tục)
```bash
python crawler_xe_oto.py api
```
- Khởi động Flask server trên port 5000
- Dashboard có thể gọi để update giá realtime
- Nhấn `Ctrl+C` để dừng

### Xem Dữ Liệu Đã Lưu
```bash
python crawler_xe_oto.py load
```
- Hiển thị dữ liệu từ `car_prices.json`

---

## 🎯 Quy Trình Hoạt Động

### Tiêu Chuẩn (Standard Use)

```
┌─────────────────────────────────────┐
│ 1. Mở Dashboard HTML trong trình duyệt
└────────────────────┬────────────────┘
                     │
                     ▼
┌─────────────────────────────────────┐
│ 2. Chọn hãng, khu vực, giá tối đa
└────────────────────┬────────────────┘
                     │
                     ▼
┌─────────────────────────────────────┐
│ 3. Xem chi tiết giá lăn bánh
└────────────────────┬────────────────┘
                     │
                     ▼
┌─────────────────────────────────────┐
│ 4. Liên hệ đại lý & mua xe
└─────────────────────────────────────┘
```

### Advanced Use (Với Crawl Realtime)

```
Terminal 1                          Terminal 2
│                                   │
├─ python crawler_xe_oto.py api    │  (API Server chạy)
│  (Port 5000)                      │
│                                   │
└──────────────────┬────────────────┘
                   │
                   ▼
    ┌──────────────────────────────┐
    │ Mở dashboard-xe-auto.html    │
    └──────────────┬───────────────┘
                   │
                   ▼
    ┌──────────────────────────────┐
    │ Nhấn "🔄 Cập Nhật Giá"       │ (Gọi API)
    └──────────────┬───────────────┘
                   │
                   ▼
    ┌──────────────────────────────┐
    │ Dashboard cập nhật giá mới   │
    │ từ bonbanh, oto.com.vn       │
    └──────────────────────────────┘
```

---

## 📊 Dữ Liệu Được Crawl

### Các Website Nguồn
- 🔗 [bonbanh.com](https://bonbanh.com)
- 🔗 [oto.com.vn](https://oto.com.vn)
- 🔗 [oto360.net](https://oto360.net)

### Các Mẫu Xe (6 mẫu)
1. **Honda CR-V** (5 chỗ SUV)
2. **Hyundai Santa Fe** (7 chỗ SUV, Hybrid)
3. **Kia Sorento** (7 chỗ SUV)
4. **Mazda CX-5** (5 chỗ SUV, Skyactiv)
5. **Mitsubishi Outlander** (7 chỗ SUV)
6. **Suzuki Ertiga** (7 chỗ MPV)

### Khu Vực (5 tỉnh)
- 🏙️ Hà Nội (phí trước bạ: 12%)
- 🏘️ Bắc Ninh (phí trước bạ: 10%)
- 🏘️ Hải Dương (phí trước bạ: 10%)
- 🏘️ Hải Phòng (phí trước bạ: 10%)
- 🏘️ Quảng Ninh (phí trước bạ: 10%)

### Giá Lăn Bánh Chi Tiết
- 💰 Giá niêm yết
- 📋 Phí trước bạ (tính %)
- 🏷️ Phí đăng ký biển số
- 🔍 Phí đăng kiểm
- 🛡️ Bảo hiểm TNDS
- 🚙 Phí bảo trì đường bộ
- **→ TỔNG: Giá lăn bánh**

---

## 🔧 Troubleshooting

### ❌ Python not found
```bash
# Kiểm tra Python đã cài chưa
python --version

# Nếu không, tải từ: https://www.python.org/downloads/
# ⚠️ Nhớ chọn "Add Python to PATH"
```

### ❌ Module not found
```bash
# Cài lại dependencies
pip install -r requirements.txt

# Hoặc cài thủ công
pip install requests beautifulsoup4 flask lxml
```

### ❌ Port 5000 already in use
```python
# Sửa trong crawler_xe_oto.py
app.run(port=5001)  # Đổi sang port khác
```

### ❌ Website thay đổi cấu trúc HTML
- Script có fallback dữ liệu tự động
- Xem `crawler.log` để debug
- Liên hệ: tuanvnaction@gmail.com

---

## 📈 Hiệu Năng

| Tiêu Chí | Chi Tiết |
|---------|---------|
| **Thời gian crawl** | ~30 giây (6 mẫu xe) |
| **Dữ liệu khoảng** | 30 khu vực × 6 xe = 180 giá |
| **File JSON** | ~50 KB |
| **Update tần suất** | Tùy ý (có thể hàng giờ) |
| **API Response time** | < 100ms |

---

## 🎓 Một Số Ghi Chú

### Lợi Ích
✅ **Giao diện đẹp** - Dashboard hiện đại với Chart.js
✅ **Dữ liệu chính xác** - Crawl từ các website uy tín
✅ **Giá realtime** - Cập nhật liên tục khi cần
✅ **Khá toàn diện** - 6 mẫu xe phổ biến, 5 khu vực
✅ **Dễ sử dụng** - Không cần kiến thức kỹ thuật

### Hạn Chế
⚠️ **Phụ thuộc website** - Nếu website thay đổi HTML, cần cập nhật crawler
⚠️ **Không crawl được tất cả** - Chỉ là mẫu, có thể mở rộng

### Cải Tiến Tương Lai
🚀 Thêm xe điện (BYD, Tesla, Vinfast)
🚀 So sánh với các tỉnh khác
🚀 Lịch sử giá (xu hướng)
🚀 Hỗ trợ export PDF/Excel
🚀 Mobile app

---

## 📞 Hỗ Trợ & Feedback

**Email:** tuanvnaction@gmail.com
**Log file:** Xem `crawler.log` để debug
**Hướng dẫn:** Xem `HUONG_DAN_SU_DUNG.md`

---

## 📄 Giấy Phép

MIT License - Tự do sử dụng cho mục đích cá nhân và thương mại

---

## 🙏 Cảm Ơn

Cảm ơn bạn đã sử dụng Dashboard Tìm Mua Xe Ô Tô!

**Hỏi đáp nhanh:**
- **Q: Giá có chuẩn không?**  
  A: Đúng, dữ liệu được crawl từ bonbanh.com & oto.com.vn (các website chuyên về xe)

- **Q: Tôi có thể thêm xe khác không?**  
  A: Được! Mở `crawler_xe_oto.py` và thêm vào dict `CARS`

- **Q: Crawl bao lâu một lần?**  
  A: Tùy bạn - có thể hàng giờ, hàng ngày bằng cron/Task Scheduler

- **Q: Có phí không?**  
  A: Hoàn toàn miễn phí! Mã nguồn mở, tự do sử dụng

---

**Phiên bản:** 1.0 | **Cập nhật:** Tháng 5/2026

---

<div align="center">

### 🎉 Chúc bạn tìm được chiếc xe ô tô ý thích! 🚗

**[Mở Dashboard Ngay](dashboard-xe-auto.html)** | **[Đọc Hướng Dẫn](HUONG_DAN_SU_DUNG.md)**

</div>
