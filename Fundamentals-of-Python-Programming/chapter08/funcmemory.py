# Listing 8.18
# Uses a global variable to keep track of the number of times it has been 
# invoked
# Author: Rick Halterman
# Last modified: 

count = 0 # A global count variable

def remember():
    global count
    count += 1 # Count this invocation
    print('Calling remember (#' + str(count) + ')')
    
print('Beginning program')
remember()
remember()
remember()
remember()
remember()
print('Ending program')