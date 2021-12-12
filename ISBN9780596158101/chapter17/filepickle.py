#!/usr/bin/env python3

# Example 17-1
# Wraps pickling and unpickling calls in functions that also open the files where 
# serialized form of the object is stored.
# Author: Mark Lutz
# Last modified: 

"""
Pickle to/from flat file utilities
"""
import pickle

def saveDbase(filename, object):
    "save object to file"
    file = open(filename, 'wb')
    pickle.dump(object, file)       # pickle to binary file
    file.close()                    # any file-like object will do

def loadDbase(filename):
    'load object from file'
    file = open(filename, 'rb')
    object = pickle.load(file)      # unpickle from binary file
    file.close()                    # re-creates object in memory
    return object