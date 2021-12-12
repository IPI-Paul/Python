# Listing 7.20
# Adds two double-precision floating-point numberrs and checks for a given value
# Author: Rick Halterman
# Last modified: 

def main():
    x = 0.9
    x += 0.1
    if x == 1.0:
        print("OK")
    else:
        print("Not OK")
        
main()