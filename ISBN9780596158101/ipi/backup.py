#!/usr/bin/env python3

# Example by IPI-Paul.
# A utility program that can be added to other programs to back them up before 
# running and protect again loss of those programs through corruption or human
# error.
# Author: Paul I Ighofose
# Last modified: 2018-11-22

"""
Backup utility to be added to Python scripts to backup script before running. 
Safeguards script that may be overwritten
"""

import os, sys

class Backup:
    
    def __init__(self, fromDir='.', toDir='archive', ext=['.pyc'], err={}):
        self.fromDir = fromDir.replace('"', '').replace("'", '')
        self.toDir = toDir.replace('"', '').replace("'", '')
        self.err = err
        self.count = 0
        self.ext = ext

    def copyFile(self, file, toFile):
        try:
            if not self.exists(file, toFile) and not os.path.splitext(file) in \
               self.ext:
                open(toFile, 'wb').write(open(file, 'rb').read())
                self.count += 1
        except Exception as e:
            self.err = errors(self.err, file, e, sys.exc_info()[-1])
    
    def exists(self, filepath, topath):
        if os.path.isfile(topath) == True:
            return open(filepath, 'rb').readlines() == open(topath, 
                                                            'rb').readlines()
        return False

    def makeDir(self, path):
        try:
            if not os.path.exists(path): 
                os.mkdir(path)
        except Exception as e:
            self.err = errors(self.err, path, e, sys.exc_info()[-1])

    def run(self):
        for path, subdirs, files in os.walk(self.fromDir):
            toPath = path.replace(self.fromDir, self.toDir)
            self.makeDir(toPath)
            for file in files:
                toFile = os.path.join(toPath, file)
                self.copyFile(os.path.join(path, file), toFile)
        return self.count
    
def errors(err, caller, errType, func):
    from traceback import extract_tb
    errName = type(errType).__name__ 
    erm = '\nFailed due to '
    if errName == 'IndexError': 
        erm += 'a missing command-line parameter'  
    elif errName == 'UnicodeDecodeError': 
        erm = '\n' + erm + 'unable to decode and read file'       
    else: 
        erm += errName + ' ' + str(errType) 
    function = extract_tb(func, 1)[0]
    erm += '\nOn line no. %s when calling:\n%s' % (function[1], function[3])
    if caller in err:
        err[caller] += erm
    else:
        err[caller] = erm
    return err

if __name__ == '__main__':
    err = {}
    ipi = __file__.split(os.sep)[:-1] 
    ipi = os.path.abspath(''.join(ipi[i] + os.sep for i in range(len(ipi))))    
    ipi += os.sep if '/' in ipi else '\\'
    use = 'Your current location is: ' + ipi + """
Usage: backup.py fromDir toDir 
   optional (default excludes: '.pyc')
       backup.py fromDir toDir [extensions (in quotes if ending with *)]
    """
    try:
        fromDir, toDir = sys.argv[1:3]
        ext = sys.argv[3:] if len(sys.argv) > 3 else ['.pyc']            
        winreg = '\\'
        cygreg = os.sep
        if not (winreg in fromDir or cygreg in fromDir):
            fromDir = fromDir.replace('"', '').replace("'", '')
            fromDir = os.path.abspath(os.path.join(ipi, fromDir))
        if not(fromDir[:1] == '/' or fromDir[1:2] == ':'):
            fromDir = fromDir.replace('"', '').replace("'", '')
            fromDir = os.path.abspath(os.path.join(ipi, fromDir))
        if not(toDir[:1] == '/' or toDir[1:2] == ':'):
            toDir = toDir.replace('"', '').replace("'", '')
            toDir = os.path.abspath(os.path.join(fromDir, toDir))
        run = True
        if not(fromDir[:1] == '/' or fromDir[1:3] == ':\\'): 
            print('Error! Surround path names containing \\ with quotes:\n%s' % 
                  fromDir)
            run = False
        if not(toDir[:1] == '/' or toDir[1:3] == ':\\'):
            print('Error! Surround path names containing \\ with quotes:\n%s' % 
                  toDir)
            run = False
        if run == True:
            print('Started backup from:\n%s\n%s' % (fromDir, toDir))            
            backup = Backup(fromDir, toDir, ext=ext, err=err)
            count = backup.run()
            print('Backup completed with %d new file%s!' % (count, 
                                                            's' if count > 1 
                                                            else ''), end=' ')
    except ValueError as e:
        err = errors(err, 'main', e, sys.exc_info()[-1])
    except Exception as e:
        err = errors(backup.err, 'Backup', e, sys.exc_info()[-1])

    print()
    for x in err:
        print(x + ': ' + err[x])
    if 'main' in err or 'Backup' in err: 
        print(use)                        