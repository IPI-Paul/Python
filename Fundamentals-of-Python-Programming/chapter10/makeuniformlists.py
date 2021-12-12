# Listing 10.10
# Builds several lists using the * list multiplication operator.
# Author: Rick Halterman
# Last modified: 

def main():
    a = [0] * 10
    print(a)
    
    a = [3.4] * 5
    print(a)
    
    a = 3 * ['ABC']
    print(a)
    
    a = 4 * [10, 20, 30]
    print(a)
    
    n = 3       # Use a variable multiplier
    a = n * ['abc', 22, 8.7]
    print(a)

main()