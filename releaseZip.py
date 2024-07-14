#!/usr/bin/python
# Zip files for release

# Exclude list
# build
# dist
# .gitignore
# Releases
# *.spec
# *.git
# compile.bat
# if windows exclude *.sh
# releaseZip.py

# Inlcude list
# HackerPet_Setup.py
# HackerPet_Setup.bat
# ReadMe.md
# tools

import zipfile, os, sys, shutil
from pathlib import Path
from HackerPet_Setup import version as Version

# Path.lstat
version = Version
releaseLocation = 'Releases'
fileName = 'HackerPet_Setup'
zipFileName = f'{releaseLocation}/{fileName}_v{version}.zip'
zipFileName_versionless = f'{releaseLocation}/{fileName}.zip'

if Path(zipFileName).exists():
    os.remove(zipFileName)
opperatingSystem = sys.platform
systemList = ['.bat', '.sh']
if opperatingSystem == 'win32':
    systemList.pop(0)
# excludeList = ['build', 'dist', '.gitignore', 'Releases', '.spec', '.git', 'compile.bat', 'releaseZip.py', '.zip', '__pycache__']
excludeList = ['build', 'dist', '.gitignore', 'Releases', '.spec', '.git', 'releaseZip.py', '__pycache__']

excludeList.extend(systemList)

indexToRemove = []

def walk_dir():
    directory = str(Path.cwd())
    fileList = []
    for root, dirs, files in os.walk(directory):
        # print(f'root == {root}')

        level = root.replace(f'{directory}', '')
        if len(level) >= 1:
            if level[0] == '\\':
                level = level[1:]
        # print(f'level == {level}')

        # level = root.replace(directory, '').count(os.sep)
        # indent = '---' * (level)
        # print(f"{root}")
        for file in files:
            seperator = '\\'
            if level == '':
                seperator = ''
            fileList.append(f"{level}{seperator}{file}")
            # print(f"{root}\{file}")
    return fileList

# walk_dir('/path/to/directory')

# def listAllFiles():
#     root_dir = Path.cwd()
#     for root, dirs, files in os.walk( root_dir ):
#         for file in files:
#             print(files)
#             # file_path = os.path.join(root, file)
#     # print(file_path)

fileList = walk_dir()

for eachExclusion in excludeList:
    for i, eachFileFolder in enumerate(fileList):
        if eachExclusion in eachFileFolder:
            indexToRemove.append( i )
indexToRemove = sorted(indexToRemove, reverse = True )

for eachIndex in indexToRemove:
    fileList.pop(eachIndex)

# for eachFile in fileList:
#     print(eachFile)

with zipfile.ZipFile( zipFileName, 'w') as z:
    for file in fileList:
        # input(file)
        z.write( file )

shutil.copy( zipFileName, zipFileName_versionless)
# openedZip = zipfile.ZipFile( fileList, 'w')
# openedZip.write( zipFileName )
# # with open( zipFileName, 'w' ) as f:
# #     f.write( zipFileName, )