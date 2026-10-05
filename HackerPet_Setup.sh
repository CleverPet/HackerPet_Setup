#!/bin/bash

cd "$(dirname "$0")" || exit 1
python3 HackerPet_Setup.py
read -n 1 -s -p "Press any key to continue..."