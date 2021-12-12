#!/usr/bin/env python3

# Example 1-3
# Reloads the database from a file each time it is run
# Author: Mark Lutz
# Last modified: 

from make_db_file import loadDbase
db = loadDbase()
for key in db:
    print(key, '=>\n', db[key])
print(db['sue']['name'])