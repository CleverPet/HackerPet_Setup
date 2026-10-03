#! /bin/bash

# Reference commands
# particle serial list
# particle usb list

sleep 2
echo Flashing Bootloader...
particle flash --local photon-bootloader@3.3.1+lto.bin

echo "Manually put Photon into DFU Mode."
echo "To do this, press both buttons, then release the bottom button until it is blinking yellow."
read -p "Press Enter when ready to continue..."
# flash Part 1

echo Flashing part 1...
particle flash --usb photon-system-part1@3.3.1.bin

# flash Part 2
sleep 2
echo Flashing part 2...
particle flash --usb photon-system-part2@3.3.1.bin

# Flash Tinker
sleep 2
echo entering dfu mode...
particle usb dfu
echo Flashing Tinker...
particle flash --local photon-tinker@3.3.1.bin

# Flash HackerPet
sleep 2
echo entering dfu mode...
particle usb dfu
echo Flashing Hackerpet...
particle flash --local HackerPet_Plus_0.1.114.bin

echo waiting 2 seconds...
sleep 2
particle identify
# particle serial monitor

echo ''
echo 'To complete your HackerPet setup'
echo '1) Go to https://setup.particle.io to finish setting up your photon and add it to your particle account.'
echo '2) Then flash the HackerPet_Plus firmware at https://build.particle.io/libs/hackerpet_plus'
echo '3) Finally go to your cleverpet hub dashboard at http://cleverpet.local'
echo "Note: Be sure to set your time zone, and enable daylight savings time if applicable. <- This may actually affect the hub's ability to reliably stay online"
