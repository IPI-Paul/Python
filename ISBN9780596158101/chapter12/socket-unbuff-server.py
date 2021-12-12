#!/usr/bin/env python3

# Example 12-13
# Illustrates a simple socket server that simply reads three messages using the 
# raw socket interface
# Author: Mark Lutz
# Last modified: 

from socket import *            # read three messages over a raw socket
sock = socket()
sock.bind(('', 60000))
sock.listen(5)
print('accepting...')
conn, id = sock.accept()        # blocks till client connect

for i in range(3):
    print('receiving...')
    msg = conn.recv(1024)       # blocks till data received
    print(msg)                  # gets all print lines at once unless flushed