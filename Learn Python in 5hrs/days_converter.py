def days_to_units(num_of_days, current_type=1):
    to_seconds = (24 * 60 * 60, "seconds")
    to_minutes = (24 * 60, "minutes")
    to_hours = (24, "hours")
    calculation_type = [to_hours, to_minutes, to_seconds]
    calculation_to_units = calculation_type[current_type][0]
    name_of_unit = calculation_type[current_type][1]
    print(f"{num_of_days} days are {format(num_of_days * calculation_to_units, ',d')} {name_of_unit}")
    # print("All good!")


def validate_and_execute():
    arr = user_input.replace(" ", "").split(",")
    if len(arr) > len(set(arr)):
        _ = []
        arr = [_, list(map(lambda x: _ if _.__contains__(arr[x]) else _.append(arr[x]), range(0, len(arr))))][0]
    for day in arr:
        if day == 'exit':
            msg = f"The following items will not be computed {arr[arr.index(day) + 1:]}" if \
                arr.index(day) + 1 < len(arr) else ""
            print(f"'{day}' was included in your input!\n{msg}")
            return day
        elif day == 'test1':
            list(test1)
            continue
        try:
            days = int(day.split(':')[0])
            if days == 0:
                print("You entered a 0, therefore nothing to calculate!")
                continue
            elif days < 0:
                print("You entered a negative number, Nana says no conversion for you!")
                continue
        except ValueError:
            print(f"Your days input '{day.split(':')[0]}' is not a valid number. Don't ruin my program!")
            continue
        calc_value = day.split(':')[1] if day.__contains__(':') else 0
        try:
            calc_type = int(calc_value)
        except ValueError:
            print(f"Your calculation type '{calc_type}' is not a valid number. Don't ruin my program!")
            continue
        try:
            days_to_units(days, calc_type)
        except IndexError:
            print(f"Invalid calculation type '{calc_type}'.",
                  "You can only enter 0 for Hours, 1 for Minutes or 2 for Seconds")
            continue
    return None


# Not run
test1 = map(lambda i: days_to_units(i, 0), [20, 35, 50, 110])
# list(test1)

user_input = None
while user_input not in ["", "exit"]:
    if user_input is None:
        user_input = input('''
Please give number of days to convert or a comma separated list of days. 
(Optionally you can also enter 0 for Hours, 1 for Minutes, 2 for Seconds and 'exit' or enter only to quit! 
If you add an optional type then you need to separate the number of days value from the optional value with a comma!
i.e 20: 2)
> ''')
    else:
        user_input = input('> ')
    if user_input in ["", "exit"] or validate_and_execute() == 'exit':
        print("All Done, bye ;D")
        break
