# HackerPet_Setup

HackerPet_Setup is a command-line tool that sets up the Particle Photon in a CleverPet Hub over USB. It:

- checks that the Particle CLI is installed and logs you in to your particle.io account
- detects the Photon connected over USB and updates its Device OS when needed
- configures the Hub's Wi-Fi
- claims the Hub to your particle.io account and lets you (re)name it
- offers to open the Particle Console, the HackerPet_Plus library in the Particle Web IDE, and http://cleverpet.local in your browser

## Requirements

- A particle.io account
- [Particle CLI](https://docs.particle.io/getting-started/developer-tools/cli/)
- [Python 3](https://www.python.org/downloads/)
- A micro USB cable to connect the Hub's Photon to your computer
- A 2.4 GHz Wi-Fi network

## Setup

1. Download the latest `HackerPet_Setup_v<version>.zip` from the Assets of the [Releases page](https://github.com/CleverPet/HackerPet_Setup/releases).
2. Extract the zip to any location on your computer where you have full write permissions. Make note of that location.
3. Download and install the Particle CLI. Follow the instructions at https://docs.particle.io/getting-started/developer-tools/cli/.
4. Download and install Python 3 from https://www.python.org/downloads/.
   On Windows, check the box **Add python.exe to PATH** at the bottom of the first screen of the installer.
5. Plug the Hub's Photon into your computer with the micro USB cable and run the setup:
   - Windows: open the Command Prompt, go to the folder you extracted, and run `HackerPet_Setup.bat`:

     ```bat
     cd path\to\HackerPet_Setup
     HackerPet_Setup.bat
     ```

   - macOS or Linux: open a terminal, go to the folder you extracted, and run `HackerPet_Setup.py`:

     ```sh
     cd path/to/HackerPet_Setup
     python3 HackerPet_Setup.py
     ```

The Wi-Fi network name and password you enter during setup are saved in `wifiCred.json` in the setup folder.

## Troubleshooting

- **No Hub Photons found**: plug in the Hub's Photon with a micro USB cable and run the setup again.
- **Photon failed to enter Wi-Fi setup**: unplug the USB cable, plug it back in, and press Enter to try again.
- **http://cleverpet.local does not load**: look up the Hub's IP address in your router and open that IP address instead.

Any issues, email support@clever.pet

Brian

## API documentation

[HackerPet.com_API.md](HackerPet.com_API.md) is a copy of the HackerPet API documentation from HackerPet.com.

## To Do

- Flash the latest HackerPet firmware from the web in the command line
  - Detect the type of Particle board: Photon, P1, Photon 2, etc.
- Allow setting up the Photon without a Particle account
  - Update Device OS
  - Configure Wi-Fi
  - Flash the HackerPet firmware
