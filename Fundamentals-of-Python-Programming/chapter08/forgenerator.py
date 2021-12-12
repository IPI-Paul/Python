# Listing 8.20
# Shows that the for statement works naturally with the generator our gen 
# function produces
# Author: Rick Halterman
# Last modified: 

def gen():
    yield 3
    yield 'wow'
    yield -1
    yield 1.2
    
for i in gen():
    print(i)