@echo off
setlocal

rem Update a Photon (default) or P1 to Device OS and HackerPet_Plus firmware over USB.
rem
rem Usage:
rem   update.bat        flash a Photon
rem   update.bat p1     flash a P1

set DEVICE_OS_VERSION=3.3.1
set HACKERPET_VERSION=0.1.114

cd /d "%~dp0"

rem No P1 build of HackerPet_Plus is bundled: p1\p1-HackerPet_Plus_*.bin is a
rem Photon build. For P1, Tinker is flashed as a known-good application instead.
set PLATFORM=photon
if not "%~1"=="" set PLATFORM=%~1

if /i "%PLATFORM%"=="photon" (
    set FIRMWARE_FILES=photon-bootloader@%DEVICE_OS_VERSION%+lto.bin photon-system-part1@%DEVICE_OS_VERSION%.bin photon-system-part2@%DEVICE_OS_VERSION%.bin HackerPet_Plus_%HACKERPET_VERSION%.bin
) else if /i "%PLATFORM%"=="p1" (
    set FIRMWARE_FILES=p1\p1-bootloader@%DEVICE_OS_VERSION%+lto.bin p1\p1-system-part1@%DEVICE_OS_VERSION%.bin p1\p1-system-part2@%DEVICE_OS_VERSION%.bin p1\p1-tinker@%DEVICE_OS_VERSION%.bin
) else (
    echo Unknown platform: %PLATFORM%
    echo Usage: update.bat [photon^|p1]
    pause
    exit /b 1
)

for %%F in (%FIRMWARE_FILES%) do (
    if not exist "%%F" (
        echo Missing firmware file: %%F
        pause
        exit /b 1
    )
)

echo Updating %PLATFORM% to Device OS %DEVICE_OS_VERSION%.
echo.
echo Put the device into DFU mode: hold both buttons, release RESET, keep holding
echo SETUP until the LED blinks yellow, then release SETUP.
echo This is required for devices running Device OS older than 2.0.0.
set /p DUMMY=Press Enter when the LED is blinking yellow...

echo Flashing bootloader, Device OS and application...
call particle flash --local %FIRMWARE_FILES%
if errorlevel 1 (
    echo Flash failed. The device was not fully updated; fix the error above and run this script again.
    pause
    exit /b 1
)

echo Waiting for the device to restart...
timeout /t 5 /nobreak >nul
call particle identify
if errorlevel 1 (
    echo Warning: could not read the device ID. The flash completed; run "particle identify" manually if you need the ID.
)

echo.
echo To complete your HackerPet setup:
echo 1^) Go to https://setup.particle.io to finish setting up your device and add it to your Particle account.
if /i "%PLATFORM%"=="p1" (
    echo 2^) Flash the HackerPet_Plus firmware for P1 at https://build.particle.io/libs/hackerpet_plus
    echo    ^(this script installed Tinker; no P1 build of HackerPet_Plus is bundled^).
) else (
    echo 2^) HackerPet_Plus %HACKERPET_VERSION% is now installed. Optional: to update to a newer
    echo    version later, flash it from https://build.particle.io/libs/hackerpet_plus
)
echo 3^) Go to your CleverPet hub dashboard at http://cleverpet.local
echo.
echo Note: Set your time zone and DST setting; an incorrect setting can cause connectivity problems.
pause
