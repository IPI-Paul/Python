#!/usr/bin/env python3

# Example 9-4
# Shows how both window and Frame menu bars are completely functional in the 
# same single window
# Author: Mark Lutz
# Last modified: 

from menu_frm import makemenu           # can't use menu_win here-- one window
from tkinter import *                   # but can attach frame menus to windows

root = Tk()
for i in range(2):                      # 2 menus nested in one window
    mnu = makemenu(root)
    mnu.config(bd=2, relief=RAISED)
    Label(root, bg='black', height=5, width=25).pack(expand=YES, fill=BOTH)
Button(root, text='Bye', command=root.quit).pack()
root.mainloop()