#!/usr/bin/env python3

# Example 10-6
# Defines subclasses of the two type-specific ShellGui classes, to provide sets 
# of available tools in both list and dictionary formats
# Author: Mark Lutz, Paul I Ighofose
# Last modified: 2018-12-07

"""
################################################################################
provide type-specific option sets for application
################################################################################
"""

from shellgui import *                              # type-specfic option gui
from packdlg import runPackDialog                   #dialogs for data entry
from unpkdlg import runUnpackDialog                 # they both run app classes 
from unpacker import unpack

class TextPak1(ListMenuGui):
    def __init__(self):
        self.myMenu = [('Pack  ', runPackDialog),   # simple functions
                       ('Unpack', runUnpackDialog), # use same width here
                       ('Unpack New', unpackNew), 
                       ('Mtool', self.notdone)]     # method from guimixin
        ListMenuGui.__init__(self)
    
    def forToolBar(self, label):
        return label in {'Pack  ', 'Unpack', 'Unpack New'}        # 3.x set syntax

class TextPak2(DictMenuGui):
    def __init__(self):
        self.myMenu = {'Pack  ': runPackDialog,     # or use input here...
                       'Unpack': runUnpackDialog,   # instead of in dialogs
                       'Unpack New': unpackNew, 
                       'Mtool': self.notdone}
        DictMenuGui.__init__(self)

def unpackNew():
    from unpkdlg import unpackDialog
    input = unpackDialog()                      # get input from GUI
    if input != '':                             # do non-GUI file stuff
        print('Unpacker:', input)               # run with input from dialog
        unpack(ifile=input)

if __name__ == '__main__':                          # self-test code...
    from sys import argv                            # 'menugui.py list|^'
    if len(argv) > 1 and argv[1] == 'list':
        print('list test')
        TextPak1().mainloop()
    else:
        print('dict test')
        TextPak2().mainloop()