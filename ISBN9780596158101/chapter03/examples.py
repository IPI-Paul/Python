#!/usr/bin/env python3

# Example
# All other examples from chapter03
# Author: Mark Lutz
# Last modified: 

import os, sys

def adder2():
    sum = 0
    while True:
        line = sys.stdin.readline()
        if not line: break
        sum += int(line)
    print(sum)

def adder3():
    sum = 0 
    for line in sys.stdin: sum += int(line)
    print(sum)

def adderSmall():
    print(sum(int(line) for line in sys.stdin))
    
def help():
    print('Available functions:', end=' ')
    for item in globals().keys():
        if '_' not in item and item not in ('os', 'sys', 'argv'):
            print(item, end=' ')

def hello_in():
    inp = input()
    open('../sourceFiles/text/ch03-hello-in.txt', 'w').write('Hello ' + inp + '\n')

def hello_out():
    print('Hello shell world')

def reader():
    print('Got this: "%s"' % input())
    data = sys.stdin.readline()[:-1]
    print('The meaning of life is', data, int(data) * 2)

def sorterSmall():
    for line in sorted(sys.stdin): print(line, end='')

def whereami():
    print('my os.getcwd =>', os.getcwd())           # show my cwd execution dir
    print('my sys.path =>', sys.path[:6])           # show first 6 import paths
    input()                                         # wait for keypress if clicked

def writer():
    print("Help! Help! I'm being repressed!")
    print(42)

def writer2():
    for data in (123, 0, 999, 42):
        print('%03d' % data)

from sys import argv
if len(argv) > 1 and argv[1] in dir():
    locals()[argv[1]]()