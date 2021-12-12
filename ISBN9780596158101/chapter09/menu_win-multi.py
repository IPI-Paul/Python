#!/usr/bin/env python3

# Example 9-2
# Makes three pop-up windows with the same menu bar as Example 9-1
# Author: Mark Lutz
# Last modified: 

from menu_win import makemenu                       # reuse menu maker function
from tkinter import *

root = Tk()
for i in range(3):
    win = Toplevel(root)
    makemenu(win)
    Label(win, bg='black', height=5, width=25).pack(expand=YES, fill=BOTH)
Button(root, text='Bye', command=root.quit).pack()
root.mainloop()