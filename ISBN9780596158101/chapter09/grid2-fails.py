#!/usr/bin/env python3

# Example 9-21
# Fails in its attempt to use pack and grid within the same parent--only one 
# geometry manager can be used on any one parent
# Author: Mark Lutz
# Last modified: 

"""
FAILS-- can't grid and pack in same parent container (here, root window)
"""

from tkinter import *
from grid2 import gridbox, packbox

root = Tk()
gridbox(root)
try:
    packbox(root)
except Exception as e:
    print('packbox:', e)

try:
    Button(root, text='Quit', command=root.quit).pack()
except Exception as e:
    print('Button: ', e)
mainloop()