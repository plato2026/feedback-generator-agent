@echo off
REM ═══════════════════════════════════════════════════════════
REM run.bat — Quick Start Script (Windows)
REM ═══════════════════════════════════════════════════════════
REM Usage: double-click run.bat or run from command prompt
REM ═══════════════════════════════════════════════════════════

echo.
echo  Student Feedback Generator Agent
echo ════════════════════════════════════
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is required but not found.
    echo Please install Python 3.10+ from https://python.org
    pause
    exit /b 1
)

REM Create virtual environment if needed
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    echo Virtual environment created.
)

REM Activate
call venv\Scripts\activate.bat

REM Install dependencies
echo Installing dependencies...
pip install -q -r requirements.txt
echo Dependencies installed.

REM Check secrets
if not exist ".streamlit\secrets.toml" (
    echo.
    echo WARNING: No secrets.toml found.
    echo You can enter your API key in the sidebar when the app opens.
    echo.
)

REM Launch
echo.
echo Launching Feedback Generator Agent...
echo Open: http://localhost:8501
echo Press Ctrl+C to stop.
echo.
streamlit run app.py

pause
