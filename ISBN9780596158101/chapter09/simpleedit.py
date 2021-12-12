#!/usr/bin/env python3

# Example 9-11
# Extends Example 9-10 to add support for four common text-editing operations-
# filesave, text cut and paste, and string find searching
# Author: Mark Lutz
# Last modified: 

"""
add common edit tools to ScrolledText by inheritance; composition (embedding) 
would work just as well here; this is not robust!-- see PyEdit for a feature 
superset;
"""

import sys, os
from tkinter import *
from tkinter.simpledialog import askstring
from tkinter.filedialog import asksaveasfilename
sys.path.append('..')
from chapter08.quitter import Quitter
from scrolledtext import ScrolledText               # here, not Python's

class SimpleEditor(ScrolledText):                   # see PyEdit for more
    
    def __init__(self, parent=None, file=None):
        frm = Frame(parent)
        frm.pack(fill=X)
        Button(frm, text='Save', command=self.onSave).pack(side=LEFT)
        Button(frm, text='Copy', command=self.onCopy).pack(side=LEFT)
        Button(frm, text='Cut', command=self.onCut).pack(side=LEFT)
        Button(frm, text='Paste', command=self.onPaste).pack(side=LEFT)
        Button(frm, text='Find', command=self.onFind).pack(side=LEFT)
        Quitter(frm).pack(side=LEFT)
        ScrolledText.__init__(self, parent, file=file)
        self.text.config(font=('courier', 9, 'normal'))
    
    def onSave(self):
        filename = asksaveasfilename()
        if filename:
            alltext = self.gettext()                    # first through last
            open(filename, 'w').write(alltext)          # store text in file
    
    def onCopy(self):
        text = self.text.get(SEL_FIRST, SEL_LAST)       # error if no select
        self.clipboard_clear()
        self.clipboard_append(text)
    
    def onCut(self):
        self.onCopy()
        self.text.delete(SEL_FIRST, SEL_LAST)           # should wrap in try
    
    def onPaste(self):
        try:                                            # add clipboard text
            text = self.selection_get(selection='CLIPBOARD')
            self.text.insert(INSERT, text)
        except TclError:
            pass                                        # not to be pasted
    
    def onFind(self):
        target = askstring('SimpleEditor', 'Search String?')
        if target:
            where = self.text.search(target, INSERT, END) # from insert cursor
            if where:
                print(where)
                pastit = where + ('+%dc' % len(target)) # index past target
                #self.text.tag_remove(SEL, '1.0', END)  # remove selection
                self.text.tag_add(SEL, where, pastit)   # select found target
                self.text.mark_set(INSERT, pastit)      # set insert mark
                self.text.see(INSERT)                   # scroll display
                self.text.focus()                       # select text widget

if __name__ == '__main__':
    if len(sys.argv) > 1:
        SimpleEditor(file=sys.argv[1]).mainloop()   # filename on command line
    else:
        SimpleEditor(file=__file__).mainloop()