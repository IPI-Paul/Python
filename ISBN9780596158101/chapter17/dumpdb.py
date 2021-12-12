#!/usr/bin/env python3

# Example 17-10
# Allows us to display results as we go--it prints an entire table with either a 
# simple display (which could be parsed by other tools) or a formatted display 
# (generated with the dictionary-record utility we wrote earlier).
# Author: Mark Lutz
# Last modified: 

"""
display table contents as raw tuples,  or formatted with field names
command-line usage:dumpdb.py dbname? table? [-] (dash=formatted display)
"""

def showformat(recs, sept=('-' * 40)):
    print(len(recs), 'records')
    print(sept)
    for rec in recs:
        maxkey = max(len(key) for key in rec)               # max key len
        for key in rec:                                     # or: \t align
            print('%-*s => %s' % (maxkey, key, rec[key]))   # -ljust, *len
        print(sept)

def dumpdb(cursor, table, format=True):
    if not format:
        cursor.execute('select * from ' + table)
        while True:
            rec = cursor.fetchone()
            if not rec: break
            print(rec)
    else:
        from makedicts import makedicts
        recs = makedicts(cursor, 'select * from ' + table)
        showformat(recs)

if __name__ == '__main__':
    import sys
    path = '../sourceFiles/db/'
    dbname, format, table = '%sch17-dbase1' % path, False, 'people'
    cmdargs= sys.argv[1:]
    if '-' in cmdargs:                          # format if '-' in cmdline args
        format = True                           # dbname if other cmdline arg
        cmdargs.remove('-')
    if cmdargs: dbname = cmdargs.pop(0)
    if cmdargs: table = cmdargs[0]
    
    from loaddb import login
    conn, curs = login(dbname)
    dumpdb(curs, table, format)