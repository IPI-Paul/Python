import matplotlib.pyplot as plt
import pandas as pd


class SimplePieCharts():
    def __init__(self) -> None:
        fifa = pd.read_csv("C:/Users/Paul/Documents/Source Files/csv/fifa_data.csv")
        left = fifa.loc[fifa['Preferred Foot'] == 'Left'].count()[0]
        right = fifa.loc[fifa['Preferred Foot'] == 'Right'].count()[0]
        labels = ['Left', 'Right']
        colors = ['#abcdef', '#aabbcc']
        plt.pie([left, right], labels=labels, colors=colors, autopct='%.2f %%')
        plt.title('Foot Preference of FIFA Players')

    def save(self):
        # Save figure (dpi 300 is good when saving so graph has high resolution)
        plt.savefig('mygraph.png', dpi=300)

    def show(self):      
        # Show plot  
        plt.show()
        
        
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    win = SimplePieCharts()
    win.show()