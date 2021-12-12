#!/usr/bin/env python3

# Example by IPI-Paul. 
# Backs up a program at run time to avoid loss or coruption of the file being run
# Author: Paul I Ighofose
# Last modified: 2018-11-07

"""
Backup utility to be added to Python scripts to backup script before running. 
Safeguards script that may be overwritten
"""

import os, sys

def backup(fullPath, silent=False):
    filePath, fileName, tempPath, tempFile = fileDetails(fullPath)
    if not os.path.exists(tempFile) or not sameFile(fullPath, tempFile):
        if silent or input('Do you want to back this file up first? ').upper() == 'Y':
            open(tempFile, 'wb').write(open(fullPath, 'rb').read())
    return 'Backed up ' + tempFile
        
def confirmDelete(fullPath, tempFile):
    msg = '' if sameFile(fullPath, tempFile) else 'Files differ!\n'
    msg += 'Do you want to delete the backup? '
    return msg

def fileDetails(fullpath):
    filePath = fullpath.split(os.sep)[0]
    fileName = fullpath.split(os.sep)[-1]
    tempPath = os.path.join(__file__.split(os.sep)[0], '../sourceFiles/temp')
    tempFile = os.path.join(tempPath, fileName)
    return (filePath, fileName, tempPath, tempFile)

def removeBackup(fullPath, silent=False):
    filePath, fileName, tempPath, tempFile = fileDetails(fullPath)
    if os.path.exists(tempFile):
        if silent or input(confirmDelete(fullPath, tempFile)).upper() == 'Y':
            os.remove(tempFile)
    return 'Removed ' + tempFile

def restoreBackup(fullPath):
    filePath, fileName, tempPath, tempFile = fileDetails(fullPath)
    if os.path.exists(tempFile):
        currFile = os.path.join(filePath, fileName)
        open(currFile, 'wb').write(open(tempFile, 'rb').read())
        return 'Restored ' + currFile
    return 'File not backed up!'

def runtimeBackup(action, fullpath):
    from subprocess import Popen, PIPE
    """
    ipi = os.getcwd().split(os.sep)[:-1] + ['ipi']
    ipi = ''.join(ipi[i] + os.sep for i in range(len(ipi)))
    backup = os.path.join(ipi,'runtime_backup.py')
    """
    backup = __file__
    pypath = sys.executable
    if action == 'b':
        command = '"%s" "%s" -b "%s"' % (pypath, backup, fullpath) # sys.argv[0]
        print('Do you want to backup this script before running: ')
        Popen(command, stderr=PIPE, stdout=PIPE, shell=True).communicate()
    elif action == 'r':    
        print()
        command = '"%s" "%s" -r "%s"' % (pypath, backup, fullpath) # sys.argv[0]
        _, _, _, tempFile = fileDetails(fullpath)
        print(confirmDelete(fullpath, tempFile))
        Popen(command, stdout=PIPE, shell=True).communicate()

def sameFile(fullPath, tempFile):
    return open(tempFile, 'rb').read() == open(fullPath, 'rb').read()

if __name__ == '__main__':      
    if len(sys.argv) == 1:
        backup(sys.argv[0])
        removeBackup(sys.argv[0])
    elif sys.argv[1] == '-b':
        backup(sys.argv[2])
    elif sys.argv[1] == '-r':
        removeBackup(sys.argv[2])
        