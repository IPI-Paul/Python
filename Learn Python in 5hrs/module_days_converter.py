"""
Other Import formats
    import helper
with alias
    import helper as h
import all methods and variables
    import *
"""
from helper import validate_and_execute, user_input_message

user_input = None
while user_input not in ["", "exit"]:
    user_input = input(user_input_message)
    if user_input in ["", "exit"]:
        print("All done, bye ;D")
        continue
    days_and_unit = user_input.replace(" ", "").split(":")
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    validate_and_execute(days_and_unit_dictionary)
