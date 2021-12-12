#!/usr/bin/env python3

# Example 9-14
# Demonstrates, scroll bars canbe cross-linked with a canvas using the same 
# protocols used to add them to listboxes and text, but with a few unique 
# requirements
# Author: Mark Lutz
# Last modified: 

'a simple vertically-scrollable canvas component and demo'

from tkinter import *

class ScrollableCanvas(Frame):
    
    def __init__(self, parent=None, color='brown'):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)                # make me expandable
        canv = Canvas(self, bg=color, relief=SUNKEN)
        canv.config(width=300, height=200)              # display area size
        canv.config(scrollregion=(0, 0, 300, 1000))     # canvas size corners
        canv.config(highlightthickness=0)               # no pixels to border
        
        sbar = Scrollbar(self)
        sbar.config(command=canv.yview)                 # link sbar and canv
        canv.config(yscrollcommand=sbar.set)            # moveone moves other
        sbar.pack(side=RIGHT, fill=Y)                   # pack first=clip last
        canv.pack(side=LEFT, expand=YES, fill=BOTH)     # canv clipped first
        
        self.fillContent(canv)
        canv.bind('<Double-1>', self.onDoubleClick)     # set event handler
        self.canvas = canv
    
    def fillContent(self, canv):                        # override me below
        for i in range(10):
            canv.create_text(150, 50+(i*100), text='spam'+str(i), fill='beige')
    
    def onDoubleClick(self, event):                     # override me below
        print(event.x, event.y)
        print(self.canvas.canvasx(event.x), self.canvas.canvasy(event.y))

if __name__ == '__main__': ScrollableCanvas().mainloop()