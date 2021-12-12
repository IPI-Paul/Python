# Listing 5.33
# Guesses the square root of a number. Squares the guess to see how close it is 
# to the original number and if close enough stops. If not, makes a new guess
# Author: Rick Halterman
# Last modified: 
# File computesquareroot.py

# Get value from the user
val = float(input('Enter a number: '))
# Compute a provisional square root
root = 1.0

# How far off is our provisional root?
diff = root * root - val

# Loop until the provisional root is close enough to the actual root
while diff > 0.00000001 or diff < -0.00000001:
    print(root, 'squared is', root * root) # Report how we are doing
    root = (root + val / root) / 2         # Compute new provisional root
    diff = root * root - val               # How bad is our current approximation
    
# Report approximate square root
print('Square root of', val, '=', root)