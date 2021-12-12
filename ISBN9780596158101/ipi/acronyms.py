#!/usr/bin/env python3

# Example 18-22
# The functions defined shuffle sequences in a number of ways
# Author: Mark Lutz, Paul I Ighofose
# Last modified: 2019-04-21

"permutation-type operations for sequencies"

import sqlite3

class Acronyms:
    def __init__(self, dbase, tbl):
        self.conn, self.curs = self.getCursor(dbase)
        self.tbl = self.createTable(tbl)
        
        
    def connectSql(self, dbase):
        return sqlite3.connect(dbase)
    
    def getCursor(self, dbase):
        conn = self.connectSql(dbase)
        return conn, conn.cursor()        
    
    def createTable(self, tbl):
        try:
            tblcmd = 'drop table [%s]'  % tbl
            self.curs.execute(tblcmd)
        except:
            pass
        finally:
            tblcmd = 'create table [%s] (word char(30))'  % tbl
            self.curs.execute(tblcmd)
        return tbl
    
    def addRecords(self, rows):
        statement = "insert into [%s] values ('%s')" % (self.tbl, rows)
        self.curs.execute(statement)
    
    def permute(self, list):
        if not list:                                    # shuffle any sequence
            return [list]                               # empty sequence
        else:
            res = []
            for i in range(len(list)):
                rest = list[:i] + list[i+1:]            # delete current node
                for x in self.permute(rest):            # permute the others
                    res.append(list[i:i+1] + x)         # add node at front
            return res
    
    def run(self, list):
        res = self.permute(list)
        for itm in res:
            self.addRecords(itm.lower())
        self.conn.commit()
    
    def find(self, word):
        tblcmd = "select word from [%s] where word like '%s'" % (self.tbl, word)
        self.curs.execute(tblcmd)      
        return self.curs.fetchall()

if __name__ == '__main__':
    import sys
    while True:
        if len(sys.argv) > 4:
            dbase, tbl, word, string = sys.argv[1:]
        else:
            dbase = input('Database file with path: ') or '../sourceFiles/db/acronyms.db'
            tbl = input('Table name: ') or 'Monday'
            word = input('Word to permute: ') or 'monday'
            string = input('String to search for (surround with %string%): ') or '%dynam%'
        func = Acronyms(dbase, tbl)
        acronym = func.run(word)
        print(func.find(string))
        msg = 'Do you want to try another word (Y/N)? '
        if len(sys.argv) > 4 or input(msg).lower() != 'y':
            break