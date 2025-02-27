@echo off
echo Compiling Colin's Launcher...
g++ -o colins_launcher.exe main.cpp
if %errorlevel% neq 0 (
    echo Compilation failed!
    pause
    exit /b %errorlevel%
)
echo Compilation successful!
pause