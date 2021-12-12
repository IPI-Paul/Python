#!/usr/bin/env python3

# Example 17-13
# Provides a command-line tool that runs a query and prints its result table in 
# formatted style
# Author: Mark Lutz
# Last modified: 

"""
run a query string, display formatted result table
example: querydb.py dbase1 "se;ect name, job from people where pay > 50000"
"""

import sys
path = '../sourceFiles/db/'
database, querystr = path + 'ch17-dbase1', 'select * from people'
if len(sys.argv) > 1: dbase = sys.argv[1]
if len(sys.argv) > 2: querystr = sys.argv[2]

from makedicts import makedicts
from dumpdb import showformat
from loaddb import login

conn, curs = login(database)
rows = makedicts(curs, querystr)
showformat(rows)