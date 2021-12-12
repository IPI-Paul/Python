# Listing 7.6
# Uses turle graphics to draw regular polygons with varying numbers of sides
# Author: Rick Halterman
# Last modified: 

import turtle
import random

# Draw a regular polygon with the given number of sides.
# The length of each side is length.
# The pen begins at point(x, y)
# The color of the polygon is color
def polygon(sides, length, x, y, color):
    turtle.penup()                  # Lift pen to move it
    turtle.setposition(x, y)        # Move the pen to coordinates (x, y)
    turtle.pendown()                # Place pen to begin drawing
    turtle.color(color)          # Set pen color
    turtle.begin_fill()
    for i in range(sides):          # Draw eight sides
        turtle.forward(length)      # Each side is length units long
        turtle.left(360 // sides)   # Each vertex is 360 // sides degrees
    turtle.end_fill()


# Disable rendering to speed up drawing

turtle.hideturtle()
turtle.tracer(0)

# Draw 20 random polygons with 3/11 sides, each side ranging in length from 
# 10-50, located at random position(x, y). 
# Select a color at random from red, gree, blue, black, or yellow.
for i in range(20):
    polygon(random.randrange(3, 11), random.randrange(10, 51), 
            random.randrange(-250, 251), random.randrange(-250, 251),
            random.choice(('red', 'green', 'blue', 'black', 'yellow')))

turtle.update()                 # Render image
turtle.exitonclick()            # Wait for user's mouse click