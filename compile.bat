@echo off
REM Requires PyInstaller. pip install pyinstaller
rmdir /S /Q dist
rmdir /S /Q build
py -m PyInstaller --onefile HackerPet_Setup.py

:: Prompt the user with "Do you want to continue? (Y/N)"
set /p choice=Would you like to run the HackerPet_Setup.exe? (y/n)

:: Validate the user's response
if /i "%choice%"=="y" (
    :: If Y, execute some code here...
    dist\HackerPet_Setup.exe
) else if /i "%choice%"=="n" (
    :: If N, exit or perform another action...
    echo Compile completed
    goto :eof
)

:eof