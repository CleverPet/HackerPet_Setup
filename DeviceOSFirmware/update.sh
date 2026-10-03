#! /bin/bash

# Reference commands
# particle serial list
# particle usb list

sleep 2
echo Flashing Bootloader...
particle flash --local photon-bootloader-3.3.1+lto.bin
read -p "Put Photon into DFU Mode, \npress both buttons, and release the bottom until blinking yellow.\nPress Enter to continue..."
# flash Part 1

echo Flashing part 1...
particle flash --usb photon-system-part1-3.3.1.bin

# flash Part 2
sleep 2
echo Flashing part 2...
particle flash --usb photon-system-part2-3.3.1.bin

# Flash Tinker
sleep 2
echo entering dfu mode...
particle usb dfu
echo Flashing Tinker...
particle flash --local photon-tinker-3.3.1.bin

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
