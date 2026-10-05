1) Download the HackerPet_Setup.Zip
https://github.com/CleverPet/HackerPet_Setup/releases

2) Extract the zip to any location you have full write permissions on your PC
Make note of that location.

3) Download and install Particle CLI - Link and instructions below
https://docs.particle.io/getting-started/developer-tools/cli/

4) Download and install Python 3 - Link below. 
Also make sure to check the box for [X] "add python.exe to PATH" 
( check box at the bottom of first screen of installer )
https://www.python.org/downloads/

5) For windows open the cmd prompt
Navigate to where you extracted the folder
Run the HackerPet_Setup.bat

or for mac or linux run 
python HackerPet_Setup.py

Any issues, email support@clever.pet

-- Updating Device OS on older devices (DeviceOSFirmware) --
DeviceOSFirmware/update.bat (Windows) and DeviceOSFirmware/update.sh (macOS/Linux)
update an older Photon to Device OS 3.3.1 and flash HackerPet_Plus 0.1.114 over USB.
Use this when the device is not detected by USB or by HackerPet_Setup.

Prerequisites
 - Particle CLI installed (see step 3 above) and logged in: run "particle login"
 - Device connected to the computer by a USB data cable

How to run
 - Windows: open the cmd prompt, go to the DeviceOSFirmware folder, run
     update.bat
 - macOS/Linux: open a terminal, go to the DeviceOSFirmware folder, run
     ./update.sh
 - When asked, put the device into DFU mode (LED blinking yellow): hold both
   buttons, release RESET, keep holding SETUP until the LED blinks yellow,
   then release SETUP. Press Enter to start flashing.
 - The script stops with "Flash failed" if any step fails. Fix the error
   shown and run the script again.

P1 option
 - The scripts flash a Photon by default. For a P1, add "p1":
     update.bat p1
     ./update.sh p1
 - The P1 option flashes Device OS 3.3.1 and Tinker from DeviceOSFirmware/p1.
   No P1 build of HackerPet_Plus is included, so flash HackerPet_Plus for P1
   afterwards from https://build.particle.io/libs/hackerpet_plus

Brian

-- To Do --
 - Flash the latest HackerPet firmware from the web in the command line
   - detect type of Particle board, photon, p1, photon 2, etc...
   
 - Allow setting up the photon without a particle account.
    - update Device OS
    - configure wifi
    - flash the HackerPet firmware