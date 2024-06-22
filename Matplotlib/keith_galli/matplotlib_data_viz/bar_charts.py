import matplotlib.pyplot as plt

class BarCharts():
    def __init__(self) -> None:
        labels = ['A', 'B', 'C']
        values = [1, 4, 2]

        bars = plt.bar(labels, values)

        # bars[0].set_hatch('/')
        # bars[1].set_hatch('O')
        # bars[2].set_hatch('*')
        # Or
        patterns = ['/', 'O', '*']
        for bar in bars:
            bar.set_hatch(patterns.pop(0))

    def save(self):
        # Save figure (dpi 300 is good when saving so graph has high resolution)
        plt.savefig('mygraph.png', dpi=300)

    def show(self):      
        # Show plot  
        plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    win = BarCharts()
    win.show()