# Listing 5.24
# Incorporates a while statement so that the program's execution continues until
# a computer troubleshooting problem is resolved or its resolution is beyond the
# capabilities of the program. It uses break statments in place of the boolean 
# done variable to exit the loop.
# Author: Rick Halterman
# Last modified: 

print("Help! My computer doesn't work!")
while True:
    print("Does the computer make any sounds (fans, etc.)")
    choice = input("or show any lights? (y/n):")
    # Troublshooting control logic
    if choice == 'n': # The computer does not have power
        choice = input("Is it plugged in? (y/n):")
        if choice == 'n': # It is not plugged in, plug it in
            print("Plug it in.")
        else:   # It is plugged in
            choice = input("Is the switch in the \"on\" position? (y/n):")
            if choice == 'n':   # The switch is off, turn it on!
                print("Turn it on.")
            else:   # The switch is on
                choice = input("Does the computer have a fuse? (y/n):")
                if choice == 'n':   # No fuse
                    choice = input("Is the outlet OK? (y/n): ")
                    if choice == 'n':   # Fix outlet
                        print("Check the outlet's circuit breaker or fuse. Move ")
                        print("to a new outlet, if necessary.")
                    else:   # Beats me!
                        print("Please consult a service technician.")
                        break     # Nothing else I can do, exit loop
                else:   # Check fuse
                    print("Check the fuse. Replace if necessary.")
    else:  # The computer has power
        print("Please consult a service technician.")
        break     # Nothing else I can do, exit loop