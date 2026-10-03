echo off

echo Flashing Bootloader...
particle flash --local photon-bootloader@3.3.1+lto.bin

echo "Manually put Photon into DFU Mode."
echo "To do this, press both buttons, then release the bottom button until it is blinking yellow."
set /p DUMMY="Press Enter when ready to continue..."

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

echo ''
echo 'To complete your HackerPet setup'
echo '1) Go to https://setup.particle.io to finish setting up your photon and add it to your particle account.'
echo '2) Then flash the HackerPet_Plus firmware at https://build.particle.io/libs/hackerpet_plus'
echo '3) Finally go to your cleverpet hub dashboard at http://cleverpet.local'
echo "Note: Be sure to set your time zone, and enable daylight savings time if applicable. <- This may actually affect the hub's ability to reliably stay online"
