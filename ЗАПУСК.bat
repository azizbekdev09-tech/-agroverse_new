@echo off
chcp 65001 >nul
title AgroVerse - Ishga tushirish
cd /d "%~dp0"

echo.
echo ===============================================
echo    AgroVerse - Ishga tushirish / Запуск
echo ===============================================
echo.

REM --- Python qidirish ---
set PYTHON=
where python >nul 2>nul && set PYTHON=python
if "%PYTHON%"=="" (where py >nul 2>nul && set PYTHON=py)
if "%PYTHON%"=="" (
    echo [XATO] Python topilmadi!
    echo https://python.org dan yuklab oling
    echo O'rnatishda "Add Python to PATH" belgisini qo'ying!
    echo.
    pause
    exit /b 1
)
echo [1/4] Python OK: %PYTHON%

REM --- .env tekshirish ---
if not exist "agroverse back\.env" (
    echo.
    echo [DIQQAT] .env fayl topilmadi: "agroverse back\.env"
    echo Quyidagi matnni .env fayliga saqlang:
    echo   DATABASE_URL=postgresql://user:password@localhost:5432/agroverse
    echo   SECRET_KEY=supersecretkey123
    echo PostgreSQL ishlayotganiga ishonch hosil qiling.
    echo.
    pause
)

REM --- Virtual muhit ---
set VENVPY=agroverse back\venv\Scripts\python.exe
if not exist "%VENVPY%" (
    echo [2/4] Virtual muhit yaratilmoqda...
    %PYTHON% -m venv "agroverse back\venv"
    echo       Kutubxonalar o'rnatilmoqda (1-2 daqiqa)...
    "%VENVPY%" -m pip install --upgrade pip -q
    "%VENVPY%" -m pip install -r "agroverse back\requirements.txt" -q
    echo       OK
) else (
    echo [2/4] Virtual muhit allaqachon bor
)

REM --- Backend alohida oynada ---
echo [3/4] Backend ishga tushirilmoqda (port 8000)...
start "AgroVerse BACKEND" cmd /k "cd /d "%~dp0agroverse back" && echo === AgroVerse BACKEND === && echo API: http://127.0.0.1:8000 && echo Bu oynani yopmang! && echo. && "%~dp0agroverse back\venv\Scripts\python.exe" -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload"

echo       Backend ishi kutilmoqda (6 soniya)...
timeout /t 6 /nobreak >nul

REM --- Frontend alohida oynada ---
echo [4/4] Frontend ishga tushirilmoqda (port 5500)...
start "AgroVerse FRONTEND" cmd /k "cd /d "%~dp0agroverse front" && echo === AgroVerse FRONTEND === && echo Sayt: http://127.0.0.1:5500 && echo Bu oynani yopmang! && echo. && "%~dp0agroverse back\venv\Scripts\python.exe" -m http.server 5500"

timeout /t 3 /nobreak >nul

REM --- Brauzer ---
echo.
echo ===============================================
echo    Tayyor! Brauzer ochilmoqda...
echo ===============================================
echo.
echo   Sayt:   http://127.0.0.1:5500
echo   API:    http://127.0.0.1:8000
echo   Docs:   http://127.0.0.1:8000/docs
echo.
echo   BACKEND va FRONTEND oynalarini yopmang!
echo.

timeout /t 2 /nobreak >nul
start http://127.0.0.1:5500

echo Bu oynani yopishingiz mumkin.
pause
