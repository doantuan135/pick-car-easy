@echo off
chcp 65001 >nul
REM -*- coding: utf-8 -*-
REM Script cài đặt tự động cho Dashboard Xe Ô Tô
REM ================================================================

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║        🚗 SETUP DASHBOARD XE Ô TÔ - AUTOMATIC INSTALL 🚗       ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.

REM Kiểm tra Python đã cài chưa
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ LỖI: Python chưa được cài đặt hoặc không trong PATH
    echo.
    echo 📥 Vui lòng cài đặt Python từ: https://www.python.org/downloads/
    echo    ⚠️  Hãy chọn "Add Python to PATH" khi cài đặt
    echo.
    pause
    exit /b 1
)

echo ✅ Python đã được phát hiện
python --version
echo.

REM Kiểm tra pip
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ LỖI: pip chưa được cài đặt
    pause
    exit /b 1
)

echo ✅ pip đã được phát hiện
pip --version
echo.

REM Upgrade pip
echo 🔄 Cập nhật pip...
python -m pip install --upgrade pip --quiet
if %errorlevel% neq 0 (
    echo ⚠️  Cảnh báo: Không thể cập nhật pip
)

echo.
echo 📦 Cài đặt các thư viện cần thiết...
echo.

REM Cài đặt requirements
pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo.
    echo ❌ LỖI: Không thể cài đặt thư viện
    echo 💡 Giải pháp: Mở Command Prompt và chạy:
    echo    pip install requests beautifulsoup4 flask lxml
    echo.
    pause
    exit /b 1
)

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║               ✅ CÀI ĐẶT THÀNH CÔNG!                          ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.

echo 🎯 CÁC BƯỚC TIẾP THEO:
echo.
echo 1️⃣  MỞ DASHBOARD:
echo    📂 Tìm file: dashboard-xe-auto.html
echo    🖱️  Nhấp đúp để mở trong trình duyệt
echo.
echo 2️⃣  CRAWL GIÁ (Option A - Một lần):
echo    ▶️  python crawler_xe_oto.py crawl
echo.
echo 3️⃣  KHỞI ĐỘNG API SERVER (Option B - Liên tục):
echo    ▶️  python crawler_xe_oto.py api
echo    Sau đó nhấn nút "🔄 Cập Nhật Giá" trong Dashboard
echo.
echo 4️⃣  XEM HỖ TRỢ:
echo    📖 Mở file: HUONG_DAN_SU_DUNG.md
echo.

echo ════════════════════════════════════════════════════════════════
echo 💡 MẸO: Tạo shortcut để chạy script
echo    - Kích phải desktop
echo    - Chọn "New" → "Text file"
echo    - Dán nội dung dưới và lưu thành .bat file:
echo.
echo    @echo off
echo    cd /d "%cd%"
echo    python crawler_xe_oto.py api
echo    pause
echo.
echo ════════════════════════════════════════════════════════════════
echo.

REM Tạo shortcut chạy crawler
echo 🎯 Tạo shortcut để chạy API server...
if exist "run_api.bat" (
    echo ⚠️  File run_api.bat đã tồn tại
) else (
    echo @echo off > run_api.bat
    echo cd /d "%cd%" >> run_api.bat
    echo python crawler_xe_oto.py api >> run_api.bat
    echo pause >> run_api.bat
    echo ✅ Tạo file run_api.bat thành công
)

echo.
echo Nhấn ENTER để đóng cửa sổ này...
pause
