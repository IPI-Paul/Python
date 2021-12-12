#!/usr/bin/env python3

# Example 9-26
# Is coded as a class for reusability, and it adds a button to load the table's 
# data from a file
# Author: Mark Lutz
# Last modified: 

# recode as an embedable class

from tkinter import *
from tkinter.filedialog import askopenfilename
import sys, os
sys.path.append('..')
from chapter08.quitter import Quitter                         # reuse, pack, and grid

class SumGrid(Frame):
    
    def __init__(self, parent=None, numrow=5, numcol=5):
        Frame.__init__(self, parent)
        self.numrow = numrow                        # I am a frame container
        self.numcol = numcol                        # caller packs or grisd me
        self.makeWidgets(numrow, numcol)            # else only usable one way
    
    def makeWidgets(self, numrow, numcol):
        self.rows = []
        for i in range(numrow):
            cols = []
            for j in range(numcol):
                ent = Entry(self, relief=RIDGE)
                ent.grid(row=i+1, column=j, sticky=NSEW)
                ent.insert(END, '%d.%d' % (i, j))
                cols.append(ent)
            self.rows.append(cols)
        self.sums = []
        for i in range(numcol):
            lab = Label(self, text='?', relief=SUNKEN)
            lab.grid(row=numrow+1, column=i, sticky=NSEW)
            self.sums.append(lab)
        
        Button(self, text='Sum', command=self.onSum).grid(row=0, column=0)
        Button(self, text='Print', command=self.onPrint).grid(row=0, column=1)
        Button(self, text='Clear', command=self.onClear).grid(row=0, column=2)
        Button(self, text='Load', command=self.onLoad).grid(row=0, column=3)
        Quitter(self).grid(row=0, column=4)         # fails: Quitter(self).pack()
    
    def onPrint(self):
        for row in self.rows:
            for col in row:
                print(col.get(), end=' ')
            print()
        print()
    
    def onSum(self):
        tots = [0] * self.numcol
        for i in range(self.numcol):
            for j in range(self.numrow):
                if not ('__import__' in self.rows[j][i].get() and \
                        'system' in self.rows[j][i].get()):
                    tots[i] += eval(self.rows[j][i].get())  # sum current data
        for i in range(self.numcol):
            self.sums[i].config(text=str(tots[i]))
    
    def onClear(self):
        for row in self.rows:
            for col in row:
                col.delete('0', END)                        # delete content
                col.insert(END, '0.0')                      # preserve display
        for sum in self.sums:
            sum.config(text='?')
    
    def onLoad(self):
        file = askopenfilename()
        if file:
            for row in self.rows:
                for col in row: col.grid_forget()           # erase current gui
            for sum in self.sums:
                sum.grid_forget()
            
            filelines = open(file, 'r').readlines()         # load file data
            self.numrow = len(filelines)                    # resize to data
            self.numcol = len(filelines[0].split())
            self.makeWidgets(self.numrow, self.numcol)
            
            for(row, line) in enumerate(filelines):         # load into gui
                fields = line.split()
                for col in range(self.numcol):
                    self.rows[row][col].delete('0', END)
                    self.rows[row][col].insert(END, fields[col])

if __name__ == '__main__': 
    import sys
    root = Tk()
    root.title('Summer Grid')
    if len(sys.argv) != 3:
        SumGrid(root).pack()        # .grid works here too
    else:
        if not ('__import__' in sys.argv[1] and 'system' in sys.argv[1]) and \
           not ('__import__' in sys.argv[2] and 'system' in sys.argv[2]):
            rows, cols = eval(sys.argv[1], sys.argv[2])
        SumGrid(root, rows, cols).pack()
    mainloop()