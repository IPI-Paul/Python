# Listing 10.8
# Demonstrates several ways to build a list without explicitly listing every 
# element in the list.
# Author: Rick Halterman
# Last modified: 

def main():
    a = list(range(0, 10))
    print(a)
    a = list(range(10, -1, -1))
    print(a)
    a = list(range(0, 100, 10))
    print(a)
    a = list(range(-5, 6))
    print(a)

main()