#!/usr/bin/env python3

# Example 19-2
# Builds a rule that first splits around the if, then around the then, and 
# finally around rule giving three substrings that were sepearted by keywords.
# Test and conclusion substrings are split around "," first and spaces last. 
# join is used later to convert back (unparse) to the original string for display
# Author: Mark Lutz
# Last modified: 

def internal_rule(string):
    i = string.split(' if ')
    t = i[1]. split(' then ')
    r = i[0].split('rule ')
    return {'rule': r[1].strip(), 'if': internal(t[0]), 'then': internal(t[1])}

def external_rule(rule):
    return ('rule '     + rule['rule']           +
            ' if '      + external(rule['if'])   +
            ' then '    + external(rule['then']) + '.')

def internal(conjunct):
    res = []                                        # 'a b, c d'
    for clause in conjunct.split(','):              # -> [' b', 'c d']
        res.append(clause.split())                  # -> [['a', 'b'], ['c', 'd']]
    return res

def external(conjunct):
    strs = []
    for clause in conjunct:                         # [['a', 'b'], ['c', 'd']]
        strs.append(' '.join(clause))               # -> ['a b', 'c d']
    return ', '.join(strs)                          # -> 'a b, c d'