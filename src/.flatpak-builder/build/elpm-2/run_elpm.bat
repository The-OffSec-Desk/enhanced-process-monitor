@echo off
REM ELPM Launcher Script for Windows
REM This script helps run ELPM with proper environment setup

echo ==========================================
echo   ELPM - Enhanced Linux Process Monitor
echo ==========================================
echo.

REM Check Python version
echo Checking Python installation...
python --version >nul 2>&1
if %errorlevel% equ 0 (
    set PYTHON_CMD=python
    echo Python found: 
    python --version
) else (
    echo Python not found. Please install Python 3.8 or higher.
    pause
    exit /b 1
)

REM Check PyQt6
echo.
echo Checking PyQt6...
%PYTHON_CMD% -c "import PyQt6" >nul 2>&1
if %errorlevel% equ 0 (
    echo ✓ PyQt6 is installed
) else (
    echo ✗ PyQt6 not found
    echo.
    echo Installing PyQt6...
    %PYTHON_CMD% -m pip install PyQt6
    
    if %errorlevel% equ 0 (
        echo ✓ PyQt6 installed successfully
    ) else (
        echo ✗ Failed to install PyQt6
        echo Please run: pip install PyQt6
        pause
        exit /b 1
    )
)

REM Check psutil
echo.
echo Checking psutil...
%PYTHON_CMD% -c "import psutil" >nul 2>&1
if %errorlevel% equ 0 (
    echo ✓ psutil is installed
) else (
    echo ✗ psutil not found
    echo.
    echo Installing psutil...
    %PYTHON_CMD% -m pip install psutil
    
    if %errorlevel% equ 0 (
        echo ✓ psutil installed successfully
    ) else (
        echo ✗ Failed to install psutil
        echo Please run: pip install psutil
        pause
        exit /b 1
    )
)

REM Run the application
echo.
echo Starting ELPM...
echo.
%PYTHON_CMD% elpm_main.py

REM If it failed, suggest diagnostics
if %errorlevel% neq 0 (
    echo.
    echo ✗ Application failed to start
    echo Run diagnostics: python diagnose.py
    pause
)