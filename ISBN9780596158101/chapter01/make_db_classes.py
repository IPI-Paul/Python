#!/usr/bin/env python3

# Example 1-18
# Shows how to store data from classes in a shelve-based storage medium
# Author: Mark Lutz
# Last modified: 

import shelve
from person import Person
from manager import Manager

bob = Person('Bob Smith', 42, 30000, 'software')
sue = Person('Sue Jones', 45, 40000, 'hardware')
tom = Manager('Tom Doe', 50, 50000)

path = '../sourceFiles/shelve/ch01-'
db = shelve.open(path + 'class-shelve')
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom
db.close()
