# 🚗 Hướng Dẫn Sử Dụng Dashboard Xe Ô Tô & Script Crawl Giá

## 📋 Danh Sách File

```
├── dashboard-xe-auto.html          # Dashboard hiển thị giá (mở trong trình duyệt)
├── crawler_xe_oto.py               # Script crawl giá realtime từ các website
├── car_prices.json                 # File lưu trữ giá (được tạo tự động)
├── requirements.txt                # Danh sách thư viện Python cần cài đặt
└── HUONG_DAN_SU_DUNG.md           # File này
```

---

## 🎯 **PHẦN 1: DASHBOARD (HTML)**

### Cách Sử Dụng Dashboard

#### **Bước 1: Mở Dashboard**
1. Tìm file `dashboard-xe-auto.html` trong folder
2. Nhấp đúp để mở trong trình duyệt (hoặc kích phải → Open with → Browser)
3. Dashboard sẽ hiển thị

#### **Bước 2: Giao Diện Dashboard**

Dashboard bao gồm:

**Top Bar (Thanh điều khiển):**
- 🏢 **Hãng xe** - Lọc theo Honda, Hyundai, Kia, Mazda, Mitsubishi, Suzuki
- 📍 **Khu vực** - Lọc theo Hà Nội, Bắc Ninh, Hải Dương, Hải Phòng, Quảng Ninh
- 💰 **Giá** - Lọc theo ngân sách tối đa (slider)
- 🔄 **Cập Nhật Giá** - Nút để tải giá mới từ internet

**Left Column:**
- 📋 **Danh Sách Xe** - Hiển thị danh sách xe phù hợp với bộ lọc
- 📊 **Biểu Đồ So Sánh** - Biểu đồ so sánh giá giữa các khu vực

**Right Column:**
- 💳 **Chi Tiết Giá Lăn Bánh** - Phân tích từng thành phần giá
- 🏪 **Mạng Lưới Đại Lý** - Danh sách đại lý ở các khu vực
- 🏭 **Lịch Sử Hãng** - Thông tin về hãng xe & thông số kỹ thuật

#### **Bước 3: Sử Dụng Các Tính Năng**

**Lọc Xe:**
```
1. Chọn hãng xe: dropdown "🏢 Hãng xe"
2. Chọn khu vực: dropdown "📍 Khu vực"
3. Điều chỉnh giá tối đa: kéo slider "💰 Giá"
→ Danh sách xe tự động cập nhật
```

**Xem Chi Tiết Xe:**
```
1. Nhấp vào xe bất kỳ trong "📋 Danh Sách Xe"
2. Thông tin chi tiết sẽ hiển thị ở cột phải:
   - 💳 Giá lăn bánh chi tiết (từng thành phần)
   - 🏪 Danh sách đại lý & SĐT liên hệ
   - 🏭 Lịch sử hãng & thông số kỹ thuật
   - 📊 Biểu đồ so sánh giá
```

**Cập Nhật Giá Realtime:**
```
1. Nhấn nút "🔄 Cập Nhật Giá"
2. Script sẽ tìm kiếm giá mới từ internet
3. Kết quả sẽ cập nhật tự động
4. Thời gian cập nhật cuối cùng hiển thị ở footer
```

---

## 🐍 **PHẦN 2: SCRIPT PYTHON CRAWL GIÁ**

### Yêu Cầu Hệ Thống

- **Python 3.7+** (tải từ python.org)
- **Windows/Mac/Linux**

### Cài Đặt

#### **Bước 1: Cài Đặt Python & pip**

**Windows:**
1. Tải Python từ https://www.python.org/downloads/
2. Cài đặt (chọn "Add Python to PATH")
3. Mở Command Prompt (cmd)

**Mac/Linux:**
```bash
# Kiểm tra Python đã cài chưa
python3 --version

# Cài pip (nếu chưa có)
sudo apt install python3-pip  # Linux
brew install python3          # Mac
```

#### **Bước 2: Cài Đặt Thư Viện**

```bash
# Mở Command Prompt/Terminal
# Chuyển đến thư mục chứa script

cd "C:\Users\doant\OneDrive\Documents\Claude\Projects\Tìm mua xe ô tô"

# Cài đặt các thư viện cần thiết
pip install -r requirements.txt
```

**Output thành công:**
```
Successfully installed requests-2.31.0 beautifulsoup4-4.12.2 flask-3.0.0
```

### Sử Dụng Script

#### **Cách 1: Crawl Giá & Lưu vào File**

```bash
python crawler_xe_oto.py crawl
```

**Kết quả:**
- Crawl giá từ bonbanh.com, oto.com.vn
- Lưu dữ liệu vào `car_prices.json`
- Hiển thị log chi tiết trên màn hình

#### **Cách 2: Xem Giá Đã Lưu**

```bash
python crawler_xe_oto.py load
```

**Kết quả:**
- Hiển thị giá từ file `car_prices.json`
- Format JSON dễ đọc

#### **Cách 3: Khởi Động API Server (Advanced)**

```bash
python crawler_xe_oto.py api
```

**Kết quả:**
```
Starting API server on http://localhost:5000
```

API endpoints:
- `GET /api/prices` - Lấy giá hiện tại
- `POST /api/update` - Cập nhật giá (crawl)
- `GET /api/status` - Kiểm tra trạng thái

---

## 🔧 **PHẦN 3: KẾT NỐI DASHBOARD + SCRIPT**

### Cách Tích Hợp (Full Automation)

#### **Phương Pháp 1: JavaScript + Python (Tự động)**

1. **Chuẩn bị:**
   - Đảm bảo script Python đang chạy API server:
   ```bash
   python crawler_xe_oto.py api
   ```
   
2. **Mở Dashboard:**
   - Mở `dashboard-xe-auto.html` trong trình duyệt
   - Nhấn nút "🔄 Cập Nhật Giá"
   - Dashboard sẽ tự động kết nối đến API Python

3. **Kết Quả:**
   - Giá cập nhật realtime từ internet
   - Log chi tiết trong API server

#### **Phương Pháp 2: Scheduled (Chạy định kỳ)**

**Windows - Task Scheduler:**
1. Mở Task Scheduler
2. Tạo task mới
3. Đặt chạy: `python crawler_xe_oto.py crawl`
4. Đặt lịch: Hàng ngày lúc 6:00 AM

**Mac/Linux - Cron:**
```bash
# Mở crontab
crontab -e

# Thêm dòng: Chạy mỗi sáng lúc 6:00
0 6 * * * cd /path/to/script && python crawler_xe_oto.py crawl
```

---

## 📊 **PHẦN 4: CẤU TRÚC FILE JSON**

### Format car_prices.json

```json
{
  "data": {
    "Honda CR-V": {
      "brand": "Honda",
      "type": "5 chỗ SUV",
      "prices": {
        "Hà Nội": 1165000000,
        "Bắc Ninh": 1160000000,
        "Hải Dương": 1155000000,
        "Hải Phòng": 1150000000,
        "Quảng Ninh": 1145000000
      },
      "crawled_at": "2026-05-26T10:30:45.123456"
    },
    "Hyundai Santa Fe": {
      ...
    }
  },
  "updated_at": "2026-05-26T10:30:45.123456",
  "region_count": 5,
  "car_count": 6
}
```

---

## 🚀 **PHẦN 5: TROUBLESHOOTING**

### Vấn Đề 1: Script Không Kết Nối Internet

**Nguyên nhân:**
- Tường lửa (Firewall) chặn
- Website không phản hồi
- Timeout quá ngắn

**Giải pháp:**
```python
# Sửa timeout trong script
response = self.session.get(url, timeout=30)  # Tăng từ 10 lên 30
```

### Vấn Đề 2: Dashboard Không Kết Nối API Server

**Nguyên nhân:**
- API server chưa khởi động
- Port 5000 bị chiếm

**Giải pháp:**
```bash
# Kiểm tra API đang chạy
netstat -tuln | grep 5000  # Linux/Mac
netstat -ano | findstr :5000  # Windows

# Nếu port 5000 bị chiếm, thay đổi trong script
app.run(port=5001)  # Thay port 5000 thành 5001
```

### Vấn Đề 3: Giá Không Cập Nhật

**Nguyên nhân:**
- Website bonbanh.com có cấu trúc HTML khác
- Phí trước bạ thay đổi

**Giải pháp:**
1. Kiểm tra file `crawler.log`
2. Cập nhật giá mặc định trong hàm `get_fallback_prices()`
3. Liên hệ admin để cập nhật crawler

### Vấn Đề 4: Flask Not Found

**Nguyên nhân:**
- Thư viện Flask chưa cài

**Giải pháp:**
```bash
pip install flask==3.0.0
```

---

## 📞 **LIÊN HỆ HỖ TRỢ**

- **Email:** tuanvnaction@gmail.com
- **Log file:** Xem `crawler.log` để debug
- **Update hàng tuần:** Script sẽ tự động fallback nếu website thay đổi

---

## 🎓 **TIP & TRICK**

### 1. Tắt CORS (Nếu Cần)

Nếu dashboard không kết nối được API vì CORS:
```python
from flask_cors import CORS
CORS(app)
```

### 2. Caching (Tiết Kiệm Bandwidth)

```python
# Chỉ crawl 1 lần/6 giờ
import time
last_update = 0
if time.time() - last_update > 21600:  # 6 giờ
    crawler.run()
```

### 3. Thêm Proxy (Nếu Bị Chặn)

```python
proxies = {
    'http': 'http://proxy.example.com:8080',
    'https': 'http://proxy.example.com:8080'
}
response = self.session.get(url, proxies=proxies)
```

---

## 📈 **LỢI ÍCH CỦA HỆ THỐNG**

✅ **Giá Realtime** - Cập nhật từ các website chuyên về xe
✅ **Giá Chi Tiết** - Hiểu từng thành phần giá lăn bánh
✅ **So Sánh Khu Vực** - Biết xe nào rẻ hơn ở đâu
✅ **Thông Tin Đại Lý** - Liên hệ trực tiếp, SĐT sẵn
✅ **Lịch Sử Hãng** - Hiểu rõ nguồn gốc hãng
✅ **Thông Số Xe** - Thông tin kỹ thuật đầy đủ

---

**Bản cập nhật cuối cùng: Tháng 5/2026**
**Phiên bản: 1.0**
