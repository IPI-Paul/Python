# Listing 14.8
# Is derived from Stopwatch with a new method that returns a string containing 
# the digital representation of the time. similar to the way the graphical 
# program in Listing 14.5 displays the elapsed time
# Author: Rick Halterman
# Last modified: 

from stopwatch import Stopwatch

class DigitalStopwatch(Stopwatch):
    def digital_time(self):
        """
        Returns a string representation of the elapsed time in hours : minutes :
        seceonds
        """
        # Compute time in hours , minutes, and seconds
        seconds = round(self.elapsed())
        hours = seconds // 3600 # Compute total hours
        seconds %= 3600         # Update seconds remaining
        minutes = seconds // 60 # Compute minutes
        seconds %= 60           # Update seconds remiaining
        # Each digit occupies two spaces; pad wioth leading zeros, if necessary
        return '{0:0>2}:{1:0>2}:{2:0>2}'.format(hours, minutes, seconds)