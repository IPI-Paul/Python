#!/usr/bin/env python3

# Example 13-15
# Is just a customization of the FtpTools class. It adds a method for recursive 
# uploads
# Author: Mark Lutz
# Last modified: 

"""
################################################################################
extend the FtpTools class to upload all files and subdirectories from a local 
dir tree to a remote site/dir; supports nested dirs too, but not the cleanall 
option (that resquires parsing FTP listings to detect remote dirs: see 
cleanall.py); to upload subdirectories, uses os.path.isdir(path) to see if a 
local file is really a directory, FTP().mkd(path) to make dirs on the remote 
machine (wrapped in a try in case it already exists there), and recursion to 
upload all files/dirs inside the nested subdirectory.
################################################################################
"""

import os, ftptools

class UploadAll(ftptools.FtpTools):
    """
    upload an entire tree of subdirectories
    assumes top remote directory exists
    """
    def __init__(self):
        self.fcount = self.dcount =0
    
    def getcleanall(self):
        return False    # don't even ask
    
    def uploadDir(self, localdir):
        """
        for each directory in an entire tree upload simple files, recur into 
        subdirectories
        """
        localfiles = os.listdir(localdir)
        for localname in localfiles:
            localpath = os.path.join(localdir, localname)
            print('Uploading', localpath, 'to', localname, end=' ')
            if not os.path.isdir(localpath):
                self.uploadOne(localname, localpath, localname)
                self.fcount += 1
            else:
                try:
                    self.connection.mkd(localname)
                    print('Directory created')
                except:
                    print('Directory not created')
                self.connection.cwd(localname)          # change remote dir
                self.uploadDir(localpath)               # upload local subdir
                self.connection.cwd('..')               # change back up
                self.dcount += 1
                print('Directory exited')

if __name__ == '__main__':
    import sys
    ftp = UploadAll()
    rsite = (len(sys.argv) > 1 and sys.argv[1]) or 'localhost'
    rdir = (len(sys.argv) > 2 and sys.argv[2]) or '.'
    ftp.configTransfer(site=rsite, rdir=rdir)
    ftp.localdir = (len(sys.argv) > 3 and sys.argv[3]) or '.'
    ftp.run(transferAct=lambda:ftp.uploadDir(ftp.localdir))
    print('Done:', ftp.fcount, 'files and', ftp.dcount, 'directories uploaded.')