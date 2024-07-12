#! /usr/bin/python

# this should be renamed to something like console or cli controls.
import os
esc = '\033['
# close = '['
def clearScreen():
    clearCommand = 'clear'
    if os.name == 'nt':
        global esc
        # esc = '^<ESC^>['
        # esc = '['
        clearCommand = 'cls'
    os.system( clearCommand )

Black = '\033[30m'
Gray = '\033[90m'
Green = '\033[92m'
Red = '\033[91m'
Blue = '\033[94m'
DarkMagenta = '\033[35m'
Yellow = '\033[33m'
BYellow = '\033[93m'

End = '\033[0m'
Up = '\033[F'  # cursor up one line
Clear = '\033[K'  # clears to the end of the line
# UP = '\033[1A'  # this was in the download function
# CLEAR = '\x1b[2K' # this was in the download function


'''
echo [101;93m STYLES [0m
echo ^<ESC^>[0m [0mReset[0m
echo ^<ESC^>[1m [1mBold[0m
echo ^<ESC^>[4m [4mUnderline[0m
echo ^<ESC^>[7m [7mInverse[0m
echo.
echo [101;93m NORMAL FOREGROUND COLORS [0m
echo ^<ESC^>[30m [30mBlack[0m (black)
echo ^<ESC^>[31m [31mRed[0m
echo ^<ESC^>[32m [32mGreen[0m
echo ^<ESC^>[33m [33mYellow[0m
echo ^<ESC^>[34m [34mBlue[0m
echo ^<ESC^>[35m [35mMagenta[0m
echo ^<ESC^>[36m [36mCyan[0m
echo ^<ESC^>[37m [37mWhite[0m
echo.
echo [101;93m NORMAL BACKGROUND COLORS [0m
echo ^<ESC^>[40m [40mBlack[0m
echo ^<ESC^>[41m [41mRed[0m
echo ^<ESC^>[42m [42mGreen[0m
echo ^<ESC^>[43m [43mYellow[0m
echo ^<ESC^>[44m [44mBlue[0m
echo ^<ESC^>[45m [45mMagenta[0m
echo ^<ESC^>[46m [46mCyan[0m
echo ^<ESC^>[47m [47mWhite[0m (white)
echo.
echo [101;93m STRONG FOREGROUND COLORS [0m
echo ^<ESC^>[90m [90mWhite[0m
echo ^<ESC^>[91m [91mRed[0m
echo ^<ESC^>[92m [92mGreen[0m
echo ^<ESC^>[93m [93mYellow[0m
echo ^<ESC^>[94m [94mBlue[0m
echo ^<ESC^>[95m [95mMagenta[0m
echo ^<ESC^>[96m [96mCyan[0m
echo ^<ESC^>[97m [97mWhite[0m
echo.
echo [101;93m STRONG BACKGROUND COLORS [0m
echo ^<ESC^>[100m [100mBlack[0m
echo ^<ESC^>[101m [101mRed[0m
echo ^<ESC^>[102m [102mGreen[0m
echo ^<ESC^>[103m [103mYellow[0m
echo ^<ESC^>[104m [104mBlue[0m
echo ^<ESC^>[105m [105mMagenta[0m
echo ^<ESC^>[106m [106mCyan[0m
echo ^<ESC^>[107m [107mWhite[0m
echo.
echo [101;93m COMBINATIONS [0m
echo ^<ESC^>[31m                     [31mred foreground color[0m
echo ^<ESC^>[7m                      [7minverse foreground ^<-^> background[0m
echo ^<ESC^>[7;31m                   [7;31minverse red foreground color[0m
echo ^<ESC^>[7m and nested ^<ESC^>[31m [7mbefore [31mnested[0m
echo ^<ESC^>[31m and nested ^<ESC^>[7m [31mbefore [7mnested[0m

This is a color: 0 - default
This is a color: 1 - Bold
This is a color: 2 - normal?
This is a color: 3 - Italic
This is a color: 4 - Underline
This is a color: 5 
This is a color: 6
This is a color: 7 - hilite
This is a color: 8 - blank
This is a color: 9 - strikeout

This is a color: 30 - Gray
This is a color: 31 - Orange/Red
This is a color: 32 - LightGreen
This is a color: 33 - LightYellow
This is a color: 34 - LightBlue
This is a color: 35 - LightMagenta
This is a color: 36 - LightCyan

This is a color: 40
This is a color: 41 - bgLightRed
This is a color: 42 - bgLightGreen
This is a color: 43 - bgLightYellow
This is a color: 44 - bgLightBlue
This is a color: 45 - bgLightMagenta
This is a color: 46 - bgLightCyan
This is a color: 47 - bgLightWhite

This is a color: 90 - Gray
This is a color: 91 - Red
This is a color: 92 - Green
This is a color: 93 - Yellow
This is a color: 94 - Blue
This is a color: 95 - Magenta
This is a color: 96 - Cyan

This is a color: 100 - bgGray
This is a color: 101 - bgRed
This is a color: 102 - bgGreen
This is a color: 103 - bgYellow
This is a color: 104 - bgBlue
This is a color: 105 - bgMagenta
This is a color: 106 - bgCyan
This is a color: 107 - bgWhite

'''