# Listing 6.22
# Uses aliasing and shorter qualified function names. It runs faster that 
# Listing 6.19 because it calls the t.delay functionto speed up drawing
# Author: Rick Halterman
# Last modified: 

# Draws in the window a spiral surrounded with an octogon

import turtle as t          # use a shorter name for turtle module

t.delay(0)                  # Draw as quickly as possible
t.speed(0)                  # Turtle's action as fast as possible
t.hideturtle()              # Do not show the pen
# Draw a red ocotogon centered at (-45, 100)
t.pencolor('red')          # Set pen color
t.penup()                  # Lift pen to move it
t.setposition(-45, 100)    # Move the pen to coordinates (-45, 100)
t.pendown()                # Place pen to begin drawing
for i in range(8):              # Draw eight sides
    t.forward(80)          # Each side is 80 units long
    t.right(45)            # Each vertex is 45 degrees


# Draw a blue spiral centered at (0, 0)
distance = 0.2
angle = 40
t.pencolor('blue')         # Set pen color
t.penup()                  # Lift pen to move it
t.setposition(0, 0)        # Position the pen at coordinates (0, 0)
t.pendown()                # Set pen down to begin drawing
for i in range(100):
    t.forward(distance)
    t.left(angle)
    distance += 0.5

t.exitonclick()            # Quit program when user clicks mouse button