# Listing 7.13
# Illustrates that parameters within functions and formal parameters are treated
# as two completely different contexts even when given the same name
# Author: Rick Halterman
# Last modified: 

def increment(x):
    print('Beginning execution of increment, x =', x)
    x += 1  # Increment
    print('Ending execution of increment, x =', x)

def main():
    x = 5
    print('Before increment, x =', x)
    increment(x)
    print('After increment, x =', x)
    
main()