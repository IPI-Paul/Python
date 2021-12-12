# Listing 5.10
# Uses a while loop and user input to run an indefinite loop
# Author: Rick Halterman
# Last modified: 

done = False                # Enter the loop at least once
while not done:
    # Get value from user
    entry = int(input('Please enter an integer or 999 to quit: '))  
    if entry == 999:        # Did user provide the magic number?
        done = True        # If so, get out
    else:
        print(entry)        # If not, print it and continue