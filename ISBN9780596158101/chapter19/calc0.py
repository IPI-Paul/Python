#!/usr/bin/env python3

# Example 19-17
# Implements a limited calculator GUI, whose buttons just add text to the input
# field at the top of the window in order to compose a Python expression string
# Author: Mark Lutz
# Last modified: 

"a simpliastic calculator GUI: expressions run all at once with eval/exec"

from tkinter import *
import sys
sys.path.append('..')
from chapter10.widgets import frame, button, entry

class CalcGui(Frame):
    def __init__(self, parent=None):                    # an extended frame
        Frame.__init__(self, parent)                    # on default top-level
        self.pack(expand=YES, fill=BOTH)                # all parts expandable
        self.master.title('Python Calculator 0.1')      # 6 frames plus entry
        self.master.iconname("pycalc")
        
        self.names = {}                                 # namespace for variables
        text = StringVar()
        entry(self, TOP, text)
        
        rows = ["abcd", "0123", "4567", "89()"]
        for row in rows:
            frm = frame(self, TOP)
            for char in row:
                button(frm, LEFT, char,
                       lambda char=char: text.set(text.get() + char))
        
        frm = frame(self, TOP)
        for char in "+-*/=":
            button(frm, LEFT, char,
                   lambda char=char: text.set(text.get() + ' ' + char + ' '))
        
        frm = frame(self, BOTTOM)
        button(frm, LEFT, 'eval', lambda: self.eval(text))
        button(frm, LEFT, 'clear', lambda: text.set(''))
    
    def eval(self, text):
        try:
            text.set(str(eval(text.get(), self.names, self.names))) # was 'x'
        except SyntaxError:
            try:
                exec(text.get(), self.names, self.names)
            except:
                text.set("ERROR")               # bad as statement too?
            else:
                text.set('')                    # worked as statement
        except:
            text.set("ERROR")                   # other eval expression errors

if __name__ == '__main__': CalcGui().mainloop()