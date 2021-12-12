#!/usr/bin/env python3

# Example 1-6
# Shows how to access the pickled database after it has been created
# Author: Mark Lutz
# Last modified: 

import pickle 
# Use binary mode files in 3.X
path = '../sourceFiles/pickle/ch01-'
dbfile = open(path + 'people-pickle', 'rb') 
db = pickle.load(dbfile)
for key in db:
    print(key, '=>\n ', db[key])
print(db['sue']['name'])