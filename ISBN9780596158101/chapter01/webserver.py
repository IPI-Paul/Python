#!/usr/bin/env python3

# Example 1-32
# Provides what is needed to serve up web content using standard library modules
# Author: Mark Lutz
# Last modified: 

"""
Implement an HTTP web server in Python that knows how to run server-side CGI 
scripts coded in Python; serves files and scripts from current working dir; 
Python scripts must be stored in webdir\cgi-bin or webdir\htbin;
"""

import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

# where your html files and cgi-bin script directory live
webdir = os.path.abspath('../sourceFiles/html')
port = 80 # default http://localhost/, else use http://localhost:xxxx/

os.chdir(webdir)                                    # run in HTML root dir
srvraddr = ('', port)                               # my hostname, portnumber
srvrobj = HTTPServer(srvraddr, CGIHTTPRequestHandler)
srvrobj.serve_forever()