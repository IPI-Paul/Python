#!/usr/bin/env python3

# Example 10-30
# Constructs a bar of buttons that run programs in demonstration mode, not for 
# day-to-day use
# Author: Mark Lutz
# Last modified: 

"""
################################################################################
PyDemos.pyw
Programming Python, 2nd, 3rd, and 4th Editions (PP4E), 2001--2006--2010

Version 2.1 (4E), April '10: updated to run under Pytho 3.x, and spawn
local web servers for web demos only on first demo button selection

Version 2.0 (3E), March '06: add source-code file viewer buttons; and new Demos 
(PyPhoto, PyMailGUI); spawn locally running web servers foir the browser-based 
Demos; add window icons; and probably more I've forgotten.

Launch major Python+Tk GUI examples from the book, in a platform-neutral way.
This file also serves as an index to major program examples, though many book
examples aren't GUI-based, and so aren't listed here. Also see:

- PyGadgets.py, a simpler script for starting programs in non-demo mode that you 
  wish to use on a regular basis
- PyGadgets_bar.pyw, which creates a button bar for starting all PyGadgets
  programs on demand, not all at once
- Launch_*.pyw for starting PyDemos and PyGadgets with Launcher.py--runthese for 
  a quick look
- LaunchBrowser.pyw for running exaple web pages with an automatically located 
  web browser
- README-PP4E.txt, for generalexampkes information

Caveat: this program tries to start a locally running web server and web Browser
automatically, for web-based demos, but does not kill the server
################################################################################
"""

#...code omitted see examples package

################################################################################
# start building main GUI windows
################################################################################

from windows import MainWindow      # a Tk with icon, title, quit
from windows import PopupWindow     # same but Toplevel, diff quit
Root = MainWindow('PP4E Demos 2.1')
# build message window
Stat = PopupWindow('PP4E demo info')
Stat.protocol('WM_DELETE_WINDOW', lambda:0)     # ignore wm delete

from tkinter import *
Info = Label(Stat, text='Select demo',
             font=('courier', 20, 'italic'), padx=12, pady=12, bg='lightblue')
Info.pack(expand=YES, fill=BOTH)

################################################################################
# add launcher buttons with callback objects
################################################################################

import sys, os
sys.path.append('..')
from chapter11.textEditor import TextEditorMainPopup

# demo launcher class
# import sys, os
import chapter05.launchmodes as launchmodes
class Launcher(launchmodes.PortableLauncher):   # use wrapped launcher class
    def announce(self, text):                   # customize to set GUI label
        Info.config(text=text)

def viewer(sources):
    for filename in sources:
        # print(filename)
        TextEditorMainPopup(Root, filename,     # as pop up in this process
                 loadEncode='utf-8')            # else PyEdit may ask each!

def demoButton(name, what, doit, code):
    """
    add buttons that runs doit command-line, and open all files in code; doit 
    button retains state in an object, code in an emclosing scope;
    """
    rowfrm = Frame(Root)
    rowfrm.pack(side=TOP, expand=YES, fill=BOTH)
    
    b = Button(rowfrm, bg='navy', fg='white', relief=RIDGE, border=4)
    b.config(text=name, width=20, command=Launcher(what, doit))
    b.pack(side=LEFT, expand=YES, fill=BOTH)
    
    b = Button(rowfrm, bg='beige', fg='navy')
    b.config(text='code', command=(lambda: viewer(code)))
    b.pack(side=LEFT, fill=BOTH)

################################################################################
# tkinter GUI demos - some use network connections
################################################################################

demoButton(name='PyEdit',
           what='Text file editor',                     # edit myself
           doit='../chapter11/textEditor.py PyDemos.pyw',
           code=['../chapter05/launchmodes.py',
                 '../chapter06/find.py',
                 '../chapter09/scrolledlist.py',        # show in Pyedit viewer
                 'formrows.py',                         # last = top of stacking
                 'guimaker.py',
                 '../chapter11/textConfig.py',
                 '../chapter11/textEditor.py'])

demoButton(name='PyView',
           what='Image slideshow, plus note editor',
           doit='../chapter11/slideShowPlus.py ../sourceFiles/images',
           code=['../chapter11/textEditor.py',
                 '../chapter11/slideShow.py',
                 '../chapter11/slideShowPlus.py'])

demoButton(name='PyClock',
           what='Digital and Analog Clocks',
           doit='../chapter11/clock.py -size 175 -bg white -picture ' + \
           '../sourceFiles/images/face.gif',
           code=['../chapter11/clock.py',
                 '../chapter11/clockStyles.py',
                 '../chapter11/plotterGui.py'])

# ...code omitted: see examples package..

################################################################################
# toggle info message box font once a second
################################################################################

def refreshMe(info, ncall):
    slant = ['normal', 'italic', 'bold', 'bold italic'][ncall % 4]
    info.config(font=('courier', 20, slant))
    Root.after(1000, (lambda: refreshMe(info, ncall+1)))

################################################################################
# unhide/hide status box onb info clicks
################################################################################

Stat.iconify()
def onInfo():
    if Stat.state() == 'iconic':
        Stat.deiconify()
    else:
        Stat.iconify() # was 'normal'

################################################################################
# finish building main GUI, start event loop
################################################################################

def onLinks():
    #...code omitted: see examples package..
    pass

Button(Root, text='Info', command=onInfo).pack(side=TOP, fill=X)
Button(Root, text='Links', command=onLinks).pack(side=TOP, fill=X)
Button(Root, text='Quit', command=Root.quit).pack(side=BOTTOM, fill=X)
refreshMe(Info, 0)          # start toggling
Root.mainloop()