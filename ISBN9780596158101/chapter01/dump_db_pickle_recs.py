#!/usr/bin/env python3

# Example 1-9
# Dumps the entire database by using the standard library's glob modul to do 
# filename expansion and thus collect all the files in this directory with a 
# .pkl extension
# Author: Mark Lutz
# Last modified: 

import pickle, glob
path = '../sourceFiles/pickle/ch01-'
for filename in glob.glob(path + '*.pkl'):  # for 'bob', 'sue', 'tom'
    recfile = open(filename, 'rb')
    record = pickle.load(recfile)
    print(filename, '=>\n ', record)

suefile = open(path + 'sue.pkl', 'rb')
print(pickle.load(suefile)['name'])     # fetch sue's name