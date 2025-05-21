echo off
rem particle serial list
rem particle usb list

@REM set /p DUMMY=Put into DFU Mode...

echo Flashing part 1...
timeout /t 5
particle flash --usb photon-system-part1@3.3.1.bin

echo Flashing part 2...
timeout /t 5
particle flash --usb photon-system-part2@3.3.1.bin

set /p DUMMY=Exit DFU Mode...
echo Flashing Bootloader...
rem particle usb dfu
particle flash --usb photon-bootloader@3.3.1+lto.bin

echo Flashing Tinker...
timeout /t 5
particle usb dfu
particle flash --usb photon-tinker@3.3.1.bin

echo Flashing Hackerpet...
timeout /t 5
particle usb dfu
particle flash --usb HackerPet_Plus_0.1.114.bin

echo waiting 5 seconds...
timeout /t 5
particle identify
@REM particle serial monitor