#!/usr/bin/env python3

# Example 8-30
# Makes two scales- one horizontal and one vertical- and links them with an 
# associated variable to keep them in sync
# Author: Mark Lutz, Paul I Ighofose
# Last modified: 2018-11-19

'create two linked scales used to launch dialog demos'

from tkinter import *                           # get base widget set
from dialogTable import demos                   # button callback handlers
from quitter import Quitter                     # attach a quit frame to me

class Demo(Frame):
    
    def __init__(self, parent=None, **options):
        Frame.__init__(self, parent, **options)
        self.pack()
        Label(self, text='Scale demos').pack()
        self.var = IntVar()
        self.demos = sorted(demos)
        Scale(self, label='Pick demo number',
              command=self.onMove,                      # catch moves
              variable=self.var,                        # reflects position
              from_=0, to=len(demos)-1
              ).pack()
        self.scale = Scale(self, label=self.demos[0],#'Pick demo number',
              command=self.onMove,                      # catch moves
              variable=self.var,                        # reflects position
              from_=0, to=len(demos)-1,
              length=200, tickinterval=1,
              showvalue=YES, orient='horizontal'
              )
        self.scale.pack()
        Quitter(self).pack(side=RIGHT)
        Button(self, text='Run demo', command=self.onRun).pack(side=LEFT)
        Button(self, text='State', command=self.report).pack(side=LEFT)
    
    def onMove(self, value):
        self.scale['label'] = self.demos[self.var.get()]
        print('in onMove', value)
    
    def onRun(self):
        pos = self.var.get()
        print('you picked %d (%s)' % (pos, self.demos[pos]))
        demo = demos[self.demos[pos]]       # map from position to value (3.X view)
        print(demo())                       # or demos[list(demos.keys())[pos]]()
    
    def report(self):
        print('%d (%s)' % (self.var.get(), self.demos[self.var.get()]))

if __name__ == '__main__':
    print(list(demos.keys()))
    Demo().mainloop()