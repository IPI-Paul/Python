# Listing 14.17
# Defines the class CountingStopwatc2 that behaves identically to 
# CountingStopwatch, but it uses composition to reuse the functionality of 
# Stopwatch
# Author: Rick Halterman
# Last modified: 

from stopwatch import Stopwatch

class CountingStopwatch2:
    """
    This counting stopwatch uses composition instead of inheritance
    """
    def __init__(self):
        # Creates a stopwatch object to keep the time
        self.watch = Stopwatch()
        # Set number of starts to zero
        self._count = 0
    
    def start(self):
        # Count this start message unless the watch already is running
        if not self.watch._running:
            self._count += 1
        # Delegate other work to the stopwatch object
        self.watch.start()
    
    def stop(self):
        # Delegate to stopwatch object
        self.watch.stop()
    
    def reset(self):
        # let the stopwatch object reset the time
        watch.reset()
        # Reset the count
        sel._count = 0
    
    def elapsed(self):
        # Delegate to stopwatch object
        return self.watch.elapsed()
    
    def count(self):
        return self._count