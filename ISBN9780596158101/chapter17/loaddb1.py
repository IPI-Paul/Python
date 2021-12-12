#!/usr/bin/env python3

# Example 17-8
# Is a top-level script geared toward one particular case
# Author: Mark Lutz
# Last modified: 

"""
load table from comma-delimited text file; equivalent to this nonportable SQL:
load data local infile 'ch17-data.txt' into table people fields terminated by ','"
"""

import sqlite3
conn = sqlite3.connect('../sourceFiles/db/ch17-dbase1')
curs = conn.cursor()

file = open('../sourceFiles/text/ch17-data.txt')
rows = [line.rstrip().split(',') for line in file]
for rec in rows:
    curs.execute('insert into people values (?, ?, ?)', rec)

conn.commit()       # commit changes now, if db supports transactions
conn.close()        # close, __del__ call rollback if changes not committed yet 