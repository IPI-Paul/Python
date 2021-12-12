#!/usr/bin/env python3

# Example 19-23
# Extends PyCalc in a new subclass instead of embedding it
# Author: Mark Lutz
# Last modified: 

"""
################################################################################
a customization with an extra row of buttons for common operations;
a more useful customization: adds buttons for more operations (sqrt, 1/x, etc.)
by subclassing to extend the original class, not embedding; new buttons show up
before frame attached to bottom cy calcgui class;
################################################################################
"""

from tkinter import *
from calculator import CalcGui, getCalcArgs
import sys
sys.path.append('..')
from chapter10.widgets import label, frame, button

class CalcGuiPlus(CalcGui):
    def makeWidgets(self, *args):
        label(self, TOP, 'PyCalc Plus - Subclass')
        CalcGui.makeWidgets(self, *args)
        frm = frame(self, BOTTOM)
        extras = [('sqrt', 'sqrt(%s)'),
                  ('x^2 ', '(%s)**2'),
                  ('x^3 ', '(%s)**3'),
                  ('1/x ', '1.0/(%s)')]
        for (lab, expr) in extras:
            button(frm, LEFT, lab, (lambda expr=expr: self.onExtra(expr)))
        button(frm, LEFT, ' pi ', self.onPi)
    
    def onExtra(self, expr):
        try:
            self.text.set(self.eval.runstring(expr % self.text.get()))
        except:
            self.text.set('ERROR')
    
    def onPi(self):
        self.text.set(self.eval.runstring('pi'))

if __name__ == '__main__':
    CalcGuiPlus(**getCalcArgs()).mainloop()         # passes -bg, -fg on