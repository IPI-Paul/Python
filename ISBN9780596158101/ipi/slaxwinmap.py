#!/usr/bin/env python3

# Example by IPI-Paul. 
# Creates a a Linux mount to a windows share when running linux as a VMWare
# Author: Paul I Ighofose
# Last modified: 2018-11-29

"""
A class that allows the user to create mounts to Windows shares in SLAX (Debian)
"""

import os, subprocess
from tkinter import *
from tkinter.messagebox import *

class SlaxWinMap:
    
    def __init__(self, parent=None):
        lblShare = Label(win, text='UNC Path to share (//ip_address/../share):'
                       ).grid(row=0, column=0, sticky=W)
        self.Share = Entry(win, width=50)
        self.Share.grid(row=0, column=1)
        lblMount = Label(win, text='Mount Folder (/mnt/win):'
                       ).grid(row=1, column=0, sticky=W)
        self.Mount = Entry(win, width=50)
        self.Mount.grid(row=1, column=1)
        lblUser = Label(win, text='User Name:'
                       ).grid(row=2, column=0, sticky=W)
        self.User = Entry(win, width=50)
        self.User.grid(row=2, column=1)
        lblPassword = Label(win, text='Password:'
                       ).grid(row=3, column=0, sticky=W)
        self.Password = Entry(win, show='*', width=50)
        self.Password.grid(row=3, column=1)
        Button(win, text='Create', command=self.mount).grid(row=4, column=1)

    def mount(self):
        if not os.path.exists(self.Mount.get()):
            os.mkdir(self.Mount.get())
        p = subprocess.Popen('mount -t cifs "%s" "%s" -o username="%s",password="%s"' % 
              (self.Share.get(), self.Mount.get(), self.User.get(), self.Password.get()), 
              stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        p_status = p.wait()
        showinfo('Mount Shared Folder', 'Mounted: ' + self.Share.get())

if __name__ == '__main__':
    win = Tk()
    win.title('SLAX - Mount Windows Shares')
    SlaxWinMap(win)
    win.mainloop()