#!/usr/bin/env python3

# Example 10-25
# This script implements a GUI to display the text printed by the non-GUI 
# program, but it knows nothing of that other program's logic
# Author: Mark Lutz
# Last modified: 

# GUI server side: read and display non-GUI script's output

import sys, os
from socket import *                        # including socker.error
from tkinter import Tk
sys.path.append('..')
from chapter05.launchmodes import PortableLauncher
from guiStreams import GuiOutput

myport = 50008
sockobj = socket(AF_INET, SOCK_STREAM)       # GUI is server, script is client
sockobj.bind((' ', myport))                  # config server before client
sockobj.listen(5)

print('starting')
PortableLauncher('nongui', 'socket-nongui.py -gui')()   # spawn non-GUI script

print('accepting')
conn, addr = sockobj.accept()               # wait for client to connect
conn.setblocking(False)                     # use nonblocking socket (False=0)
print('accepted')

def checkdata():
    try:
        message = conn.recv(1024)           # don't block for input
        #output.write(message + '\n')       # could do sys.stdout=output too
        print(message, file=output)         # if ready, show text in GUI window
    except error:                           # raises socket.error if not ready
        print('no data')                    # print to sys.stdout
    root.after(1000, checkdata)             # check once per second

root = Tk()
output = GuiOutput(root)                    # socket text is displayed on this
checkdata()
root.mainloop()