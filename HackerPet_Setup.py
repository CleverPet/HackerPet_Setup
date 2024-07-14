#! /usr/bin/python
version = '0.1.2'
# command line executer from library
# import bgcommandThingy
from tools import subpTools
from tools import cursor as c
c.clearScreen()
import getpass, time, re, os
import sys, webbrowser, subprocess, json
from importlib import reload

loggedIN = ''
email = ''
YorN = f'({c.Green}Y{c.End} or {c.Red}N{c.End})'

def exit():
    # print('Press any key to continue.')
    os.system('pause')
    sys.exit()
    

def goodbye( success ):
    if success:
        print(f'Setup {c.Green}Complete{c.End}, {c.Blue}Good bye!{c.End}')
    else:
        print(f'Setup {c.Red}Failed{c.End}, {c.Yellow}Run the setup again to try again.{c.End}')
    exit()

def safeInt( s ):
    newInt = 0
    try:
        newInt = int(s)
    except:
        newInt = -1
    return newInt

def loginSuccesCheck( loggedIN ):
    result = False

    if 'error' in loggedIN[0]:
        for each in loggedIN:
            print(each)

    if 'Failed' in loggedIN[0]:
        print(f'{c.Yellow}You might be offline, check your internet connection and try again.{c.End}')

    if 'Successfully' in loggedIN[0] or '\x1b[2K\x1b[1G>' in loggedIN[0]:
        # print('already logged in')
        result = True
    return result

def particleLogin( skipLogin = False ):
    email = ''
    if skipLogin == False:
        whoamiResults = subpTools.open( ['particle', 'whoami'], shellOption=True )
        # time.sleep(3)
        if loginSuccesCheck( whoamiResults ) == False:
            # something = subprocess.Popen(['particle', 'login'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
            # print(something.communicate()[0])
            skipCheck = input(f'Would you like to login to particle.io? {YorN}:')
            if 'n' in skipCheck:
                return email

            username = input( f'Enter your particle.io Email address: {c.Green}' )
            password = getpass.getpass( f'{c.End}Enter your password:{c.Green}[Input is hidden]{c.End} ' )
            loginResult = subpTools.open( ['particle', 'login', '--username', username, '--password', password], verbose= False )
            # input(f'loginResult == {loginResult}')

            if loginSuccesCheck( loginResult ) == False:
                inputResult = input(f'{c.Red}Login Failed{c.End}, Try again? ({YorN} or "{c.Yellow}S{c.End}" to skip logging in to particl.io:')
                if inputResult.lower() == 'y':
                    particleLogin()
                if inputResult.lower() == 'q' or inputResult == 'n':
                    goodbye( False )
                if inputResult.lower() == 's':
                    return email
        
        loggedIN = subpTools.open( ['particle', 'whoami'] )
        email = loggedIN[0].split(' ')[1]
        # input(email)
    return email

email = particleLogin()

# accountAnswer = input( 'Do you have a particle.io account? (Y or N):' )
# if accountAnswer.lower() != 'y':
#     print('Exiting, particle account required, please go to https://login.particle.io/signup and create a free personal account to continue the setup.')
#     exit()


# if 'are not signed in' in loggedIN[0]:
#     # something = subprocess.Popen(['particle', 'login'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
#     # print(something.communicate()[0])
#     username = input( 'Enter your particle.io username:' )
#     password = input( 'Enter your password:' )
#     subpTools.open( ['particle', 'login', '--username', username, '--password', password], verbose= False )
#     loggedIN = subpTools.open( ['particle', 'whoami'] )
#     email = loggedIN[0].split(' ')[1]

print(f'Welcome {c.Green}{email}{c.End}')

# Deivce in DFU Mode for update
deviceIDs = []
devices = []
# exit()


def returnUSBDevices():
    print('Searching for CleverPet Hub Photon plugged into USB...')
    serialDevices = subpTools.open( ['particle', 'serial', 'list'])
    devices = subpTools.open( ['particle', 'usb','list'] )
    deviceID = ''
    deviceIDs = []
    updateResponse = ''
    # print(f'serialDevices == {serialDevices}')
    # print(f'devices == {devices}')
    serialDevicesFound = safeInt( serialDevices[0].split(' ')[1] )
    if serialDevicesFound == -1:
        print(f'{c.Red}No Hub Photons found, please plugin the Hubs Photon with a micro USB cable and run the setup again.{c.End}')
        updateResponse = input(f'Would you like to continue and update the HackerPet firmware over the web? {YorN}')
        if updateResponse.lower() != 'y':
            goodbye( False )

    if serialDevicesFound != -1:
        if serialDevicesFound != len(devices):
            print(f'{c.Yellow}You need to update the OS on your Hubs Photon, push both Buttons, then release the bottom one until the light flashes Yellow.{c.End}')
            input(f'{c.Green}Press a key to continue...{c.End}')
            print(f'Updating os, please wait and do not unplug your Hubs photon...{c.DarkMagenta}')
            updateResult = subpTools.open( ['particle', 'update'], verbose=True ) 
            print(f'{c.Yellow}{updateResult[-1]}{c.End}')
            print(f'Device OS update complete!  \nIf the above result did not complete succesfully, restart and try again. Otherwise contact {c.Yellow}support@clever.pet{c.End}')

    if updateResponse.lower() != 'y':
        for each in devices:
            deviceID = each.split( '[' )
            # input(f'deviceID == {deviceID}')
            try:
                deviceID = deviceID[1].split( ']' )
                deviceID = deviceID[0]
                print( f'Found Photon: {deviceID}' )
                deviceIDs.append(deviceID)
                if len(deviceID) != 24:
                    input( 'Could not find a device ID' )
            except:
                tryAgainResponse = input( f'No device found connected to your computer. Plug in your Hub and Try again? {YorN}:' )
                if tryAgainResponse.lower() == 'y':
                    returnUSBDevices()
            # else:
            #     exit()
    # print(f'devices == {devices}' )
    return deviceIDs

def returnClaimedDevices() -> list:
    claimedDevices = []
    devices = subpTools.open( ['particle', 'list'] )
    for eachDevice in devices:
        device = {}
        # deviceString = re.sub(r'\x1b[2K\x1b[1G\x1b[2K\x1b', '', eachDevice)
        deviceString = re.sub(r'\x1b\[2K\x1b\[1G', '', eachDevice)

        # input(deviceString)
        deviceString = deviceString.split(' ')
        device['name'] = deviceString[0]
        device['particleID'] = re.sub(r'\[|]', '', deviceString[1] )
        device['type'] = re.sub( r'()', '', deviceString[2] )
        device['status'] = deviceString[4]
        # device = device[0].split('[')
        claimedDevices.append( device )
    return claimedDevices

def printClaimedDevices( claimedDevices_dict ):
    for i, each in enumerate( claimedDevices_dict ):
        print(f"{i}) {each['name']} {each['particleID']} {each['type']} {each['status']}")

def enterListening( ):
    maxAttempts = 3
    attempts = 0
    print('Entering WiFi Setup mode...')
    while attempts < maxAttempts:
        listeningResult = subpTools.open( ['particle', 'usb', 'start-listening'] )
        # input(f'listeningResult == {listeningResult}')
        if 'Something went wrong' in listeningResult[0] or 'timeout' in listeningResult[0]:
            input(f'{c.Yellow}Photon failed to enter Wifi Setup, unplug the USB and plug it back in and hit Enter to try again.{c.End}')
        else:
            attempts = 3
    return
    
def wifiSetup( setupFile = 'wifiCred.json'):
    success = False
    # interactive so shell maybe?
    # dfu mode before wifi setup
    ## Needs work with wifi setup.
    max_attempts = 3
    setupResult = False
    attempts = 0
    while attempts < max_attempts:
        wifiSetupResult = input( f'Would you like to configure or re-configure the wifi on your Hub? {YorN}:' )
        if wifiSetupResult.lower() == 'n':
            attempts = max_attempts
            break
        if wifiSetupResult.lower() == 'y':
            enterListening()
            with open( setupFile, 'r' ) as f:
                wifiCredJson = json.load(f)
            wifiCredJson['network'] = input(f'Enter your 2.4Ghz Netwrok Wifi Name. (ie,"{c.Yellow}My SSID Name!{c.End}"):')
            wifiCredJson['password'] = input(f'Enter your SSID Password: ({c.Yellow}#CaPiTalzM4ttEr!{c.End}):')
            # print( 'Setting up wifi' )
            with open( setupFile, 'w' ) as f:
                json.dump( wifiCredJson, f )
            # subpTools.open( ['particle', 'serial', 'wifi'], shellOption=True, verbose = True )
            setupResult = subpTools.open( ['particle', 'serial', 'wifi', '--file', setupFile], verbose = True )
            if setupResult == []:
                input('Wifi Setup failed, unplug and replug the USB and press enter to try again.')
            else:
                attempts = max_attempts +1
    return setupResult

def particleCLICheck() -> bool:
    reload(subpTools)

    success = False
    results = subpTools.open(['particle', 'help'], verbose = False, output = True)
    # print( results )
    if len(results) > 0:
        if 'welcome' in results[0].lower():
            # particle installed
            print(f'{c.Green}Particle CLI {results[1]}{c.End}')
            success = True
        else:
            print(f'{c.Red}Particle CLI required!{c.End}\n Download and installtion instructions available from link below:\n{c.Green}https://docs.particle.io/getting-started/developer-tools/cli/')
    return success

## Main ####
def claimParticle( deviceID ):
    # claim particle device
    print( 'claiming device...' )
    # input(f' claimedDevices == {claimedDevices}')
    claimedDevices = returnClaimedDevices()
    deviceClaimed = False
    currentDevice = {}
    for eachDevice in claimedDevices:
        if eachDevice['particleID'] == deviceID:
            deviceClaimed = True
            print(f'Device {eachDevice["name"]}: {c.Yellow}{deviceID}{c.End} already {c.Green} claimed!{c.End}')
            currentDevice = eachDevice
    # s = selectedDevice
    if deviceClaimed == False:
        print(c.BYellow )
        claimResults = subpTools.open( ['particle', 'cloud', 'claim', deviceID], shellOption = True, verbose = True )
        # input(f'claimResults == {claimResults}')
        claimedDevices = returnClaimedDevices()
        for each in claimedDevices:
            print(each)
        print(c.End)
    return currentDevice

def main():
    # check see if there's an update and change the color if it's old?
    print(f'{c.DarkMagenta}HackerPet Setup {c.Green}v{version}{c.End}')

    # check for particle install
    if particleCLICheck() == False:
        goodbye( False )

    s = -1
    deviceIDs = returnUSBDevices()
    print(f'({c.Yellow}{len(deviceIDs)}{c.End}) Devices found plugged in.\n')
    # claimedDevices_dict = returnClaimedDevices()

    # only 1 allowed right now
    selectedDevice = 1-1
    devicesPluggedIn = len(deviceIDs)
    if devicesPluggedIn > 1:
        input(f'This setup only allows setting up one Hub at a time, unplug all but one, and press {c.Green}Enter{c.End} key to retry.')
        main()

    # unused at the moment
    wifiSetupResult = ''
    if devicesPluggedIn >= 1:
        # Wifi Setup
        wifiSetupResult = wifiSetup()
        # input(f'wifiSetupResult =={wifiSetupResult}')

    claimedDevice = ''
    if devicesPluggedIn >= 1:
        claimedDevice = claimParticle( deviceIDs[selectedDevice] )


    if claimedDevice != '':
        if selectedDevice >= 0:
            # Name the device
            deviceName = "Fluffy's Arcade Machine"
            if claimedDevice['name']:
                deviceName = claimedDevice['name']

            chosenName = input( f"Would you like (Re)Name your CleverPet Hub? (ie, {c.Yellow}{deviceName}{c.End}, {c.Red}N{c.End} to skip): " )
            # print( chosenName )
            if chosenName.lower() != 'n':
                if chosenName.lower() != '':
                    subpTools.open( ['particle', 'cloud', 'name', deviceIDs[s], chosenName], shellOption = True )
            else:
                print( 'No Name entered, skipping (Re)Name.' )

            # Compile and flash hackerpet_plus firmware.
            # particle library create
            # particle library create --name hackerpet_plus --version 0.1.114 --author CleverPet --dir .
            # particle flash DeviceID


    consoleResult = input(f'Would you like to open the particle Console in your Browser to review your Hub connection status? {c.DarkMagenta}https://console.particle.io/devices{c.End}  {YorN}:')
    if consoleResult.lower() == 'y':
        webbrowser.open( 'https://console.particle.io/devices' )

    HPResult = input(f'Would you like to open {c.DarkMagenta}https://build.particle.io/libs/hackerpet_plus{c.End} and install or update HackerPet_Plus? {YorN}')
    if 'y' in HPResult.lower():
        print(f'{c.Green}HackerPet_Plus Installation Instructions{c.End}:\n              1) Scroll down on the left column to particle-test-local.ino and click on that.\n              2) Then scroll all the down one more time and click on the Blue Button "Use This Example".')
        print('              3) Double check your Hub is selected int the bottom right corner, \n              4) Then click on the lightning bolt in the very top left corner to send the firmware to your Hub.')
        print(f'\n              Once that is complete, just navigate to {c.DarkMagenta}http://cleverpet.local{c.End} with any device on your local network to configure your hub and select a game.')
        webbrowser.open( 'https://build.particle.io/libs/hackerpet_plus' )

    cpLocalAnser = input(f'Would you like to open{c.DarkMagenta} http://cleverpet.local{c.End} To configure your CleverPet Hub?{YorN}')
    if cpLocalAnser.lower() == 'y':
        webbrowser.open( 'http://cleverpet.local' )
        print('If this address does not resolve to a site, check your router for the Hubs IP address and replace cleverpet.local with IP.')
        print(f'If you need additional help, email {c.DarkMagenta}support@clever.pet{c.End} to schedule a 1 on 1 video call to finish the setup.')

    goodbye( True )

if __name__ == '__main__':
    main()
######