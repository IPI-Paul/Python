# Listing 14.3
# Provides an example of ingeritance, defining the new class of our enhanced 
# stopwatch watch objects
# Author: Rick Halterman
# Last modified: 

from stopwatch import Stopwatch

class CountingStopwatch(Stopwatch):
    def __init__(self):
        # Allow base class to do its initialisation of the inherited instance 
        # variables
        super().__init__()
        # Set number of starts to zero
        self._count = 0
        
    def start(self):
        # Count this start message unless the watch is already running
        if not self._running:
            self._count += 1
        # let base class do its start code
        super().start()
        
    def reset(self):
        # Let bas class reset the inherited instance variables
        super().reset()
        # Reset new instance variable that the base class method does not know 
        # about
        self._count = 0
    
    def count(self):
        return self._count