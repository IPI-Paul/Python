#!/usr/bin/env python3

# Example by IPI-Paul.
# A class that allows the user to replace strings within files in a directory. 
# Uses binary mode 
# Author: Paul Ighofose
# Last modified: 2018-11-15

import os
from runtime_backup import backup, restoreBackup, removeBackup

class FileContentReplace:
    def __init__(self, args=[False]*9, txtFrom='', txtTo='', wd='.', subs='Y', 
                 multi='Y', fname='|', fpath='Y', prn='N', vbose='N'):
        self.txtFrom = txtFrom if not args[0] else args[0]
        self.txtTo = (txtTo if not args[1] else args[1])
        self.wd = os.path.abspath(wd if not args[2] else \
                                  args[2]).replace('"', '').replace("'", '') 
        self.subs = (subs if not args[3] else args[3]).upper()
        self.multi = (multi if not args[4] else args[4]).upper() 
        self.fname = fname if not args[5] else args[5]
        self.fpath = fpath if not args[6] else args[6]
        self.prn = (prn if not args[7] else args[7]).upper()
        self.vbose = (vbose if not args[8] else args[8]).upper()
    
    def interactive(self):
        self.getFolder()
        self.txtFrom = input('Please enter the text to find: ')
        self.txtTo = input('Please enter the replacement text: ')
        self.fpath = 'Y' if input('Do you want to replace file names' +
            ' (Y/N): ').upper() == 'Y' else 'N'
        self.prn = 'Y' if input('Do you want to print the contents' +
            ' (Y/N): ').upper() == 'Y' else 'N'
        self.vbose = 'Y' if input('Do you want to print file errors' +
            ' (Y/N): ').upper() == 'Y' else 'N'
        self.run()
    
    def confirm(self):
        confirm = len(self.txtFrom) != 0 and len(self.txtTo) != 0
        while confirm == False or len(self.txtFrom) == 0:
            if len(self.txtFrom) == 0:
                self.txtFrom = input('Please enter the text to find: ')
            if confirm == False and len(self.txtTo) == 0:
                confirm = True if input('Do you want to remove the text %s? ' %
                                        '(Y/N)').upper() == 'Y' else False
            if confirm == False and len(self.txtTo) == 0:
                self.txtTo = input('Please enter the replacement text: ')
                confirm = len(self.txtTo) != 0
        if confirm == False:
            self.confirm()
        
    def run(self):
        self.confirm()
        files = self.getFileList(self.wd)
        for file in files:
            if self.multi == 'Y' or (self.multi == 'N' and self.fname in file):
                self.replaceText(os.path.join(self.wd, file))
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
                        self.replaceText(os.path.join(path, file))
    
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
        if input('Do you want to replace text in A)ll files or just one F)ile' +
                 ' name pattern? ').upper() == 'A':
            self.multi = 'Y'
        else:
            self.multi = 'N'
            self.fname = input('Which file do you want to replace text in? ')
    
    def replaceText(self, filename):
        try:
            with open(filename, 'rb') as f:
                contents = f.read()
            if self.txtFrom in [contents, contents.decode()] or \
               self.txtFrom.encode() in contents:
                print('Replacing "%s" with "%s" in %s' % (self.txtFrom, 
                                                          self.txtTo, filename))
                contents = contents.replace(self.txtFrom.encode(), 
                                            self.txtTo.encode())
                backup(filename, silent=True)
                with open(filename , 'wb') as w:
                    # print(contents, file=w)
                    w.write(contents)
                if self.prn == 'Y':
                    print(contents)
                    print()
        except:
            if self.vbose == 'Y': 
                print('Unable to work with: ', filename)
                print(restoreBackup(filename))
            else: pass
        finally:
            removeBackup(filename, silent=True)
            
        if self.fpath == 'Y':
            if self.txtFrom in filename:
                print('Replacing "%s" with "%s" in %s file name' % (self.txtFrom, 
                                                          self.txtTo, filename))                
                os.rename(filename, filename.replace(self.txtFrom, self.txtTo))
        
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        FileContentReplace().interactive()
    elif sys.argv[1].lower() == '--i':
        FileContentReplace().interactive()
    elif sys.argv[1].lower() in ('--h', '--help'):
        print("""
Usage: FileContentReplace                                     (interactive mode)
       FileContentReplace [--i/[--h/--help]]            (interactive/help modes)
       FileContentReplace txtFrom txtTo
       FileContentReplace txtFrom txtTo wd subs multi fname fpath prn vbose
           txtFrom: text to search for
           txtTo: look for files Y->containing, N->not containing     
       optional:           
           wd: root folder '.'->cwd, '..'->up a level, or full path  (.=defualt)
           subs: search subdirectories Y/N                           (Y=default)
           multi: Y->search all files, N->search file name pattern   (Y=default)
           fname: filename pattern
           fpath: also change filenames with text to search for Y/N  (Y=default)
           prn: print files found Y/N                                (N=default)
           vbose: print file errors Y/N                              (N=default)
        """)
    else:
        srch = FileContentReplace(sys.argv[1:] + [False]*(10-len(sys.argv)))
        srch.run()
    input('Press any key to close')