#! /usr/bin/python3
import subprocess, io, os, shlex, shutil, threading

def PopenResultStream( result, verbose = True, output = True ) -> list:
    CLEAR = '\x1b[2K'
    outputList = []
    # Drain stderr on a separate thread while stdout is streamed, so a child
    # that fills the stderr pipe cannot block forever. Output order is kept:
    # stdout lines first, then stderr lines.
    errLines = []
    def readStderr():
        for line in io.TextIOWrapper( result.stderr, encoding="utf-8", errors="replace" ):
            errLines.append( line.rstrip() )
    errThread = threading.Thread( target=readStderr, daemon=True )
    errThread.start()
    for line in io.TextIOWrapper( result.stdout, encoding="utf-8", errors="replace" ):
        saveLine = line.rstrip()
        outputList.append( saveLine )
        if verbose == True:
            print( saveLine )
    errThread.join()
    for saveLine in errLines:
        outputList.append( saveLine )
        if verbose == True:
            print( saveLine )
    result.wait()
    if output == True:
        # print(f'#################### outputing list...: {outputList}')
        return outputList

def resolveCommand( commandList ):
    # Resolve the executable through PATH (and PATHEXT on Windows), so that
    # 'particle' finds particle.cmd (npm install) or particle.exe (Particle
    # installer) without needing a shell.
    if isinstance( commandList, str ) or not commandList:
        return commandList
    executable = shutil.which( commandList[0] )
    if executable is None:
        return list( commandList )
    return [executable] + list( commandList[1:] )

######## Interactive cmd
# p = subprocess.Popen(['your_command'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
def interactive( commandList: list ):
    p = subprocess.Popen( resolveCommand( commandList ), stdin=subprocess.PIPE, stdout=subprocess.PIPE )

    output, _ = p.communicate()
    while True:
        line = input('Enter your response: ')
        if not line:
            break
        p.stdin.write( line.encode() )

def open( commandList: list, verbose = False, output = True, shellOption = False  ) -> list:
    CLEAR = '\x1b[2K'
    if shellOption:
        # With shell=True on macOS/Linux only the first list item is run as the
        # command, so join the list into one properly quoted command string.
        if os.name != 'nt' and not isinstance( commandList, str ):
            commandList = shlex.join( commandList )
    else:
        commandList = resolveCommand( commandList )
    try:
        result = subprocess.Popen( commandList, shell=shellOption, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True )
    except FileNotFoundError:
        name = commandList if isinstance( commandList, str ) else commandList[0]
        message = f'{name}: command not found'
        if verbose == True:
            print( message )
        return [message] if output == True else None
    outputList = []
    # Prints and replaces each line as subprocess outputs info.
    outputList = PopenResultStream( result, verbose = verbose, output = output  )
    return outputList
