import matplotlib.pyplot as plt
import pandas as pd


class PieCharts():
    def __init__(self) -> None:
        fifa = pd.read_csv("C:/Users/Paul/Documents/Source Files/csv/fifa_data.csv")
        fifa.Weight = [int(x.strip('lbs')) if type(x) == str else x for x in fifa.Weight]
        light = fifa.loc[fifa.Weight < 125].count()[0]
        light_medium = fifa.loc[(fifa.Weight >= 125) & (fifa.Weight < 150)].count()[0]
        medium = fifa.loc[(fifa.Weight >= 150) & (fifa.Weight < 175)].count()[0]
        medium_heavy = fifa.loc[(fifa.Weight >= 175) & (fifa.Weight < 200)].count()[0]
        heavy = fifa.loc[fifa.Weight >= 200].count()[0]
        weights = [light, light_medium, medium, medium_heavy, heavy]
        labels = ['Under 125', '125-150', '150-175', '175-200', 'Over 200']
        plt.style.use('ggplot')
        explode = [.4, .1, 0, 0, .4]
        plt.title("Weight Distribution of FIFA Players (in lbs)")
        plt.pie(weights, labels=labels, autopct='%.2f %%', pctdistance=0.8, explode=explode)

    def save(self):
        # Save figure (dpi 300 is good when saving so graph has high resolution)
        plt.savefig('mygraph.png', dpi=300)

    def show(self):      
        # Show plot  
        plt.show()
        
        
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    win = PieCharts()
    win.show()