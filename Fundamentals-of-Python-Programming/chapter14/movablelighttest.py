# Listing 14.13
# Is a small application that allows the user to move the traffic light image to 
# various places in the window via a mouse click. The user changes the light by 
# pressing the C key. The program also utilises the inherited resize method by 
# allowing the user to press the < key to shrink or > key to grow the traffic 
# light object
# Author: Rick Halterman
# Last modified: 

import tkinter as tk
import tkinter.ttk as ttk

from movablelight import MovableLight

class MovableLightTest:
    """
    Graphical window that allows a user to move and resize a traffic light 
    object
    """
    
    def __init__(self):
        root = tk.Tk()      # Create the main window
        root.title('Movable Traffic Light Test')    # Set title bar text
        width, height = 800, 600
        f = ttk.Frame(root, width=width, height=height)
        f.pack()
        # Place traffic light at the center of the window frame
        print('Frame width:', f.winfo_width())
        self.light_width = height // 10
        self.light = MovableLight(f, self.light_width, 'green')
        f.bind('<Button-1>', self.mouse_pressed)
        f.bind('<Key>', self.key_pressed)
        f.focus_set()   # Allow graphical window to receive key strokes
        print('width // 2 =', width // 2, ' height // 2 =', height // 2)
        self.light.move_to(width // 2, height // 2)
        # Start the GUI event loop
        root.mainloop()
    
    def mouse_pressed(self, event):
        """
        The window manager calls this function when the user presses clicks 
        the mouse button
        """
        self.light.move_to(event.x, event.y)
    
    def key_pressed(self, event):
        """
        The window manager calls this function when the user presses a key
        """
        ch = event.char
        if ch == '>' or ch == '.':
            self.light_width += 5
            self.light.resize(self.light_width)
        elif ch == '<' or ch ==',':
            self.light_width -= 5
            self.light.resize(self.light_width)
        elif ch.upper() == 'C':
            self.light.change()
        print('Key pressed')
        
# Main program -----------------------------------------------------------

# Create and execute a traffic light window
MovableLightTest()