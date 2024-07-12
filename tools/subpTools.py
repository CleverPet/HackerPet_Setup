#! /usr/bin/python3
import subprocess, io

def PopenResultStream( result, verbose = True, output = True ) -> list:
    CLEAR = '\x1b[2K'
    outputList = []
    for line in io.TextIOWrapper( result, encoding="utf-8"):
        saveLine = line.rstrip()
        outputList.append( saveLine )
        if verbose == True:
            print( saveLine )
    if output == True:
        # print(f'#################### outputing list...: {outputList}')
        return outputList

######## Interactive cmd
# p = subprocess.Popen(['your_command'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
def interactive( commandList: list ):
    p = subprocess.Popen( commandList, stdin=subprocess.PIPE, stdout=subprocess.PIPE )

    output, _ = p.communicate()
    while True:
        line = input('Enter your response: ')
        if not line:
            break
        p.stdin.write( line.encode() )

def open( commandList: list, verbose = False, output = True, shellOption = False  ) -> list:
    CLEAR = '\x1b[2K'
    result = subprocess.Popen( commandList, shell=shellOption, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True )
    outputList = []
    # Prints and replaces each line as subprocess outputs info.
    outputList = PopenResultStream( result.stdout, verbose = verbose, output = output  )
    return outputList