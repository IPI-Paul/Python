#!/usr/bin/env python3

# Example 1-7
# Shows how to update a pickle file in a similar way to a manually formatted 
# file, except that Python is doing all the formatting work for us
# Author: Mark Lutz
# Last modified: 

import pickle
path = '../sourceFiles/pickle/ch01-'
dbfile = open(path + 'people-pickle', 'rb')
db = pickle.load(dbfile)
dbfile.close()

db['sue']['pay'] *= 1.10
db['tom']['name'] = 'Tom Tom'

dbfile = open(path + 'people-pickle', 'wb')
pickle.dump(db, dbfile)
dbfile.close()