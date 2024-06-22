import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class Histogram():
    def __init__(self) -> None:
        fifa = pd.read_csv("C:/Users/Paul/Documents/Source Files/csv/fifa_data.csv")
        bins = np.arange(40, 100, 10)
        plt.hist(fifa.Overall, bins=bins, color='#abcdef')
        plt.ylabel('Number of Players')
        plt.xlabel('Skill Level')
        plt.title('Distribution of Player Skills in FIFA 2018')
        plt.xticks(bins)

    def save(self):
        # Save figure (dpi 300 is good when saving so graph has high resolution)
        plt.savefig('mygraph.png', dpi=300)

    def show(self):      
        # Show plot  
        plt.show()
         

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    win = Histogram()
    win.show()