#!/usr/bin/env python3

# Example 17-12
# Deletes all rows in a table, instead of dropping and re-creating them entirely
# Author: Mark Lutz
# Last modified: 

"""
delete all rows in table, but don't drop the table or database it is in
usage: cleardb.py dbname? tablename?
"""

import sys
if input('Are you sure? ').lower() not in ('y', 'yes'):
    sys.exit()

path = '../sourceFiles/db/'
dbname = sys.argv[1] if len(sys.argv) > 1 else '%sch17-dbase1' % path
table = sys.argv[2] if len(sys.argv) > 2 else 'people'

from loaddb import login
conn, curs = login(dbname)
curs.execute('delete from ' + table)
# print(rurs.rowcount, 'records deleted')       # conn closed by its __del__
conn.commit()                                   # else rows not really deleted