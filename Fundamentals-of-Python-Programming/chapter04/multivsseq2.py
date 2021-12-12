# Listing 4.23
# Uses if statements to demonstrate that sequential ifs behave differently from  
# multi-way conditional statements
# Author: Rick Halterman
# Last modified: 

num = int(input("Please enter an integer: "))
if num == 1:
    print("You entered one")
if num == 2:
    print("You entered two")
if num > 5:
    print("You entered a number greater than five")
if num == 7:
    print("You entered seven")
else:
    print("You entered some other number")