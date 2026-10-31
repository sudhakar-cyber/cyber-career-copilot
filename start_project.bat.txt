@echo off
cd /d "%~dp0"
start "Cyber Career Copilot" cmd /k ""%~dp0venv\Scripts\python.exe" "%~dp0app.py""
timeout /t 5 /nobreak >nul
start "" "http://127.0.0.1:5000"
