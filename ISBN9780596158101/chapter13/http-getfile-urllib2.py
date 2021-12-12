#!/usr/bin/env python3

# Example 13-31
# This urllib.request downloader script uses the slightly higher-level urlretrieve 
# interface in that module to automatically save the downloaded file or script 
# to a local file on the client machine
# Author: Mark Lutz
# Last modified: 

"""
fetch a file from an HTTP (web) server over sockets via urllib; this version 
uses an interface that saves the fetched data to a local binary-mode file; the
loacal filename is either passed in as a cmdline arg or stripped from the URL 
with urllib.parse: the filename argument may have a directory path at the front 
and query parameters at end, so os.path.split is not enough (only splits off 
directory path); caveat: should urllib.parse.quote filename unless known ok--see
later chapters;
"""

import sys, os, urllib.request, urllib.parse
showlines = 6
try:
    servername, filename = sys.argv[1:3]                # first 2 cmdline args
except:
    servername, filename = 'localhost', '/iisstart.htm'

remoteaddr = 'http://%s%s' % (servername, filename)     # any address on the Net
if len(sys.argv) == 4:                                  # get result filename
    localname = sys.argv[3]
else:
    (scheme, server, path, parms, query, frag) = urllib.parse.urlparse(remoteaddr)
    localname = os.path.split(path)[1]

print(remoteaddr, localname)
urllib.request.urlretrieve(remoteaddr, localname)       # can be file or script
remotedata = open(localname, 'rb').readlines()          # saved to local file
for line in remotedata[:showlines]: print(line)         # file is bytes/binary