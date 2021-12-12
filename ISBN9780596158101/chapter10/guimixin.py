#!/usr/bin/env python3

# Example 10-2
# Implements common methods in a class and inherit them every-where they are needed
# Mixin classes like this can access the subject instance, self, to utilize both 
# per-instance state and inherited methods
# Author: Mark Lutz
# Last modified: 

"""
################################################################################
a 'mixin' class for other frames: common methods for canneddialogs, spawning 
programs, simple text viewers, etc; this class must be mixed with a Frame (or a
subclass derived from Frame) for its quit method
################################################################################
"""

from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import os, sys
sys.path.append('..')
from chapter09.scrolledtext import ScrolledText               # or tkinter.scrolledtext
from chapter05.launchmodes import PortableLauncher, System    # or use multiprocessing

class GuiMixin:    
    def infobox(self, title, text, *args):          # use standard dialogs
        return showinfo(title, text)                # *args for bkwd compat
    
    def errorbox(self, text):
        showerror('Error!', text)
    
    def question(self, title, text, *args):
        return askyesno(title, text)               # return True or False
    
    def notdone(self):
        showerror('Not implemented', 'Option not available')
    
    def quit(self):
        ans = self.question('Verify quit', 'Are you sure you want to quit?')
        if ans:
            Frame.quit(self)                        # quit not recursive!
    
    def help(self):
        self.infobox('RTFM', 'See figure 1...')     # override this better
    
    def selectOpenFile(self, file='', dir='.'):     # use standard dialogs
        return askopenfilename(initialdir=dir, initialfile=file)
    
    def selecSaveFile(self, file='', dir='.'):
        return asksaveasfilename(initifile=file, initialdir=dir)
    
    def clone(self, args=()):               # optional constructor args
        new = Toplevel()                    # make new in-process version of me
        myclass = self.__class__            # instance's (lowest) class object
        myclass(new, *args)                 # attach/run instance to new window
    
    def spawn(self, pycmdline, wait=False):
        if not wait:
            PortableLauncher(pycmdline, pycmdline)()    # run Python program
        else:
            System(pycmdline, pycmdline)()              # wait for it to exit
    
    def browser(self, filename):
        new = Toplevel()                                # make new window
        view = ScrolledText(new, file=filename)         # Text with Scrollbar
        view.text.config(height=30, width=85)           # config Text in Frame
        view.text.config(font=('courier', 10, 'normal'))# use fixed-width font
        new.title('Text Viewer')                        # set window mgr attrs
        new.iconname('browser')                         # file text added auto
    
    """
    def browser(self, filename):                        # if tkinter.scrolledtext
        new = Toplevel()                                # included for reference
        text.config(font=('courier', 10, 'normal'))
        text.pack(expand=YES, fill=BOTH)
        new.title('Text Viewer')
        new.iconname('browser')
        text.insert('0.0', open(filename, 'r').read()) 
    """
    
if __name__ == '__main__':
    
    class TestMixin(GuiMixin, Frame):               # standalone test
        def __init__(self, parent=None):
            Frame.__init__(self, parent)
            self.pack()
            Button(self, text='quit', command=self.quit).pack(fill=X)
            Button(self, text='help', command=self.help).pack(fill=X)
            Button(self, text='clone', command=self.clone).pack(fill=X)
            Button(self, text='open', command=self.selectOpenFile).pack(fill=X)
            Button(self, text='spawn', command=self.other).pack(fill=X)
        
        def other(self):
            self.spawn('guimixin.py')       # spawn self as separate process
    
    TestMixin().mainloop()