#!/usr/bin/env python3

# Example 1-19
# Reads the shelve and prints fields of its records
# Author: Mark Lutz
# Last modified: 

import shelve
path = '../sourceFiles/shelve/ch01-'
db = shelve.open(path + 'class-shelve')
for key in db:
    print(key, '=>\n ', db[key].name, db[key].pay)

bob = db['bob']
print(bob.lastName())
print(db['tom'].lastName())