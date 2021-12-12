# Listing 4.18
# Uses if/elif/else statements to carry out one of many actions avoiding 
# rightward code drift
# Author: Rick Halterman
# Last modified: 

value = int(input("Please enter an integer in the range 0...5: "))
if value <0:
    print("Too small")
elif value == 0:
    print("zero")
elif value == 1:
    print("one")
elif value == 2:
    print("two")
elif value == 3:
    print("three")
elif value == 4:
    print("four")
elif value == 5:
    print("five")
else:
    print("Too large")
print("Done")