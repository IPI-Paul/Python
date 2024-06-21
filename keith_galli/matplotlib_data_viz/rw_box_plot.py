import matplotlib.pyplot as plt
import pandas as pd


class BoxPlots():
    def __init__(self) -> None:
        fifa = pd.read_csv("C:/Users/Paul/Documents/Source Files/csv/fifa_data.csv")
        barcelona = fifa.loc[fifa.Club == 'FC Barcelona']['Overall']
        madrid = fifa.loc[fifa.Club == 'Real Madrid']['Overall']
        revs = fifa.loc[fifa.Club == 'New England Revolution']['Overall']
        labels = ['FC Barcelona', 'Real Madrid', 'New England Revolution']
        boxes = plt.boxplot([barcelona, madrid, revs], labels=labels, patch_artist=True, medianprops={'linewidth': 2})

        for box in boxes['boxes']:
            # Set edge color
            box.set(color='#4286f4', linewidth=2)

            # Change fill color
            box.set(facecolor='#e0e0e0')
        
        plt.title('Professional Soccer Team Comparison')
        plt.ylabel('FIFA Overall Rating')

    def save(self):
        # Save figure (dpi 300 is good when saving so graph has high resolution)
        plt.savefig('mygraph.png', dpi=300)

    def show(self):      
        # Show plot  
        plt.show()
        
        
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    win = BoxPlots()
    win.show()