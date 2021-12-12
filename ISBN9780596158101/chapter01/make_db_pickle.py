#!/usr/bin/env python3

# Example 1-5
# Shows how to store records in a flat file, using pickle
# Author: Mark Lutz
# Last modified: 

from initdata import db
import pickle
# use binary mode files in 3.X
path = '../sourceFiles/pickle/ch01-'
dbfile = open(path + 'people-pickle', 'wb')
pickle.dump(db, dbfile)     # data is bytes, not str
dbfile.close()