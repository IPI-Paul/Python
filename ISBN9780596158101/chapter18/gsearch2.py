#!/usr/bin/env python3

# Example 18-18
# Implements search algorithms. Uses explicit stack of paths to be expanded using
# tuple-tree stack representation.
# Author: Mark Lutz
# Last modified: 

"graph search, using paths stack instead of recursion"

def search(start, goal, graph):
    solns = generate(([start], []), goal, graph)
    solns.sort(key=lambda x: len(x))
    return solns

def generate(paths, goal, graph):                       # return solns list
    solns = []                                          # use tuple-stack
    while paths:
        front, paths = paths                            # pop the top path
        state = front[-1]
        if state == goal:
            solns.append(front)                         # goal on this path
        else:
            for arc in graph[state]:                    # add all extensions
                if arc not in front:
                    paths = (front + [arc]), paths
    return solns

if __name__ == '__main__':
    import gtestfunc
    gtestfunc.tests(search)