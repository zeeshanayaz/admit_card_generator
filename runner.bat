@echo off
cd /d "%~dp0"

echo ========================================
echo   Admit Card Genertor
echo ========================================
echo.

if not exist "venv\Scripts\python.exe" (
    echo Creating virtual environment...
    python -m venv venv
)

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo Installing required packages...
python -m pip install -r requirements.txt

echo.
echo Starting Admit Card generator...
python app.py

pause