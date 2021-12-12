#!/usr/bin/env python3

# Example 1-10
# Updates the database by fetching a record from it's file, changing it in 
# memory, and then witing it back to its pickle file
# Author: Mark Lutz
# Last modified: 

import pickle 
path = '../sourceFiles/pickle/ch01-'
suefile = open(path + 'sue.pkl', 'rb')
sue = pickle.load(suefile)
suefile.close()
sue['pay'] *= 1.10
suefile = open(path + 'sue.pkl', 'wb')
pickle.dump(sue, suefile)
suefile.close()