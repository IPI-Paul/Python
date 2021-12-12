#!/usr/bin/env python3

# Example 6-21
# Extends FileVisitor to count the number of lines in program source code files 
# of various types throughout an entire tree.
# Author: Mark Lutz
# Last modified: 

"""
Count lines among all program source files in a tree named on the command line,
and report totals grouped by file types (extension). A Simple SLOC (source lines 
if code) metric: skip blank and comment lines if desired
"""

import sys, pprint, os
from visitor import FileVisitor, errors

class LinesByType(FileVisitor):
    srcExts = []            # define in subclass
    
    def __init__(self, trace=1, err={}):
        FileVisitor.__init__(self, trace=trace, err=err)
        self.srcLines = self.srcFiles = 0
        self.extSums = {ext: dict(files=0, lines=0) for ext in self.srcExts}
        self.err = err
    
    def visitsource(self, fpath, ext):
        try:
            if self.trace > 0: print(os.path.basename(fpath))
            lines = len(open(fpath, 'rb').readlines())
            self.srcFiles += 1
            self.srcLines += lines
            self.extSums[ext]['files'] += 1
            self.extSums[ext]['lines'] += lines
        except Exception as e:
            self.err = errors(self.err, fpath, e, sys.exc_info()[-1])
    
    def visitfile(self, filepath):
        try:
            FileVisitor.visitfile(self, filepath)
            for ext in self.srcExts:
                if filepath.endswith(ext):
                    self.visitsource(filepath, ext)
                    break
        except Exception as e:
            self.err = errors(self.err, filepath, e, sys.exc_info()[-1])

class PyLines(LinesByType):
    srcExts = ['.py', '.pyw']       # just python files

class SourceLines(LinesByType):
    srcExts = ['.py', '.pyw', '.cgi', '.htm', '.html', '.c', '.cxx', '.cpp', 
               '.h', '.i', '.java']

if __name__ == '__main__':
    err = {}
    use = """
Usage: visitor_sloc.py rootDir    
    """
    try:
        walker = SourceLines(err=err)
        walker.run(sys.argv[1])
        print('Visited %d files and %d dirs' % (walker.fcount, walker.dcount))
        print('-' * 80)
        print('By Types:')
        pprint.pprint(walker.extSums)
        
        print('\nCheck sums:', end=' ')
        print(sum(x['files'] for x in walker.extSums.values()), end=' ')
        print(sum(x['lines'] for x in walker.extSums.values()))
    except IndexError as e:
        err = errors(err, 'main', e, sys.exc_info()[-1])
    except Exception as e:
        err = errors(walker.err, 'SourceLines', e, sys.exc_info()[-1])
        
    try:        
        print('\nPython only walk:')
        walker = PyLines(trace=0, err=err)
        walker.run(sys.argv[1])
        pprint.pprint(walker.extSums)
    except IndexError as e:
        err = errors(err, 'main', e, sys.exc_info()[-1])
    except Exception as e:
        err = errors(walker.err, 'Pylines', e, sys.exc_info()[-1])

    print()
    for x in err:
        print(x + ': ' + err[x])
    if 'main' in err or 'SourceLines' in err or 'Pylines' in err: 
        print(use)        