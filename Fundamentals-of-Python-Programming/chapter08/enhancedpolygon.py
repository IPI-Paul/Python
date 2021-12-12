# Listing 8.2
# Enhances Listing 7.6 by adding the ability to optionally fill the polygon with
# a color
# Author: Rick Halterman
# Last modified: 

import turtle
import random

# Draws a regular polygon with the given number of sides.
# The length of each side is length.
# The pen begins at point(x, y)
# The color of the polygon is color (defaults to black).
# The polygon is rendered solid if fill is True (defaults to False).
def polygon(sides, length, x, y, color = "black", fill = False):
    turtle.penup()                  # Lift pen to move it
    turtle.setposition(x, y)        # Move the pen to coordinates (x, y)
    turtle.pendown()                # Place pen to begin drawing
    turtle.color(color)          # Set pen color
    if fill:
        turtle.begin_fill()
    for i in range(sides):          # Draw eight sides
        turtle.forward(length)      # Each side is length units long
        turtle.left(360 // sides)   # Each vertex is 360 // sides degrees
    if fill:
        turtle.end_fill()


# Disable rendering to speed up drawing

turtle.hideturtle()
turtle.tracer(0)

# Draw a few polygons
polygon(3, 30, 10, 10)                  # Black triangle outline
polygon(4, 30, 50, 50, "blue")          # Blue square outline
polygon(5, 30, 100, 100, "red", True)   #Red solid pentagon

# Draw 20 random polygons with 3/11 sides, each side ranging in length from 
# 10-50, located at random position(x, y). 
# Select a color at random from red, gree, blue, black, or yellow.
for i in range(5):
    fill = True if i % 2 == 0 else False
    polygon(random.randrange(3, 11), random.randrange(10, 51), 
            random.randrange(-250, 10), random.randrange(-250, 10),
            random.choice(('red', 'green', 'blue', 'black', 'yellow')), fill)

turtle.update()                 # Render image
turtle.exitonclick()            # Wait for user's mouse click