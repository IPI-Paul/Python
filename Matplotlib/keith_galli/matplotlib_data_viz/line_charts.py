import matplotlib.pyplot as plt
import numpy as np

class LineCharts():
    def __init__(self) -> None:
        # Basic Graph
        x = [0, 1, 2, 3, 4]
        y = [0, 2, 4, 6, 8]

        # Resize Graph (dpi specifies pixels per inch. When saving probably should use 300 if posible)
        # plt.figure(figsize=(5, 3), dpi=100)

        plt.plot(x, y, label='2x', color='blue', linewidth=2, marker='.', markersize=10, markeredgecolor='red', linestyle='--')

        # Shorthand notation
        plt.plot(y, x, 'b.--', label='y')

        # Line Number Two
        # Select interval we want o plot points at
        x2 = np.arange(0, 4.5, 0.5)

        # Plot part of the graph as a line
        plt.plot(x2[:6], x2[:6]**2, 'r', label='x^2')

        # Plot remainder of the graph as a dashed line
        plt.plot(x2[5:], x2[5:]**2, 'r--')

        #  Add a title (specify font parameters with fontdict)
        plt.title('Our First Graph', fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})

        # x and y labels
        plt.xlabel('X Axis')
        plt.ylabel('Y Axis')

        # x, y axis Tickmarks (scale of your graph)
        # Set the tick range to the max of x and y
        plt.xticks(np.arange(0, max(max(x, y)) + 1, 1))

        # Set the tick range to the max of x, y and x2^2
        plt.yticks(np.arange(0, max(max(max(x, y)), (x2**2).max()) + 1, 1))

        plt.legend()

    def save(self):
        # Save figure (dpi 300 is good when saving so graph has high resolution)
        plt.savefig('mygraph.png', dpi=300)

    def show(self):      
        # Show plot  
        plt.show()
        
        
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    win = LineCharts()
    win.show()