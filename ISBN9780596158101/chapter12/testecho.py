#!/usr/bin/env python3

# Example 12-3
# Fire's up eight copies of the client script in parallel. Uses launchmodes 
# module to spawn clients and alternatives such as multiprocessing and 
# subprocess modules
# Author: Mark Lutz
# Last modified: 

import sys, os
sys.path.append('..')
from chapter05.launchmodes import QuietPortableLauncher

numclients = 8
def start(cmdline):
    QuietPortableLauncher(cmdline, cmdline)()

# start('echo-server.py')               # spawn server locally if not yet started

args = ' '.join(sys.argv[1:])           # pass server name if running remotely
for i in range(numclients):
    start('echo-client.py %s' % args)   # spawn *? clients to test the server