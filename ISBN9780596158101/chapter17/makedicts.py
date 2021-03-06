#!/usr/bin/env python3

# Example 17-4
# Makes the Person class from previous section in to a utility module. A reusable
# module that knows how to translate the result of a query fro row tuples to row 
# dictionaries
# Author: Mark Lutz
# Last modified: 

"""
convert list of row tuples to list of row dicts with field name keys
this is not a command-line utility: hardcoded self-test if run
"""

def makedicts(cursor, query, params=()):
    cursor.execute(query, params)
    colnames = [desc[0] for desc in cursor.description]
    rowdicts = [dict(zip(colnames, row)) for row in cursor.fetchall()]
    return rowdicts

if __name__ == '__main__':      # self test
    import sqlite3
    conn = sqlite3.connect('../sourceFiles/db/ch17-dbase1')
    cursor = conn.cursor()
    query = 'select name, pay from people where pay < ?'
    lowpay = makedicts(cursor, query, [70000])
    for rec in lowpay: print(rec)