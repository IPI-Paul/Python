#!/usr/bin/env python3

# Example 6-9
# Shows some of the more commonly used system tools in action. It implements a 
# simple regression test sytem for Python scritps
# Author: Mark Lutz
# Last modified: 

"""
################################################################################
Test a directory of Python scripts, passing command-line arguments, piping in 
stdin, and capturing stdout, stderr, and exit status to detect failures and 
regressions from prior run outputs. The subprocess module spawns and controls 
streams ( much like os.popen3 in Python 2.X), and i scross-platform. Streams are 
always binary bytes in subprocess. Test inputs, args, outputs, and errors map to 
files in subdirectories.

This is a command-line script, using command-line arguments for optional test 
directory name, and force-generation flag. While we could package it as a 
callable function, the fact that its results are messages and output files makes 
a call/return model less useful.

Suggested enhancement: could be extended to allow multiple sets of command-line 
arguments and/or inputs per test script, to run a script multiple times (glob 
for multiple '.in*' files in inputs?). Might also seem simpler to store all test 
files in same directory with different extensions, but this could grow large 
over time.Could also save both stderr and stdout to Errors on failures, but I 
prefer to have expected/actual output in outputs on regressions.
################################################################################
"""

import os, sys, glob, time
from subprocess import Popen, PIPE

# configuration args
testdir = sys.argv[1] if len(sys.argv) > 1 else '../test'
forcegen = len(sys.argv) > 2
print('Start tester:', time.asctime())
print('in', os.path.abspath(testdir))

def verbose(*args):
    print('-' * 80)
    for arg in args: print(arg)

def quiet(*args): pass
trace = quiet

# glob scripts to be tested 
testpath = os.path.join(testdir, 'Scripts', '*.py')
testfiles = glob.glob(testpath)
testfiles.sort()
trace(os.getcwd(), *testfiles)

numfail = 0
for testpath in testfiles:                      # run all tests in dir
    testname = os.path.basename(testpath)       # strip directory path
    
    # get input and args
    infile = testname.replace('.py', '.in')
    inpath = os.path.join(testdir, 'Inputs', infile)
    indata = open(inpath, 'rb').read() if os.path.exists(inpath) else b''
    
    argfile = testname.replace('.py', '.args')
    argpath = os.path.join(testdir, 'Args', argfile)
    argdata = open(argpath).read() if os.path.exists(argpath) else ''
    
    # locate output and error, scrub prior results
    outfile = testname.replace('.py', '.out')
    outpath = os.path.join(testdir,'Outputs', outfile)
    outpathbad = outpath + '.bad'
    if os.path.exists(outpathbad): os.remove(outpathbad)
    
    errfile = testname.replace('.py', '.err')
    errpath = os.path.join(testdir, 'Errors', errfile)
    if os.path.exists(errpath): os.remove(errpath)
    
    # run test with redirected streams
    pypath = sys.executable
    command = '"%s" %s %s' % (pypath, testpath, argdata)
    trace(command, indata)
    
    process = Popen(command, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    process.stdin.write(indata)
    process.stdin.close()
    outdata = process.stdout.read()
    errdata = process.stderr.read()             # data are bytes
    exitstatus = process.wait()                 # requires binary files
    trace(outdata, errdata, exitstatus)
    
    # analyse results
    if exitstatus != 0:
        print('Error status:', testname, exitstatus)    # status and/or stderr
    if errdata:
        print('Error status:', testname, errpath)       # save error text
        open(errpath, 'wb').write(errdata)
    if exitstatus or errdata:                           # consider both failure
        numfail += 1                                    # can get status+stderr
        open(outpathbad, 'wb').write(outdata)           # save output to view
    elif not os.path.exists(outpath) or forcegen:
        print('generating:', outpath)
        open(outpath, 'wb').write(outdata)
    else:
        priorout = open(outpath, 'rb').read()           # or compare to prior
        if priorout == outdata:
            print('passed:', testname)
        else:
            numfail += 1
            print('FAILED output:', testname, outpathbad)
            open(outpathbad, 'wb').write(outdata)

print('Finished:', time.asctime())
print('%s tests were run, %s tests failed.' % (len(testfiles), numfail))