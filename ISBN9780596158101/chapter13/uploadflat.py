#!/usr/bin/env python3

# Example 13-11
# Uses FTP to copy all files in a directory on the local machine on which it 
# runs up to a directory on a remote machine
# Author: Mark Lutz, Paul I Ighofose
# Last modified: 2019-02-10

"""
################################################################################
use FTP to upload all files from one local dir to a remote site/directory;
e.g., run me to copy a web/FTP site's files from your PC to your ISP;
assumes a flat directory upload: uploadall.py does nested directories.
see downloadflat.py comments for more notes: this script is symmetric.
################################################################################
"""

import os, sys, ftplib
from getpass import getpass
from mimetypes import guess_type

nonpassive = False                                  # passive FTP by default
remotesite = 'localhost'                            # upload to this site
#                                                     from machine running on
remotedir = (len(sys.argv) > 1 and sys.argv[1]) or '.'
remoteuser = input('User Name: ')
remotepass = getpass('Password for %s on %s: ' % (remoteuser, remotesite))
localdir = (len(sys.argv) > 2 and sys.argv[2]) or '.'
cleanall = input('Clean remote directory first? ')[:1] in ['y', 'Y']

print('Connecting...')
connection = ftplib.FTP(remotesite)                 # connect to FTP site
connection.login(remoteuser, remotepass)            # log in as user/password
connection.cwd(remotedir)                           # cd to directory to copy
if nonpassive:                                      # force active mode FTP
    connection.set_pasv(False)                      # most servers do passive

if cleanall:
    for remotename in connection.nlst():            # try to delete all remotes
        try:                                        # first, to remove old files
            print('Deleting remote', remotename)
            connection.delete(remotename)           # skips . and .. if attempted
        except:
            print('Cannot delete remote', remotename)

count = 0                                           # upload all local files
localfiles = os.listdir(localdir)                   # listdir() strips dir path

for localname in localfiles:
    mimetype, encoding = guess_type(localname)      # e.g., ('text/plain', 'gzip')
    mimetype = mimetype or  '?/?'                   # may be (None, None)
    maintype = mimetype.split('/')[0]               # .jpg ('image/jpeg', None)
    
    localpath = os.path.join(localdir, localname)
    print('Uploading', localpath, 'to', localname, end=' ')
    print('as', maintype, encoding or '')
    
    if maintype == 'text' and encoding == None:
        # use ascii mode xfer and bytes file
        # needf rb mode ftplib's crlf logic
        localfile = open(localpath, 'rb')
        connection.storlines('STOR ' + localname, localfile)
    else:
        # use binary mode xfer and bytes file
        localfile = open(localpath, 'rb')
        connection.storbinary('STOR ' + localname, localfile)
    
    localfile.close()
    count += 1

connection.quit()
print('Done:', count, 'files uploaded.')