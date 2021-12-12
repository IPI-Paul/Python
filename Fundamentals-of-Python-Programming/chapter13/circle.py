# Listing 13.1
# Contains the complete specification for Circle.
# Author: Rick Halterman
# Last modified: 

from math import pi

class Circle:
    """
    Represents a geometric cirlce object
    """
    def __init__(self, center, radius):
        """
        Initialise the cirle's center and radius
        """
        # Disallow a negative radius
        if radius < 0:
            raise  ValueError('Negative radius')
        self.center = center
        self.radius = radius
    
    def get_radius(self):
        """
        Return the radius of the circle
        """
        return self.radius
    
    def get_center(self):
        """
        Return the coordinates of the center
        """
        return self.center
    
    def get_area(self):
        """
        Compute and return the area of the circle
        """
        # return pi * self.radius * self.radius
        return pi * self.radius ** 2
    
    def get_circumference(self):
        """
        Compute and return the circumference of the circle
        """
        return 2 * pi * self.radius
    
    def move(self, pt):
        """
        Moves the center of the circle to point pt
        """
        self.center = pt
    
    def grow(self):
        """
        Increases the radius of the circle 
        """
        self.radius += 1
    
    def shrink(self):
        """
        Decreases the radius of the circle; does not affect a circle with radius 
        zero
        """
        if self.radius > 0:
            self.radius -= 1