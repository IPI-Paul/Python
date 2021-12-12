#!/usr/bin/env python3

# Example 13-2
# Does the same as the one in Example 13-1, but it uses the general urllib.request
# module to fetch the source distribution file, instead of the protocol-specified
# ftplib
# Author: Mark Lutz, Paul I Ighofose
# Last modified: 2019-02-08

"""
A Python script to download a file by FTP by its URL string; use higer-level
urllib instead of ftplib to fetch file; urllib supports FTP, HTTP, client-side 
HTTPS, and local files, and handles proxies, redirects, cookies, and more; urllib 
also allows downloads of html pages, images, text, etc.; see allso Python 
html/xml parsers for web pages fetched by urllib in Chapter 19;
"""

import os, getpass
from urllib.request import urlopen          # socket-based web tools

filename = 'Earth.jpg'                      # remote/local filename
userName = input('User Name: ')
password = getpass.getpass('Pswd?')

# remoteaddr = 'ftp://lutz:%s@ftp.rmi.net/%s; type=i' % (password, filename)
dirname = 'Java/ISBN100134177290/sourceFiles/images' 
login = (userName, password, dirname, filename)
remoteaddr = 'ftp://%s:%s@localhost/%s/%s; type=i' % login
print('Downloading', remoteaddr)

# this works too:
# urllib.request.urlretrieve(remoteaddr, filename)

remotefile = urlopen(remoteaddr)            # returns input file-like object
localfile = open(filename, 'wb')            # where to store data locally
localfile.write(remotefile.read())
localfile.close()
remotefile.close()