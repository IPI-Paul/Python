#!/usr/bin/env python3

# Example 13-29
# Can be used to grab any file from any server machine running an HTTP web 
# server program
# Author: Mark Lutz
# Last modified: 

"""
fetch a file from an HTTP (web) server over sockets via http.client; the filename
parameter may have a full directory path, and may name a CGI script with ? query
parameters on the end to invoke a remote program; fetched file data or remote 
program output could be saved to a local file to mimic FTP, or parsed with 
str.find or html.parser module; also: http.client 
request(methos, url, body=None, hdrs{});
"""

import sys, http.client
showlines = 6
try:
    servername, filename = sys.argv[1:]             # cmdline args?
except:
    servername,filename = '', '/iisstart.htm'       # 'learning-python.com'

print(servername, filename)
server = http.client.HTTPConnection(servername)     # connect to http site/server
server.putrequest('GET', filename)                  # send request and headers
server.putheader('Accept', 'text/html')             # POST requests work here too
server.endheaders()                                 # as do CGI script filenames

reply = server.getresponse()                        # read reply headers + data
if reply.status != 200:                             # 200 means success
    print('Error sending request', reply.status, reply.reason)
else:
    data = reply.readlines()                        # file obj for data received
    reply.close()                                   # show lines with eoln at end
    for line in data[:showlines]:                   # to save, write data to file
        print(line)                                 # line already has \n, but bytes