#!/usr/bin/env python3

# Example 18-16
# Builds a test graph as a simple dictionary: each state is a dictionar key with 
# a list of keys of nodes it leads to (i.e., its arcs). It also defines a function 
# that is used to run a few searches in the graph
# Author: Mark Lutz
# Last modified: 

"dictionary based graph representation"

Graph = {'A':   ['B', 'E', 'G'],
         'B':   ['C'],                          # a directed, cyclic graph
         'C':   ['D', 'E'],                     # stored as a dictionary
         'D':   ['F'],                          #'key' leads-to [nodes]
         'E':   ['C', 'F', 'G'],
         'F':   [],
         'G':   ['A']}

def tests(searcher):                            # test searcher function
    print(searcher('E', 'D', Graph))            # find all paths from 'E' to 'D'
    for x in ['AG', 'GF', 'BA', 'DA']:
        print(x, searcher(x[0], x[1], Graph))