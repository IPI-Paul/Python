#!/usr/bin/env python3

# Example 13-10
# Automatially downloads by FTP all the files in directory at a remote site to a
# directory on the local machine
# Author: Mark Lutz, Paul I Ighofose
# Last modified: 2019-02-10

"""
################################################################################
use FTP to copy (download) all files from a single directory at a remote site to
directory on the local machine; run me periodically to mirror a flat FTP site 
directory to your ISP account; set user to 'anonymous' to do anonymous FTP; we 
could use try to skip file failures, butthe FTP connection is likely closed if 
any files fail; we could also try to reconnect with a new FTP instance before
each transfer: connects once now; if failures, try setting nonpassive for active
FTP, or disable firewalls; this also depends on a working FTP server, and 
possibly its load policies.
################################################################################
"""

import os, sys, ftplib
from getpass import getpass
from mimetypes import guess_type

nonpassive = False                              # passive FTP on by default in 2.1+
remotesite = 'localhost'                        # download from this site
#                                                 and this dir (e.g., public_html)
remotedir = (len(sys.argv) > 1 and sys.argv[1]) or '.'                         
remoteuser = input('User Name: ')
remotepass = getpass('Password for %s on %s: ' % (remoteuser, remotesite))
localdir = (len(sys.argv) > 2 and sys.argv[2]) or '.'
cleanall = input('Clean local directory first? ')[:1] in ['y', 'Y']

print('Connecting...')
connection = ftplib.FTP(remotesite)             # connect to FTP site
connection.login(remoteuser, remotepass)        # login as user/password
connection.cwd(remotedir)                       # cd to directory to copy
if nonpassive:                                  # force active mode FTP
    connection.set_pasv(False)                  # most servers do passive

if cleanall:
    for localname in os.listdir(localdir):      # try to delete all locals
        try:                                    # first, to remove old files
            print('Deleting local', localname)  # os.listdir omits . and ..
            os.remove(os.path.join(localdir, localname))
        except:
            print('Cannot delete local', localname)

count = 0                                       # download all remote files
remotefiles = connection.nlst()                 # nlst() gives files list
#                                                 dir() gives full details
for remotename in remotefiles:
    if remotename in ('.', '..'): continue      # some servers include . and ..
    mimetype, encoding = guess_type(remotename) # e.g., ('text/plain', 'gzip')
    mimetype = mimetype or '?/?'                # may be (None, None)
    maintype = mimetype.split('/')[0]           # .jpg ('image/jpeg', None)
    localpath = os.path.join(localdir, remotename)
    print('Downloading', remotename, 'to', localpath, end=' ')
    print('as', maintype, encoding or '')
    
    if maintype == 'text' and encoding == None:
        # use asii mode xfer and text file
        # use encoding compatible with ftplib's
        localfile = open(localpath, 'w', encoding=connection.encoding)
        callback = lambda line: localfile.write(line + '\n')
        connection.retrlines('RETR ' + remotename, callback)
    else:
        # use binary mode xfer and bytes file
        localfile = open(localpath, 'wb')
        connection.retrbinary('RETR ' + remotename, localfile.write)
    
    localfile.close()
    count += 1

connection.quit()
print('Done:', count, 'files downloaded.')