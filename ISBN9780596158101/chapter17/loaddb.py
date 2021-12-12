#!/usr/bin/env python3

# Example 17-9
# Is a module and command-line script for loading Sql table data
# Author: Mark Lutz
# Last modified: 

"""
load table from comma-delimited text file: reusable/generalized version
Importable functions; command-line usage: loaddb.py dbfile? table?
"""

def login(dbfile):
    import sqlite3
    conn = sqlite3.connect(dbfile)          # create or open db file
    curs = conn.cursor()
    return conn, curs

def loaddb(curs, table, datafile, conn=None, verbose=True):
    file = open(datafile)                                 # x,x,x\nx,x,x\n
    rows = [line.rstrip().split(',') for line in file]  # [[x,x,x], [x,x,x]]
    rows = [str(tuple(rec)) for rec in rows]            # ["(x,x,x)", "(x,x,x)"]
    for recstr in rows:
        curs.execute('insert into ' + table + ' values ' + recstr)
    if conn: conn.commit()
    if verbose: print(len(rows), 'rows loaded')

if __name__ == '__main__':
    import sys
    path = '../sourceFiles/'
    parms = ('%sdb/ch17-dbase1' % path, '%stext/ch17-data.txt' % path, 'people')
    dbfile, datafile, table = parms
    if len(sys.argv) > 1: dbfile = sys.argv[1]
    if len(sys.argv) > 2: dbfile = sys.argv[2]
    if len(sys.argv) > 3: dbfile = sys.argv[3]
    conn, curs = login(dbfile)
    loaddb(curs, table, datafile, conn)
    from examples import fetchAll
    fetchAll(curs)