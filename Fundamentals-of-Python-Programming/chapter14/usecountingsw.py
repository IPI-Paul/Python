# Listing 14.4
# Provides some sample client code that uses the CountingStopwatch class
# Author: Rick Halterman
# Last modified: 

from time import sleep

watch = int(input('Use 1)CountingStopwatch 2)CountingStopwatch2: '))
if watch == 1:
    from countingstopwatch import CountingStopwatch
    timer = CountingStopwatch()
elif watch == 2:
    from countingstopwatch2 import CountingStopwatch2
    timer = CountingStopwatch2()    
else:
    print('Invalid selection')
    import sys
    sys.exit(1)
timer.start()
sleep(10)   # Pause program for 10 seconds
timer.stop()
print('Time:', timer.elapsed(), ' Number:', timer.count())

timer.start()
sleep(5)    # Pause program for 5 seconds
timer.stop()
print('Time:', timer.elapsed(), ' Number:', timer.count())

timer.start()
sleep(20)    # Pause program for 20 seconds
timer.stop()
print('Time:', timer.elapsed(), ' Number:', timer.count())