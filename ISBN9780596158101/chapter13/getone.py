#!/usr/bin/env python3

# Example 13-1
# This script automatically fetches a.k.a. "downloads") and opens a remote file 
# with Python.
# Author: Mark Lutz
# Last modified: 

"""
A Python script to download and play a media file by FTP. Uses ftplib, te ftp 
protocol handler which uses sockets. FTP runs on 2 sockets, (one for data, 
one for control--on ports 20 and 21) and imposes message text formats, but 
Python's ftplib module hides most of ths protocol's detals. Change for yur 
site/file
"""

import os, sys
from getpass import getpass                 # hidden password input
from ftplib import FTP                      # socket-based FTP tools

nonpassive = False                          # force active mode FTP for server?
filename = 'Earth.jpg'                      # file to be downloaded
#                                             remote directory to fetch from
dirname = 'Java/ISBN100134177290/sourceFiles/images' 
# sitename = 'ftp.rmi.net'                  # FTP site to contact
sitename = 'localhost'
# userinfo = ('lutz', getpass('Pswd?'))     # use () for anonymous
userinfo = (input('User Name: '), getpass('Pswd?'))
if len(sys.argv) > 1: filename = sys.argv[1]   # filename on command line?

print('Connecting...')
connection = FTP(sitename)                  # connect to FTP site
connection.login(*userinfo)                 # default is anonymous login
connection.cwd(dirname)                     # xfer 1k at a time to localfile
if nonpassive:                              # force active FTP if server requires
    connection.set_pasv(False)

print('Downloading...')
localfile = open(filename, 'wb')            # local file to store download
connection.retrbinary('RETR ' + filename, localfile.write, 1024)
connection.quit()
localfile.close()

if input('Open file?') in ['Y', 'y']:
    sys.path.append('..')
    from chapter06.playfile import playfile
    playfile(filename)