#!/usr/bin/env python3

# Example 6-19
# Defines a new EditVisitor class that simply customizes the visitmatch method 
# of the SearchVisitor class to open a text editor on the matched file
# Author: Mark Lutz
# Last modified: 

"""
Use: 'python ...\Tools\visitor_edit.py string rootdir?'.
Add auto-editor startup to SearchVisitor in an external subclass component;
Automatically pops up an editor on each file containing string as it traverses; 
can also use editor='edit' or 'notepad' on Windows; to use texteditor from later 
in the book, try r'python GUI\TextEditor\textEditor.py'; could also send a search
command to go to the first match on start in some editors;
"""

import os, sys
from visitor import SearchVisitor, errors

class EditVisitor(SearchVisitor):
    """
    edit files at and below starDir having string
    """
    cygwinPath = 'c:\cygwin' if os.path.exists('c:\\cygwin') else 'c:\\cygwin64'
    
    editor = r'%s\bin\vim.exe' % cygwinPath         # ymmv!

    if sys.platform[:3] == 'win' and not os.path.exists(editor):
        editor = 'notepad.exe'
    if sys.platform[:3] == 'cyg' and os.path.exists(editor):
        editor = '/bin/vim.exe'
    elif not os.path.exists(editor):
        editor = 'edit.exe'
    
    def visitmatch(self, fpathname, text):
        os.system('%s %s' % (self.editor, fpathname))

if __name__ == '__main__':
    err = {}
    use = """
Usage: visitor_edit.py string rootdir
"""
    try:
        visitor = EditVisitor(sys.argv[1], err=err)
        visitor.run('.' if len(sys.argv) < 3 else sys.argv[2])
        print('Edited %d files, visited %d' % (visitor.scount, visitor.fcount))
    except IndexError as e:
        err = errors(err, 'main', e, sys.exc_info()[-1])
    except Exception as e:
        err = errors(visitor.err, 'main', e, sys.exc_info()[-1])

    print()
    for x in err:
        print(x + ': ' + err[x])
    if 'main' in err: 
        print(use)    