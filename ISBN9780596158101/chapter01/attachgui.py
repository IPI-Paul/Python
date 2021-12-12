#!/usr/bin/env python3

# Example 1-26
# Is a generated as a subclass of Frame and automatically becomes an attachable
# component
# Author: Mark Lutz
# Last modified: 

from tkinter import *
from tkinter102 import MyGui

# main app window
mainwin = Tk()
Label(mainwin, text=__name__).pack()

# popup window
popup = Toplevel()
Label(popup, text='Attach').pack(side=LEFT)
MyGui(popup).pack(side=RIGHT)                   # attach my frame
mainwin.mainloop()