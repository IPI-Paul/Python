#!/usr/bin/env python3

# Example 6-18
# Exports a general FileVisitor class that mostly just wraps os.walk for easier
# use and extension, as well as a generic SearchVisitor class that generalizes 
# the notion of directory searches
# Author: Mark Lutz, Paul I Ighofose
# Last modified: 2018-11-10

"""
################################################################################
Tes: 'python ...\Tools\visitor.py dir testmask [string]'. Uses classes and 
subclasses to wrap some of the details of os.walk call usage to walk and search;
testmask is an integer bitmask with 1 bit per available self-test; see also:
visitor_*/.py subclasses use cases; frameworks should  generally use__X pseudo 
private names, but all names here are exported for use in subclasses and clients;
redefine reset to support multiple independent walks that require subclass updates;
################################################################################
"""

import os, sys

class FileVisitor:
    """
    Visits all nondirectory files below startDir (default '.'); 
    override visit* methods to proivide custom file/dir handlers;
    context arg/attribute is optional subclass-specific state;
    trace switch: 0 is silent, 1 is directories, 2 adds files
    """
    def __init__(self, context=None, trace=2, err={}):
        self.fcount = 0 
        self.dcount = 0
        self.context = context
        self.trace = trace
        self.err = err
    
    def run(self, startDir=os.curdir, reset=True):
        if reset: self.reset()
        try:
            for (thisDir, dirsHere, filesHere) in os.walk(startDir):
                self.visitdir(thisDir)
                for fname in filesHere:                     # for non-dir files
                    fpath = os.path.join(thisDir, fname)    # fnames have no path
                    self.visitfile(fpath)
        except Exception as e:
            self.err = errors(self.err, startDir, e, sys.exc_info()[-1])
                
    def reset(self):                                    # to reuse walker
        self.fcount = self.dcount = 0                   # for independent walks
    
    def visitdir(self, dirpath):                        # called for each dir
        self.dcount += 1                                # override or extend me
        if self.trace > 0: print(dirpath, '...')
    
    def visitfile(self, filepath):                      # called for each file
        self.fcount += 1                                # override or extend me
        if self.trace > 1: print(self.fcount, '=>', filepath)

class SearchVisitor(FileVisitor):
    """
    Search files at and below startDir for a string;
    subclass: redefine visitmatch, extension lists, candidate as needed;  
    subclasses can use testexts to specify file types to search (but can also 
    redefine candidate to use mimetypes for text content: see ahead)
    """
    
    skipexts = []
    # search these exts
    testexts = ['.txt', '.py', '.pyw', '.htm', '.html', '.c', '.cpp', '.h', 'java']
    # skipexts = ['.gif', '.jpg', '.pyc', '.o', '.a', '.exe'] # or skip these exts
    
    def __init__(self, searchkey, trace=2, err={}):
        FileVisitor.__init__(self, searchkey, trace, err)
        self.err = err
        self.scount = 0
    
    def reset(self):                                    # on independent walks
        self.scount = 0
    
    def candidate(self, fname):                         # redef for mimetypes
        ext = os.path.splitext(fname)[1]
        if self.testexts:
            return ext in self.testexts                 # in test list
        else:                                           # or not in skip list
            return ext not in self.skipexts
    
    def visitfile(self, fname):                         # test for a match
        try:
            FileVisitor.visitfile(self, fname)
            if not self.candidate(fname):
                if self.trace > 0: print('Skipping', fname)
            else:
                text = open(fname).read()                   # 'rb' if undecodable
                if self.context in text:                    # or text.find() != -1
                    self.visitmatch(fname, text)
                    self.scount += 1
        except Exception as e: 
            self.err = errors(self.err, fname, e, sys.exc_info()[-1])
    
    def visitmatch(self, fname, text):                  # process a match
        print('%s has %s' % (fname, self.context))      # override me lower

def errors(err, caller, errType, func):
    from traceback import extract_tb
    errName = type(errType).__name__ 
    erm = '\nFailed due to '
    if errName == 'IndexError': 
        erm += 'a missing command-line parameter'  
    elif errName == 'UnicodeDecodeError': 
        erm = '\n' + erm + 'unable to decode and read file'       
    else: 
        erm += errName + ' ' + str(errType) 
    function = extract_tb(func, 1)[0]
    erm += '\nOn line no. %s when calling:\n%s' % (function[1], function[3])
    if caller in err:
        err[caller] += erm
    else:
        err[caller] = erm
    return err

if __name__ == '__main__':
    err = {}
    # self-test logic
    dolist = 1
    dosearch = 2    # 3=do list and search
    donext = 4      # when next test added        
    use = """
Usage: visitor.py 1 dir
       visitor.py [2/3] dir string
       visitor.py 4 dir (not yet Kato!)       
"""
        
    def selftest(testmask):
        global err
        try:                
            if testmask & dolist:
                visitor = FileVisitor(trace=2, err=err)
                visitor.run(sys.argv[2])
                print()
                print('Visited %d files and %d dirs' % (visitor.fcount, visitor.dcount))
        except Exception as e:
            err = errors(visitor.err, 'dolist', e, sys.exc_info()[-1])
    
        print()
        try:                
            if testmask & dosearch:
                visitor = SearchVisitor(sys.argv[3], trace=0, err=err)
                visitor.run(sys.argv[2])
                print()
                print('Found %d files, Visited %d ' % (visitor.scount, visitor.fcount))
        except IndexError as e:
            err = errors(err, 'dosearch', e, sys.exc_info()[-1])
        except Exception as e:
            err = errors(visitor.err, 'dosearch', e, sys.exc_info()[-1])
        
    try:
        selftest(int(sys.argv[1]))      # e.g., 3 = dolist | dosearch
    except Exception as e:
        err = errors(err, 'main', e, sys.exc_info()[-1])

    print()
    for x in err:
        print(x + ': ' + err[x])
    if 'main' in err or 'dolist' in err or 'dosearch' in err or 'donext' in err: 
        print(use)