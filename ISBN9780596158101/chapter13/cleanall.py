#!/usr/bin/env python3

# Example 13-16
# Gets rid of all files accidentally upload to a remote site. It deletes all 
# files and nested subdirectories in an entire remote tree
# Author: Mark Lutz, Paul I Ighofose
# Last modified: 2019-02-13

"""
################################################################################
extendthe FtpTools class to delete fiels and subdirectories from a remote 
directory tree; supports nested  directories too; depends on the dir() command 
output format, which may vary on some servers! - see Python's 
Tools\Scripts\ftpmirror.py for hints; extend me for remote tree downloads;
################################################################################
"""

from ftptools import FtpTools

class CleanAll(FtpTools):
    """
    delete an entire remote tree of subdirectories
    """
    def __init__(self):
        self.fcount = self.dcount = 0
    
    def getlocaldir(self):
        return None     # irrelevant here
    
    def getcleanall(self):
        return True     # implied here
    
    def cleanDir(self):
        """
        for each item in current remote directory, del simple files, recur into
        and then del subdirectories
        the dir() ftp call passes each line to a func or method
        """
        lines = []                              # each level has own lines
        self.connection.dir(lines.append)       # list current remote dir
        for line in lines:
            parsed = line.split()               # split on whitespace
            permiss = parsed[0]                 # assume 'drw... ... filename'
            fname = parsed[-1]
            if fname in ('.', '..'):            # some include cwd and parent
                continue
            elif permiss[0] != 'd' and 'dir' not in line.lower():  # simple file: delete
                print('Deleting file', fname)
                self.connection.delete(fname)
                self.fcount += 1
            else:                               # directory: recur, del
                print('Directory', fname)
                self.connection.cwd(fname)      # chdir into remote dir
                self.cleanDir()                 # clean subdirectory
                self.connection.cwd('..')       # chdir remote back up 
                self.connection.rmd(fname)      # delete empty remote dir
                self.dcount += 1
                print('Directory exited')

if __name__ == '__main__':
    import sys
    ftp = CleanAll()
    rsite = (len(sys.argv) > 1 and sys.argv[1]) or 'localhost'
    rdir = (len(sys.argv) > 2 and sys.argv[2]) or '.'
    ftp.configTransfer(site=rsite, rdir=rdir)
    ftp.run(cleanTarget=ftp.cleanDir)
    print('Done:', ftp.fcount, 'files and', ftp.dcount, 'directories cleaned.')