# Listing 14.9
# Exercises the DigitalStopwatch class
# Author: Rick Halterman
# Last modified: 

from digitalstopwatch import DigitalStopwatch
from time import sleep

dsw = DigitalStopwatch()
dsw.start()                 # Start the timer
sleep(140)                  # Do nothing for 2:20
dsw.stop()                  # Stop the timer
print(dsw.digital_time())   # Print elapsed time in digital format