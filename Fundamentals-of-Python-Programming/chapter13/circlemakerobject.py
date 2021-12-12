# Listing 13.3
# Is a rewrite of Listing 13.2 that moves the previously global Turtle and 
# Circle objects inside of a new object of type GraphicalCircle
# Author: Rick Halterman
# Last modified: 

from turtle import Turtle, Screen, mainloop, delay, clear
from circle import Circle

class GraphicalCircle:
    """
    Wraps a Circle object with a prinitive graphical interface. Each 
    GraphicalCircle object maintains its own Circle object and Turtle graphics 
    Turtle object.
    """
    def __init__(self, center, radius):
        """
        Initialises a graphical circle object. The circle is centered at the 
        position specified by the center parameter. The cirlce's radius is set 
        to the radius parameter.
        """
        # Make a turtle graphics object to do the drawing. Assign it to an 
        # instance variable so other methods can access it.
        self.turtle = Turtle()          
        self.turtle.speed(0)            # Make turlte's actions as fast as possible
        self.turtle.hideturtle()        # Make the turtle invisible
        
        # Create a local screen object to receive user input.
        screen = Screen()               
        screen.delay(0)                 # Do not slowly trace drawing
        screen.listen()                 # Set focus for keystrokes
        # Mouse click repositions the circle
        screen.onclick(self.move)       # Set mouse press handler
        # Up cursor key calls the increase method to expand the circle
        screen.onkey(self.increase, 'Up') # Set 'up' cursor key handler
        # Down cursor key calls the decrease method to contract the circle
        screen.onkey(self.decrease, 'Down') # Set 'down' cursor key handler
        
        # Make a circle object. Assign it to an instance variable so other 
        # methods can access it.
        self.circle = Circle(center, radius)
        
        # Start the graphics environment. The local screen object will exist 
        # until the user quits the program.
        screen.mainloop()
        
    def draw(self):
        """
        Draws the circle in the graphical window.
        """
        x, y = self.circle.get_center()     # Unpack circle's coordinates
        radius = self.circle.get_radius()
        self.turtle.penup()                     # Lift pen
        self.turtle.setposition(x, y)           # Move pen to (x, y)
        self.turtle.pendown()                   # Place pen
        self.turtle.dot()                       # Draw a dot at the circle's center
        self.turtle.penup()                     # Lift pen
        self.turtle.setposition(x, y - radius)  # Position pen to draw rim of circle
        self.turtle.pendown()                   # Place pen to draw
        self.turtle.circle(radius)              # Draw the circle
        self.turtle.penup()                     # Lift pen
    
    def move(self, x, y):
        """
        Moves the circle's center to the specified (x, y) location.
        Delegates the work to the contained Circle object.
        """
        self.circle.move((x, y))        # move the circle to a new location
        self.redraw()
    
    def increase(self):
        """
        Increases the circle's radius by one, then redraws the circle. 
        Delegates the work to the contained Circle object.
        """
        self.circle.grow()              # Make the circle bigger
        self.redraw()                   # Redraw the circle object
    
    def decrease(self):
        """
        Reduces the circle's radius by one, then redraws the circle. 
        Delegates the work to the contained Circle object.
        """            
        self.circle.shrink()            # Make the circle smaller
        self.redraw()
    
    def redraw(self):
        """
        Clears the graphical window, then draws the circle.
        """
        self.turtle.clear()                 # Clear the drawing screen
        self.draw()                         # Redraw the circle object
        
def main():
    """
    Allows the user to manipulate a graphical circle object.
    """
    circle = GraphicalCircle((0, 0), 100)   # Make a graphical circle object
    print('Program done')
        
if __name__ == '__main__':
    main()