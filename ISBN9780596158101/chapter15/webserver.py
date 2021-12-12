#!/usr/bin/env python3

# Example 15-1
# A web server that allows the working directory and port number to be passed 
# in as command-line arguments
# Author: Mark Lutz
# Last modified: 

"""
Implement an HTTP web server in Python which knows how to server HTML pages and 
run server-side CGI scripts coded in Python; this is not a prodcution-grade 
server (e.g., no HTTPS, slow script launch/run on some platforms), but suffices 
for testing, especially on localhost;

Servers files and scripts from the current working dir and port 80 by default,
unless these options are specified in command-line arguments; Python CGI scripts
must be stored in wedir\cgi-bin or webdir\htbin; monre than one of this server
may be running on thesame machine to serve from different directories, as long 
as they listen on different ports;
"""

import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

# '.' where your HTML files and cgi-bin script directory live
webdir = '../sourceFiles/html'  
port = 80   # http://servername/ if 80, else use http://servername:xxx/

if len(sys.argv) > 1: webdir = sys.argv[1]              # command-line args
if len(sys.argv) > 2: port = int(sys.argv[2])           # else default ., 80
print('webdir "%s", port %s' % (webdir, port))

os.chdir(webdir)                                        # run in HTML root dir
srvraddr = ('', port)                                   # my hostname, portnumber
srvrobj = HTTPServer(srvraddr, CGIHTTPRequestHandler)
srvrobj.serve_forever()                                 # serve clients till exit