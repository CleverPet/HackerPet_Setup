echo off

echo Flashing Bootloader...
particle flash --local photon-bootloader@3.3.1+lto.bin

set /p DUMMY="Put Photon into DFU Mode, \npress both buttons, and release the bottom until blinking yellow.\nPress Enter to continue..."
echo Flashing part 1...
timeout /t 5
particle flash --usb photon-system-part1@3.3.1.bin

echo Flashing part 2...
timeout /t 5
particle flash --usb photon-system-part2@3.3.1.bin

echo Flashing Tinker...
timeout /t 5
particle usb dfu
particle flash --local photon-tinker@3.3.1.bin

echo Flashing Hackerpet...
timeout /t 5
particle usb dfu
particle flash --local HackerPet_Plus_0.1.114.bin

echo waiting 5 seconds...
timeout /t 5
particle identify
