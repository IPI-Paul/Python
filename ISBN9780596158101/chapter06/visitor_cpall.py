#!/usr/bin/env python3

# Example 6-22
# Simply replaces the 'from' directory path string with the 'to' directory path 
# string, at the front of all directory names and pathnames passed in from os.walk.
# The results of the string replacements are the paths to which the original 
# files and directories are to be copied.
# Author: Mark Lutz, Paul I Ighofose
# Last modified: 2018-11-12

"""
Use: 'python ...\Tools\visitor_cpall.py fromDir toDir trace?'
Like Sytem\Filetools\cpall.py, but with the visitor classes and os.walk; does 
string replacement of fromDir with toDir at the front of all the names that the 
walker passes in; assumes that the toDir does not exist initially;
"""

import os 
from visitor import FileVisitor, errors             # visitor is in '.'
# PP4E is in a dir on path (packages not working as should do in Python 3.x
from cpall import copyfile

class CpallVisitor(FileVisitor):
    
    def __init__(self, fromDir, toDir, trace=True, err={}):
        self.fromDirLen = len(fromDir) + 1
        self.toDir = toDir
        self.err = err
        FileVisitor.__init__(self, trace=trace, err=err)
    
    def visitdir(self, dirpath):
        try:
            toPath = os.path.join(self.toDir, dirpath[self.fromDirLen:])
            if not os.path.exists(toPath): 
                if self.trace: print('d', dirpath, '=>', toPath)
                os.mkdir(toPath)
                self.dcount += 1
            else:
                if self.trace: print('%s already exisits' % 
                                     dirpath[self.fromDirLen:])
        except Exception as e:
            self.err = errors(self.err, dirpath, e, sys.exc_info()[-1])
    
    def visitfile(self, filepath):
        try:
            toPath = os.path.join(self.toDir, filepath[self.fromDirLen:])
            if not self.exists(filepath, toPath):
                if self.trace: print('f', filepath, '=>', toPath)
                copyfile(filepath, toPath)
                self.fcount += 1
            else:
                if self.trace: 
                    print('%s already exisits' % \
                          (os.path.join(toPath.split(os.sep)[-2],
                                        toPath.split(os.sep)[-1])))
        except Exception as e:
            self.err = errors(self.err, filepath, e, sys.exc_info()[-1])
    
    def exists(self, filepath, topath):
        if os.path.isfile(topath) == True:
            return open(filepath, 'rb').readlines() == open(topath, 
                                                            'rb').readlines()
        return False

if __name__ == '__main__':
    err = {}
    use = """
Usage: visitor_cpall.py fromDir toDir trace   
    """
    import sys, time
    try:
        fromDir, toDir = sys.argv[1:3]
        winreg = '\\'
        cygreg = os.sep
        if not (winreg in fromDir or cygreg in fromDir):
            fromDir = fromDir.replace('"', '').replace("'", '')
            fromDir = os.path.abspath(os.path.join(os.getcwd(), fromDir))
        if not(fromDir[:1] == '/' or fromDir[1:2] == ':'):
            fromDir = fromDir.replace('"', '').replace("'", '')
            fromDir = os.path.abspath(os.path.join(os.getcwd(), fromDir))
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
            trace = len(sys.argv) > 3
            print('Copying...')
            start = time.clock()
            walker = CpallVisitor(fromDir, toDir, trace, err=err)
            walker.run(startDir=fromDir)
            print('Copied', walker.fcount, 'files,', walker.dcount, 'directories', 
                  end=' ')
            print('in', time.clock() - start, 'seconds')
    except ValueError as e:
        err = errors(err, 'main', e, sys.exc_info()[-1])
    except Exception as e:
        err = errors(walker.err, 'CpallVisitor', e, sys.exc_info()[-1])

    print()
    for x in err:
        print(x + ': ' + err[x])
    if 'main' in err or 'CpallVisitor' in err: 
        print(use)                