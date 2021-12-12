#!/usr/bin/env python3

# Example 1-12
# Shows how to store in-memory dicitionary objects in a shelve for permanent 
# keeping
# Author: Mark Lutz
# Last modified: 

import shelve
path = '../sourceFiles/shelve/ch01-'
db = shelve.open(path + 'people-shelve')
for key in db:
    print(key, '=>\n ', db[key])
print(db['sue']['name'])
db.close()