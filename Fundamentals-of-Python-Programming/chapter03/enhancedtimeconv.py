# Listing 3.10
# File enhancedtimeconv.py
# Uses integer division and modulus to split up a given number of seconds to 
# hours, minutes, and seconds. Then uses the fact that if x is a one- or two-digit
# number, x 5 10 is the tens digit of x. if x % 10 is zero, x is necessarily a 
# one-digit number
# Author: Rick Halterman
# Last modified: 

# Get the number of seconds
seconds = int(input("Please enter the number of seconds:"))
# First, compute the number of hours in the given number of seconds 
# Note: integer division with possible truncation
hours = seconds // 3600 # 3600 seconds = 1 hour
# Compute the remaining seconds after the hours are accounted for
seconds = seconds % 3600
# Next, compute the number of minutes in the remaining number of seconds
minutes = seconds // 60 # 60 seconds = 1 minute
# Compute the remaining seconds after the minutes are accounted for
seconds = seconds % 60
# Report the results
print(hours, ":", sep="", end="")
# Compute tens digit of minutes
tens = minutes // 10
# Compute ones digit of minutes
ones = minutes % 10
print(tens, ones, ":", sep="", end="")
# Compute tens digit of seconds
tens = seconds // 10
# Compute ones digit of seconds
ones = seconds % 10
print(tens, ones, sep="")