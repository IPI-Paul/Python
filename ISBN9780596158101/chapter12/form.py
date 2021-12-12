#!/usr/bin/env python3

# Example 12-20
# Is a general-purpose form-layout class that handles most of the GUI layout 
# grunt work
# Author: Mark Lutz, Paul I Ighofose
# Last modified: 2019-02-05

"""
################################################################################
a reusable form class, used by getfilegui (andd  others)
################################################################################
"""

from tkinter import *
entrysize = 40

class Form:                                         # add non-modal form box
    def __init__(self, labels, parent=None):        # pass field labels list
        labelsize = max(len(x) for x in labels) + 2
        box = Frame(parent)                         # box has rows, buttons
        box.pack(expand=YES, fill=X)                # rows has row frames
        rows = Frame(box, bd=2, relief=GROOVE)      # go=button or return key
        rows.pack(side=TOP, expand=YES, fill=X)     # runs onSubmit method
        self.content = {}
        
        for label in labels:
            row = Frame(rows)
            row.pack(fill=X)
            Label(row, text=label.strip(), width=labelsize, anchor=W).pack(side=LEFT)
            entry = Entry(row, width=entrysize)
            if 'password' in label.lower() or 'pswd' in label.lower():
                entry.configure(show='*')
            entry.pack(side=RIGHT, expand=YES, fill=X)
            self.content[label.strip()] = entry
        Button(box, text='Cancel', command=self.onCancel).pack(side=RIGHT)
        Button(box, text='Submit', command=self.onSubmit).pack(side=RIGHT)
        box.master.bind('<Return>', (lambda event: self.onSubmit()))
    
    def onSubmit(self):                                     # override this
        labelsize = max(len(x) for x in self.content) + 2
        for key in self.content:                            # user inputs in
            # print(key, '\t=>\t', self.content[key].get())   # self.content[k]
            if 'password' in key.lower() or 'pswd' in key.lower():
                pwd = '*' * len(self.content[key].get())
                print(key, ' ' * (labelsize - len(key)), pwd)
            else:
                print(key, ' ' * (labelsize - len(key)), self.content[key].get())
        
    def onCancel(self):                                     # override if need
        Tk().quit()                                         # default is exit

class DynamicForm(Form):
    def __init__(self, labels=None):
        labels = input('Enter field names (separated by a comma): ').split(',')
        Form.__init__(self, labels)
        
    def onSubmit(self):
        print('Field values...')
        Form.onSubmit(self)
        self.onCancel()

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        Form(['Name', 'Age', 'Job'])        # precoded fiels, stay after submit
    else:
        DynamicForm()                       # input fields, go away after submit
    mainloop()