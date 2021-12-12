#!/usr/bin/env python3

# Example 12-14
# Illustrates a simple socket client that sends three messages; the first two 
# over a socket wrapper file, and the last using the raw socket  
# Author: Mark Lutz
# Last modified: 

import time                         # send three msgs over wrapped and raw socket
from socket import *
sock = socket()                     # default=AF_INET, SOCK_STREAM (tcp/ip)
sock.connect(('localhost', 60000)) 
file = sock.makefile('w', buffering=1)  # default=full buff, 0=error, 1 not linebuff!

print('sendig data1')
file.write('spam\n')
time.sleep(5)               # must follow with flush( to truly send now
# file.flush()              # uncomment flush lines to see the difference

print('sending data2')
print('eggs', file=file)    # adding more file prints does not flush buffer either
time.sleep(5)
# file.flush()              # output appears at server recv only upon flush or exit

print('sending data3')
sock.send(b'ham\n')         # low-level byte string interface sends immediately
time.sleep(5)