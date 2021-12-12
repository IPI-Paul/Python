#!/usr/bin/env python3

# Example 1-20
# Database updates are as simple as before (compare this to Example 1-13, but 
# dicitionary keys become attributes of instance objects, and updates are 
# implemented by class method calls instead of hardcoded logic
# Author: Mark Lutz
# Last modified: 

import shelve

path = '../sourceFiles/shelve/ch01-'
db = shelve.open(path + 'class-shelve')

sue = db['sue']
sue.giveRaise(.25)
db['sue'] = sue

tom = db['tom']
tom.giveRaise(.20)
db['tom'] = tom
db.close()