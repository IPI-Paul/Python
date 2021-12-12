#!/usr/bin/env python3

# Example 18-21
# Builds a test graph using linked instances of the Graph class
# Author: Mark Lutz
# Last modified: 

from graph import Graph

S = Graph('s')
P = Graph('p')              # a graph of spam
A = Graph('a')              # make node objects
M = Graph('m')

S.arcs = [P, M]             # S leads to P and M
P.arcs = [S, M, A]          # arcs: embedded objects
A.arcs = [M]
print(S.search(M))          # find all paths from S to M