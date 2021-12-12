#!/usr/bin/env python3

# Example by IPI-Paul.
# Text search program that finds all text within Python readable files using 
# binary mode. Has functions to edit programs/documents found using specified 
# editor. Also has functions to run script files
# Author: Paul I Ighofose
# Last modified: 2018-11-15 

"""
A class that allows the user to search for strings within files in a directories
"""

import os, sys, subprocess

class ListFilesContaining:
    def __init__(self, args=[False]*8, string='', incl='Y', wd='.', subs='Y',  
                 multi='Y', fname='|', prn='N', vbose='N'):
        self.string = string if not args[0] else args[0]
        self.incl = (incl if not args[1] else args[1]).upper() 
        self.wd = os.path.abspath(wd if not args[2] else \
                                  args[2]).replace('"', '').replace("'", '') 
        self.subs = (subs if not args[3] else args[3]).upper()
        self.multi = (multi if not args[4] else args[4]).upper() 
        self.fname = fname if not args[5] else args[5]
        self.prn = (prn if not args[6] else args[6]).upper()
        self.vbose = (vbose if not args[7] else args[7]).upper()
        self.found = []
    
    def interactive(self):
        self.incl = 'Y' if input('Find files with (Y), without(N): ').upper() == \
            'Y' else 'N'
        self.getFolder()
        self.string = input('Please enter the text to find: ')
        self.prn = 'Y' if input('Do you want to print the contents' +
            ' (Y/N): ').upper() == 'Y' else 'N'
        self.vbose = 'Y' if input('Do you want to print file errors' +
            ' (Y/N): ').upper() == 'Y' else 'N'
        self.run()
    
    def confirm(self):
        while len(self.string) == 0:
            self.string = input('Please enter the text to find: ')
        
    def run(self):
        self.confirm()
        files = self.getFileList(self.wd)
        for file in files:
            if self.multi == 'Y' or (self.multi == 'N' and self.fname in file):
                self.findText(os.path.join(self.wd, file))
        if self.subs == 'Y':
            self.trySubfolders(self.wd)
        

    def currentDirectory(self):
        ipi = __file__.split(os.sep)[:-1] 
        ipi = os.path.abspath(''.join(ipi[i] + os.sep for i in range(len(ipi))))
        ipi += os.sep if '/' in ipi else '\\'
        return ipi
    
    def getFileList(self, root):
        for path, subdirs, files in os.walk(root):
            return files
            
    def trySubfolders(self, root):
        for path, subdirs, files in os.walk(root):
            if not path == root:
                for file in files:
                    if self.multi == 'Y' or (self.multi == 'N' and self.fname in file):
                        self.findText(os.path.join(path, file))
    
    def getFolder(self):
        curr = folder = ''
        while not os.path.isdir(curr + folder):
            curr = self.currentDirectory() \
                if input('Is the folder to use a sub directory of \n' + 
                    self.currentDirectory() + '\nIf No you will need to ' +
                    'give the full path when prompted (Y/N): ').upper() == 'Y' \
                else ''       
            folder = input('Which folder do you want to work in? ')
            folder = folder + os.sep if folder != '' else ''
            self.wd = os.path.abspath(curr + folder)
        self.subs = 'Y' if \
            input('Search subfolders (Y/N): ').upper() == 'Y' else 'N'
        if input('Do you want to search in A)ll files or just one F)ile name ' +
                 'pattern? ').upper() == 'A':
            self.multi = 'Y'
        else:
            self.multi = 'N'
            self.fname = input('Which file do you want to search in? ')
    
    def findText(self, file):
        try:
            with open(file) as f:
                contents = f.read()
                if (self.incl == 'Y' and self.string in contents) or (
                    self.incl == 'N' and self.string not in contents):
                    print(file)
                    self.found += [file]
                    if self.prn == 'Y':
                        print(contents)
                        print()
        except Exception as e:
            if self.vbose == 'Y': print('Unable to work with: ', file)
            else: pass
            
    def foundFiles(self):
        return self.found
    
    def editFile(self):
        if sys.platform[:3] == 'win':
            app = {
                'wing': '"C:\\Program Files (x86)\\Wing IDE 101 6.1\\bin\\wing-101.exe" ',
                'Idle 3.6': '"C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\Python36_64\pythonw.exe" "C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\Lib\\idlelib\\idle.pyw" ',
                'notepad': 'notepad.exe ',
                'notepad++': '"C:\\Program Files (x86)\\Notepad++\\notepad++.exe" '
                }
        else:
            app = {
                'Idle 3.6': 'Idle3.6 ',
                'emacs': 'emacs ',
                'GVim': 'gvim '
                }
        print()
        whichApp = input('%sWhich app would you like to use to edit the file: ' %
                         ''.join(x + '\n' for x in app.keys()))
        print()
        try:
            whichFile = int(input('%s\nPlease give the number of the file you wish to edit: ' % 
                              ''.join(str(i) + ')' + self.found[i].split(os.sep)[-1] 
                              + '; ' for i in range(len(self.found)))))
            if whichApp in app and self.found[whichFile] in self.found:
                p = subprocess.Popen(app[whichApp] + self.found[whichFile], 
                                     stdin=subprocess.PIPE, stdout=subprocess.PIPE, 
                                     shell=True)
                p_status = p.wait()
        except: pass
        print()
        self.query()
            
    
    def executeFile(self):
        try:
            whichFile = int(input('%s\nPlease give the number of the file you wish to run: ' % 
                                  ''.join(str(i) + ')' + self.found[i].split(os.sep)[-1] 
                                  + '; ' for i in range(len(self.found)))))
            if self.found[whichFile] in self.found:
                path = ''.join(x + os.sep for x in 
                               self.found[whichFile].split(os.sep)[:-1])
                os.chdir(path)
                p = subprocess.Popen(self.found[whichFile], stdin=subprocess.PIPE, 
                                     stdout=subprocess.PIPE, shell=True)
                print('%s'.replace('\\r', '') % p.communicate()[0].decode('utf-8'), end='')
                p_status = p.wait()
        except: pass
        print()
        self.query()
    
    def query(self):
        toDo = input('Do you want to E)dit or R)un a file: ').upper()
        if toDo == 'E': 
            srch.editFile()
        elif toDo == 'R':
            srch.executeFile()        

if __name__ == '__main__':
    if len(sys.argv) == 1:
        srch = ListFilesContaining()
        srch.interactive()
    elif sys.argv[1].lower() == '--i':
        srch = ListFilesContaining()
        srch.interactive()
    elif sys.argv[1].lower() in ('--h', '--help'):
        print("""
Usage: ListFilesContaining                                    (interactive mode)
       ListFilesContaining [--i/[--h/--help]]           (interactive/help modes)
       ListFilesContaining string incl
       ListFilesContaining string incl wd subs multi fname prn
           string: text to search for
           incl: look for files Y->containing, N->not containing     
       optional:           
           wd: root folder '.'->cwd, '..'->up a level, or full path  (.=defualt)
           subs: search subdirectories Y/N                           (Y=default)
           multi: Y->search all files, N->search file name pattern   (Y=default)
           fname: filename pattern
           prn: print files found Y/N                                (N=default)
           vbose: print file errors Y/N                              (N=default)
        """)
    else:
        srch = ListFilesContaining(sys.argv[1:] + [False]*(9-len(sys.argv)))
        srch.run()
    if srch:
        srch.query()
    input('Press any key to quit!')