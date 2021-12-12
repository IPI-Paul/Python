#!/usr/bin/env python3

# Example 1-4
# Makes changes by loading, updating, and sorting again
# Author: Mark Lutz
# Last modified: 

from make_db_file import loadDbase, storeDbase
db = loadDbase()
db['sue']['pay'] *= 1.10
db['tom']['name'] = 'Tom Tom'
storeDbase(db)