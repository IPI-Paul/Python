#!/usr/bin/env python3

# Example 1-8
# Stores each record in its own flat file, using each record's original key as 
# its filename with a .pkl appended (it creates the files bob.pkl, sue.pkl, and
# tom.pkl in the current working directory)
# Author: Mark Lutz
# Last modified: 

from initdata import bob, sue, tom
import pickle
path = '../sourceFiles/pickle/ch01-'
for (key, record) in [('bob', bob), ('tom', tom), ('sue', sue)]:
    recfile = open(path + key + '.pkl', 'wb')
    pickle.dump(record, recfile)
    recfile.close()