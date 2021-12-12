# Listing 14.12
# Augments the Traffic Signal class, enabling clients to reposition the traffic
# light's center to a given (x, y) location within the graphics window
# Author: Rick Halterman
# Last modified: 

import tkinter as tk
import tkinter.ttk as ttk

from trafficsignal import TrafficSignal

class MovableLight(TrafficSignal):
    """
    Models a graphical traffic light that the user can reposition
    """
    
    def __init__(self, parent, width, initial_color='red'):
        """
        Makes a new movable traffic light object. 
        parent: is the parent widget
        width: is the width of the light in pixels
        initial_color: is the light's initial colour
        """
        # Call base class constructor
        super().__init__(parent, width, initial_color)
        self.place(x=0, y=0)
        
    def move_to(self, x, y):
        """
        Positions the light's center at point(x, y)
        """
        center_x_offset = self.winfo_width() // 2
        center_y_offset = self.winfo_height() // 2
        self.x = x - center_x_offset
        self.y = y - center_y_offset
        self.place(x=self.x, y=self.y)