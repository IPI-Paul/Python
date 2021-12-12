# Listing 3.9
# File timeconv.py
# Uses integer division and modulus to split up a given number of seconds to 
# hours, minutes, and seconds
# Author: Rick Halterman
# Last modified: 

# Get the number of seconds
seconds = int(input("Please enter the number of seconds: "))
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
print(hours, "hr,", minutes, "min,", seconds, "sec")