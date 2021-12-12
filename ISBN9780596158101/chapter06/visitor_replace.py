#!/usr/bin/env python3

# Example 6-20
# The ReplaceVisitor class is a SearchVisitor subclass that customizes the 
# visitfile method to globally replace any appearances of one string with another,
# in all text files at and below a root directory. It also collects the names of 
# all the files that were changed in a list just in cas you wish to go through 
# and verify verify the automatic edits applied (a text editor could be 
# automatically popped up on each changed file, for instance)
# Author: Mark Lutz
# Last modified: 

"""
Use: 'python ...\Tools\visitor_replace.py rootdir fromStr toStr'.
Does global search-and-replace in all files in a directory tree: replaces fromStr
with toStr in all text files; this is powerful but dangerous!! visitor_edit.py 
runs an editor for you to verify and make changes, and so is safer; use 
visitor_collect.py to simply collect matched files list; listonly mode here is 
similar to both SearchVisitor and CollectVisitor;
"""

import sys
from visitor import SearchVisitor, errors

class ReplaceVisitor(SearchVisitor):
    """
    Change fromStr to toStr in files at and below starDir; files changeds 
    available in obj.changed list after run
    """
    def __init__(self, fromStr, toStr, listOnly=False, trace=0, err={}):
        self.changed = []
        self.toStr = toStr
        self.listOnly = listOnly
        self.err = err
        SearchVisitor.__init__(self, fromStr, trace, err)
    
    def visitmatch(self, fname, text):
        try:
            self.changed.append(fname)
            if not self.listOnly:
                fromStr, toStr = self.context, self.toStr
                text = text.replace(fromStr, toStr)
                open(fname, 'w').write(text)
        except Exception as e:
                self.err = errors(self.err, 'visitmatch', e, sys.exc_info()[-1])
if __name__ == '__main__':
    err = {}
    use = """
Usage: visitor_replace.py rootDir fromStr toStr
    """
    listonly = input('List only (Y/N): ').upper() == 'Y'
    try:
        visitor = ReplaceVisitor(sys.argv[2], sys.argv[3], listonly, err=err)
        if listonly or input('Proceed with changes? ').upper() == 'Y':
            visitor.run(startDir=sys.argv[1])
            action = 'Changed' if not listonly else 'Found'
            print('Visited %d files' % visitor.fcount)
            print(action, '%d files: ' % len(visitor.changed))
            for fname in visitor.changed: print(fname)
    except IndexError as e:
        err = errors(err, 'main', e, sys.exc_info()[-1])
    except Exception as e:
        err = errors(visitor.err, 'main', e, sys.exc_info()[-1])

    print()
    for x in err:
        print(x + ': ' + err[x])
    if 'main' in err or 'visitmatch' in err: 
        print(use)    