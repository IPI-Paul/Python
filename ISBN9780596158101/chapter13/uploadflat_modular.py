#!/usr/bin/env python3

# Example 13-13
# Refactors the upload program. It is now noticeably simpler, and the code it 
# shares with the download script only needs to be changed in one place if it
# ever requires improvement
# Author: Mark Lutz
# Last modified: 

"""
################################################################################
use FTP to upload all files from a local dir to a remote site/directory;
this ersion reuses downloader's functions, to avoid code redundancy; 
################################################################################
"""

import os
from downloadflat_modular import configTransfer, connectFtp, isTextKind

def cleanRemotes(cf, connection):
    """
    try to delete all remote files first to remove garbage
    """
    if cf.cleanall:
        for remotename in connection.nlst():            # remote dir listing
            try:                                        # remote file delete
                print('Deleting remote', remotename)    # skips . and .. exc
                connection.delete(remotename)
            except:
                print('Cannot delete remote', remotename)

def uploadAll(cf, connection):
    """
    upload all files to remote site/dir per cf config
    listdir() strips dir path, any failure ends script
    """
    localfiles = os.listdir(cf.localdir)            # listdir is local listing
    for localname in localfiles:
        localpath = os.path.join(cf.localdir, localname)
        print('Uploading', localpath, 'to', localname, 'as', end=' ')
        if isTextKind(localname):
            # use text mode xfer
            localfile = open(localpath, 'rb')
            connection.storlines('STOR ' + localname, localfile)
        else:
            # use binary mode xfer
            localfile = open(localpath, 'rb')
            connection.storbinary('STOR ' + localname, localfile)
        localfile.close()
    connection.quit()
    print('Done:', len(localfiles), 'files uploaded.')

if __name__ == '__main__':
    cf = configTransfer(site='localhost')
    conn = connectFtp(cf)
    cleanRemotes(cf, conn)
    uploadAll(cf, conn)