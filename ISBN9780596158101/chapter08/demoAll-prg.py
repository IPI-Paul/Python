#!/usr/bin/env python3

# Example 8-34
# Spawns each of the four demo launchers as independent programs (processes), 
# using the launchmodes module written earlier
# Author: Mark Lutz
# Last modified: 

"""
4 demo classes run as independent program processes: command lines;
if one window is quit now, the others will live on; there is no simple way to 
run all report calls here (though sockets and pipes could be used for IPC), and
some launch schemes may drop child program stdout and disconnect parent/child;
"""

from tkinter import *
import os, sys
sys.path.append('..')
from chapter05.launchmodes import PortableLauncher
demoModules = ['demoDlg', 'demoRadio', 'demoCheck', 'demoScale']

for demo in demoModules:                        # see Parallel System Tools
    PortableLauncher(demo, demo + '.py')()      # start as top-level programs

root = Tk()
root.title('Processes')
Label(root, text='Mulitple program demo: command lines', bg='white').pack()
root.mainloop()