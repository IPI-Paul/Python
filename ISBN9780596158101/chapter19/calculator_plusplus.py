#!/usr/bin/env python3

# Example 19-24
# Puts up four distinct calculator windows
# Author: Mark Lutz
# Last modified: 

"""
demo all 3 calculator flavors at once
each is a distinct calculator object and window
"""

from tkinter import Tk, Button, Toplevel
import calculator, calculator_plus_ext, calculator_plus_emb

root = Tk()
calculator.CalcGui(Toplevel())
calculator.CalcGui(Toplevel(), fg='white', bg='purple')
calculator_plus_ext.CalcGuiPlus(Toplevel(), fg='gold', bg='black')
calculator_plus_emb.CalcGuiPlus(fg='black', bg='orange')
Button(root, text='Quit Calcs', command=root.quit).pack()
root.mainloop()