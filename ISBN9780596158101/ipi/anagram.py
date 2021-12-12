#!/usr/bin/env python3

# Example by IPI-Paul. 
# Uses a for loop to permute all the differrent arrangements of the user input
# Author: Paul I Ighofose
# Last modified: 2019-04-22

import sqlite3

class Anagram:
    def __init__(self, dbase, tbl):
        self.conn, self.curs = self.getCursor(dbase)
        self.tbl = self.createTable(tbl)
        self.word = ''
        
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
        
    def perm(self, lst, begin):
        end = len(lst) - 1
        if begin == end:
            yield lst[:]
        else:
            for i in range(begin, end + 1):
                lst[begin], lst[i] = lst[i], lst[begin]
                yield from self.perm(lst, begin + 1)
                lst[begin], lst[i] = lst[i], lst[begin]
    
    def permutations(self, lst):
        yield from self.perm(lst, 0)
    
    def run(self, word):
        # Get the user input
        print('Running algorithm!')        
        lst = list(range(len(word))) 
        ix = 0
        for p in self.permutations(lst):
            words = ''
            for item in p:
                words += word[item].lower()
            self.addRecords(words)
            if ix == 700:
                self.conn.commit()
                ix = 0
            else:
                ix += 1
        self.conn.commit()
        print('Done')

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
            dbase = input('Database file with path: ') or '../sourceFiles/db/anagram.db'
            tbl = input('Table name: ') or 'Monday'
            word = input('Word to permute: ') or 'monday'
            string = input('String to search for (surround with %string%): ') or '%dynam%'
        func = Anagram(dbase, tbl)
        permutation = func.run(word)
        print(func.find(string))
        msg = 'Do you want to try another word (Y/N)? '
        if len(sys.argv) > 4 or input(msg).lower() != 'y':
            break