#!/usr/bin/env python3

# Example 17
# Various examples not modulised
# Author: Mark Lutz, Paul I Ighofose
# Last modified: 2019-04-13

import sqlite3

def connectSql(dbase):
    return sqlite3.connect(dbase)               # '../sourceFiles/db/ch17-dbase1'

def getCursor(dbase):
    conn = connectSql(dbase)
    return conn, conn.cursor()        

def createTable(curs, statement):
    # 'create table people (name char(30), job char(10), pay int(4))'
    tblcmd = statement 
    curs.execute(tblcmd)

def addRecords(curs, statement, rows):
    # 'insert into people values (?, ?, ?)', ('Bob', 'dev', 5000)
    curs.execute(statement, rows)
    curs.rowcount
    sqlite3.paramstyle

def executeMany(curs, statement, rows):
    curs.executemany(statement, rows)
    curs.rowcount

def insertIterate(curs, statement, rows):
    for row in rows:
        curs.execute(statement, row)

def importFlatFile(curs, filename):
    curs.execute('delete from people')          # empty table
    curs.execute('select * from people')
    curs.fetchall()
    file = open(filename)
    rows = [line.rstrip().split(',') for line in file]
    rows[0]
    for rec in rows:
        curs.execute('insert into people values (?, ?, ?)', rec)
    curs.execute('select * from people')
    for rec in curs.fetchall(): print(rec)

def selectSum(curs, job):
    print("SQL Summing statement")
    curs.execute("select sum(pay), avg(pay) from people where job = '%s'" % job)
    print(curs.fetchall())
    print()
    print("SQL fetchall and Python summing functions")
    curs.execute("select name, pay from people where job = '%s'" % job)
    result = curs.fetchall()
    print(result)
    tot = 0
    for (name, pay) in result: tot += pay
    print('total:', tot, 'average:', tot / len(result))
    print('\nUsing Python comprehensions and generator expressions')
    print(sum(rec[1] for rec in result))        # generator expr
    print(sum(rec[1] for rec in result) / len(result))
    print(max(rec[1] for rec in result))
    print('\nUsing Python advanced comprehensions')
    avg = sum(rec[1] for rec in result) / len(result)
    print([rec[0] for rec in result if rec[1] > avg])
    print([rec[0] for rec in result if rec[1] < avg])

def nestedQueries(curs, job):
    query = ("select name from people where job = '%s' and "
             "pay > (select avg(pay) from people where job = '%s')")
    curs.execute(query % (job, job))
    print(curs.fetchall())
    query = ("select name from people where job = '%s' and "
             "pay < (select avg(pay) from people where job = '%s')")
    curs.execute(query % (job, job))
    print(curs.fetchall())

def includeModule(curs, job):
    from makedicts import makedicts
    recs = makedicts(curs, "select * from people where job = '%s'" % job)
    print(len(recs), recs[0])
    print([rec['name'] for rec in recs])
    print(sum(rec['pay'] for rec in recs))
    avg = sum(rec['pay'] for rec in recs) /len(recs)
    print([rec['name'] for rec in recs if rec['pay'] > avg])
    print([rec['name'] for rec in recs if rec['pay'] >= avg])

def fetchAll(curs):
    curs.execute('select * from people')
    for rec in curs.fetchall(): print(rec)    

def selftest():
    dbase = '../sourceFiles/db/ch17-dbase1'
    createStatement = 'create table people (name char(30), job char(10), pay int(4))'
    insertStatement = 'insert into people values (?, ?, ?)'
    filename = '../sourceFiles/text/ch17-data.txt'
    rows1 = ('Bob', 'dev', 5000)
    rows2 = [ ('Sue', 'mus', '70000'), 
          ('Ann', 'mus', '60000')]
    rows3 = [['Tom', 'mgr', 100000],
            ['Kim', 'adm', 30000],
            ['pat', 'dev', 90000]]
    conn, curs = getCursor(dbase)
    def help():
        print("""
        ex1: Run the create table People statement
        ex2: Run the add single record statement
        ex3: Run the add multiple records statement
        ex4: Run the add multiple records by iteration statement
        ex5: Run the import flat file statement
        ex6: Run the fetch all records statement
        ex7: Run SQL summing statements and Python comprehensions and generator 
             expressions
        ex8: Run SQL advanced statements with nested queries versus Python 
             comprehensions
        ex9: Run SQL statement and call imported Python module to produce output
        h: Display help
        q: Quit
        """)
    ex = {
        'ex1': lambda: createTable(curs, createStatement),
        'ex2': lambda: addRecords(curs, insertStatement, rows1),
        'ex3': lambda: executeMany(curs, insertStatement, rows2),
        'ex4': lambda: insertIterate(curs, insertStatement, rows3),
        'ex5': lambda: importFlatFile(curs, filename),
        'ex6': lambda: fetchAll(curs),
        'ex7': lambda: selectSum(curs, input('Job: ') or 'devel'),
        'ex8': lambda: nestedQueries(curs, input('Job: ') or 'devel'),
        'ex9': lambda: includeModule(curs, input('Job: ') or 'devel'),
        'h': lambda: help()
        }
    while True:
        rn = input(
            'Please enter example number (e.g. ex1, h for help, or q to quit): ')
        if rn == 'q': break
        ex[rn]()
        
    conn.commit()    

if __name__ == '__main__': 
    selftest()