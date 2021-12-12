# Listing 4.22
# Uses if/elif/else statement to demonstrate that multi-way conditional 
# statements behave differently from sequential ifs
# Author: Rick Halterman
# Last modified: 

num = int(input("Please enter an integer: "))
if num == 1:
    print("You entered one")
elif num == 2:
    print("You entered two")
elif num > 5:
    print("You entered a number greater than five")
elif num == 7:
    print("You entered seven")
else:
    print("You entered some other number")