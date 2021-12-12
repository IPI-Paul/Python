#!/usr/bin/env python3

# Example 12-8
# This module's primary classes implement servers which process clients in parallel
# (a.k.a. asynchronously) to avoid denying service to new requestes during long-
# running transactions. Their net effect is to automate the top-levels of 
# common server code
# Author: Mark Lutz
# Last modified: 

"""
Server side: open a socket on a port, listen for a messsage from a client, and 
send an echo reply; this version uses the standard library modul socketserver to 
do its work; socketserver provides TCPServer, ThreadingTCPServer, ForkingTCPServer, UDP variants of these, and more, and routes each client connect request to a new 
instance of a passed-in request handler object's handle method; socketserver 
also supports Unix domain sockets, but only on Unixen; see the Python library
manual.
"""

import socketserver, time               # get socket server, handler objects
myHost = ''                             # server machine, '' means local host
myPort = 50007                          # listen on a non-reserved port number

def now():
    return time.ctime(time.time())

class MyClientHandler(socketserver.BaseRequestHandler):
    def handle(self):                           # on each client connect
        print(self.client_address, now())       # show this client's address
        time.sleep(5)                           # simulate a blocking activity
        while True:                             # self.request is client socket
            data = self.request.recv(1024)      # read, write a client socket
            if not data: break
            reply = 'Echo=>% at %s' % (data, now())
            self.request.send(reply.encode())
        self.request.close()

# make a threaded server, listen/handle clients forever
myaddr = (myHost, myPort)
server = socketserver.ThreadingTCPServer(myaddr, MyClientHandler)
server.serve_forever()