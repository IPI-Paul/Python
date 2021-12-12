# Listing 14.19
# Establishes a Top class. Top allows us to build a cooperative multiple 
# inheritance hierachy that allows the various class constructors to accept 
# varied agruments
# Author: Rick Halterman
# Last modified: 

class Top(object):
    def __init__(self, **kwargs):
        pass    # Terminate the constructor
