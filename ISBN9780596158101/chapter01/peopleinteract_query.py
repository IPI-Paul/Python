#!/usr/bin/env python3

# Example 1-21
# Implements a simple interactive loop that allows a user to query multiple 
# record objects in the shelve by key
# Author: Mark Lutz
# Last modified: 

# interactive queries
import shelve
path = '../sourceFiles/shelve/ch01-'
fieldnames = ('name', 'age', 'job', 'pay')
maxfield = max(len(f) for f in fieldnames)
db = shelve.open(path + 'class-shelve')

while True:
    key = input('\nKey? => ')       # key or empty line, exc at eof
    if not key: break
    try:
        record = db[key]            # fetch by key, show in console
    except:
        print('No such key "%s"!' % key)
    else:
        for field in fieldnames:
            print(field.ljust(maxfield), '=>', getattr(record, field))