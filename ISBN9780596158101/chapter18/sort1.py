#!/usr/bin/env python3

# Example 18-25
# Defines a simple sort routine in Python, which orders a list of objects on a 
# field
# Author: Mark Lutz
# Last modified: 

def sort(list, field):
    res = []                                    # always returns a list
    for x in list:
        i = 0
        for y in res:
            if x[field] <= y[field]: break      # list node goes here?
            i += 1
        res[i:i] = [x]                          # insert in result slot
    return res

if __name__ == '__main__':
    table = [{'name': 'john', 'age': 25}, {'name':'doe', 'age': 32}]
    print(sort(table, 'name'))
    print(sort(table, 'age'))
    table = [('john', 25), ('doe', 32)]
    print(sort(table, 0))
    print(sort(table, 1))