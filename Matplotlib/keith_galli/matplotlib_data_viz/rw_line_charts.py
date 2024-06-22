import matplotlib.pyplot as plt
import pandas as pd


class LineCharts():
    def __init__(self) -> None:
        gas = pd.read_csv("C:/Users/Paul/Documents/Source Files/csv/gas_prices.csv")

        # plt.figure(figsize=(8, 5))

        plt.title("Gas Prices over Time (in USD)", fontdict={'fontweight': 'bold', 'fontsize': 18})
        
        plt.plot(gas.Year, gas.USA, 'r.-', label='United States')
        plt.plot(gas.Year, gas.Canada, 'b.-', label='Canada')
        plt.plot(gas.Year, gas['South Korea'], 'g.-', label='South Korea')
        plt.plot(gas.Year, gas.Australia, 'y.-', label='Australia')

        # Other ways to plot many values
        # for country in gas:
        #     if country != 'Year':
        #         plt.plot(gas.Year, gas[country], marker='.', label=country)

        # countries_to_look_at = ['Australia', 'Canada', 'South Korea', 'USA']
        # for country in gas:
        #     if country in countries_to_look_at:
        #         plt.plot(gas.Year, gas[country], marker='.', label=country)

        # Use ::# to skip years
        plt.xticks(gas.Year[::3].tolist()+[2011])

        plt.xlabel('Year')
        plt.ylabel('US Dollars')

        plt.grid()

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