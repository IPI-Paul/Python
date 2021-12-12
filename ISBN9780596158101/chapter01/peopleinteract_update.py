#!/usr/bin/env python3

# Example 1-22
# Allows interactive updates to our class stored in a shelve. For an input key, 
# it inputs values for each field and either updates an existing record or creates
# a new object and stores it under the key
# Author: Mark Lutz
# Last modified: 

# interactive updates 
import shelve
from person import Person
fieldnames = ('name', 'age', 'job', 'pay')
path = '../sourceFiles/shelve/ch01-'

db = shelve.open(path + 'class-shelve')
while True:
    key = input('\nKey? => ')
    if not key: break
    if key in db:
        record = db[key]                    # update existing record
    else:                                   # or make/store new rec
        record = Person(name='?', age='?')  # eval: quote strings
    for field in fieldnames:
        currval = getattr(record, field)
        newtext = input('\t[%s]=%s\n\t\tnew?=>' % (field, currval))
        if newtext:
            if not ('__import__' in newtext and 'system' in newtext):
                setattr(record, field, eval(newtext))
    db[key] = record
db.close()