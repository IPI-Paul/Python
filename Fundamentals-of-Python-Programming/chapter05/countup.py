# Listing 5.3
# Counts up from zero as long as the user wishes to do so
# Author: Rick Halterman
# Last modified: 

# Counts up from zero. The user continues the count by entering 'Y'. The user 
# discontinues the count by entering 'N'

count = 0       # The current count
entry = 'Y'     # Count to begin with

while entry != 'N' and entry != 'n':
    # Print the current value of count
    print(count)
    entry = input('Please enter "Y" to continue or "N" to quit: ')
    if entry == 'Y' or entry == 'y':
        count += 1      # Keep counting
    # Check for "bad" entry
    elif entry != 'N' and entry != 'n':
        print('"' + entry +'" is not a valid choice')
    # else must be 'N' or 'n'