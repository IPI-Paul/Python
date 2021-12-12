#!/usr/bin/env python3

# Example 1-11
# Shows how to store in-memory dicitionary objects in a shelve for permanent 
# keeping
# Author: Mark Lutz
# Last modified: 

from initdata import bob, sue
import shelve
path = '../sourceFiles/shelve/ch01-'
db = shelve.open(path + 'people-shelve')
db['bob'] = bob
db['sue'] = sue
db.close()