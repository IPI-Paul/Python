#!/usr/bin/env python3

# Example 18-19
# Illustrates how classes can be used to model nodes in a network which may 
# contain content useful for more sophisticated searches. They may also participate 
# in inheritance hierarchies to acquire additional behaviours.
# Author: Mark Lutz
# Last modified: 

"build agraph with objects that know how to search"

class Graph:
    def __init__(self, label, extra=None):
        self.name = label                       # nodes=inst objects
        self.data = extra                       # graph=linked objs
        self.arcs = []
    
    def __repr__(self):
        return self.name
    
    def search(self, goal):
        Graph.solns = []
        self.generate([self], goal)
        Graph.solns.sort(key=lambda x: len(x))
        return Graph.solns
    
    def generate(self, path, goal):
        if self == goal:                            # class == tests addr
            Graph.solns.append(path)                # or self.solns: same
        else:
            for arc in self.arcs:
                if arc not in path:
                    arc.generate(path + [arc], goal)