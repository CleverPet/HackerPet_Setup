#!/usr/bin/env bash
#
# Update a Photon (default) or P1 to Device OS and HackerPet_Plus firmware over USB.
#
# Usage:
#   ./update.sh        flash a Photon
#   ./update.sh p1     flash a P1
#
# Reference commands:
#   particle usb list
#   particle serial list

set -euo pipefail

DEVICE_OS_VERSION="3.3.1"
HACKERPET_VERSION="0.1.114"

cd "$(dirname "$0")"

PLATFORM="${1:-photon}"

case "$PLATFORM" in
	photon)
		FIRMWARE_FILES=(
			"photon-bootloader@${DEVICE_OS_VERSION}+lto.bin"
			"photon-system-part1@${DEVICE_OS_VERSION}.bin"
			"photon-system-part2@${DEVICE_OS_VERSION}.bin"
			"HackerPet_Plus_${HACKERPET_VERSION}.bin"
		)
		;;
	p1)
		# No P1 build of HackerPet_Plus is bundled (p1/p1-HackerPet_Plus_*.bin is a
		# Photon build), so flash Tinker as a known-good application instead.
		FIRMWARE_FILES=(
			"p1/p1-bootloader@${DEVICE_OS_VERSION}+lto.bin"
			"p1/p1-system-part1@${DEVICE_OS_VERSION}.bin"
			"p1/p1-system-part2@${DEVICE_OS_VERSION}.bin"
			"p1/p1-tinker@${DEVICE_OS_VERSION}.bin"
		)
		;;
	*)
		echo "Unknown platform: $PLATFORM" >&2
		echo "Usage: $0 [photon|p1]" >&2
		exit 1
		;;
esac

for f in "${FIRMWARE_FILES[@]}"; do
	if [ ! -f "$f" ]; then
		echo "Missing firmware file: $f" >&2
		exit 1
	fi
done

echo "Updating $PLATFORM to Device OS $DEVICE_OS_VERSION."
echo
echo "Put the device into DFU mode: hold both buttons, release RESET, keep holding"
echo "SETUP until the LED blinks yellow, then release SETUP."
echo "This is required for devices running Device OS older than 2.0.0."
read -r -p "Press Enter when the LED is blinking yellow..."

echo "Flashing bootloader, Device OS and application..."
if ! particle flash --local "${FIRMWARE_FILES[@]}"; then
	echo "Flash failed. The device was not fully updated; fix the error above and run this script again." >&2
	exit 1
fi

echo "Waiting for the device to restart..."
sleep 5
if ! particle identify; then
	echo "Warning: could not read the device ID. The flash completed; run 'particle identify' manually if you need the ID."
fi

echo
echo "To complete your HackerPet setup:"
echo "1) Go to https://setup.particle.io to finish setting up your device and add it to your Particle account."
if [ "$PLATFORM" = "p1" ]; then
	echo "2) Flash the HackerPet_Plus firmware for P1 at https://build.particle.io/libs/hackerpet_plus"
	echo "   (this script installed Tinker; no P1 build of HackerPet_Plus is bundled)."
else
	echo "2) HackerPet_Plus $HACKERPET_VERSION is now installed. Optional: to update to a newer"
	echo "   version later, flash it from https://build.particle.io/libs/hackerpet_plus"
fi
echo "3) Go to your CleverPet hub dashboard at http://cleverpet.local"
echo
echo "Note: Set your time zone and DST setting; an incorrect setting can cause connectivity problems."
