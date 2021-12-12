#!/usr/bin/env python3

# Example 17-11
# Completely deletes and recreates the database, to rest it to an initial state
# Author: Mark Lutz
# Last modified: 

"""
physically delte and re-create database files 
usage: makedb.py dbname? tablename?
"""

import sys
if input('Are you sure? ').lower() not in ('y', 'yes'):
    sys.exit()

path = '../sourceFiles/db/'
dbname = (len(sys.argv) > 1 and sys.argv[1]) or '%sch17-dbase1' % path
table = (len(sys.argv) > 2 and sys.argv[2]) or 'people'

from loaddb import login
conn, curs = login(dbname)
try:
    curs.execute('drop table ' + table)
except:
    print('database table did not exist\n')

command = 'create table %s (name char(30), job char(10), pay int(4))' % table
curs.execute(command)
conn.commit()                   # commit may be optional here
print('made', dbname, table)