# Listing 7.21
# Attempts to control a loop with a double-precision floating-point number
# Author: Rick Halterman
# Last modified: 

def main():
    # Count to ten by tenths
    i = 0.0
    while i != 1.0:
        print("i =", i)
        i += 0.1
        if i > 1.2:
            print("Bad Code")
            break
            
main()