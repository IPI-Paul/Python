#!/usr/bin/env python3

# Example 1-13
# Shows how to code shelve updates
# Author: Mark Lutz
# Last modified: 

from initdata import tom
import shelve
path = '../sourceFiles/shelve/ch01-'
db = shelve.open(path + 'people-shelve')
sue = db['sue']         # fetch sue
sue['pay'] *= 1.50
db['sue'] = sue         # update sue
db['tom'] = tom         # add a new record
db.close()