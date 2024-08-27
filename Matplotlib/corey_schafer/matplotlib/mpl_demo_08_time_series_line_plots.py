import pandas as pd
from datetime import datetime
from matplotlib import pyplot as plt, dates as mpl_dates
from main import Main
from annotations import Annotations


class Demo():
    def __init__(self) -> None:
        self.examples = [[1, "Dates"], [1, "Solid Line"], [1, "Figure Auto Format"], [1, "Datetime Formatting"], [1, "Bitcoin Prices"],
                         [1, "Dates Sorted"]]      
        self.charts = [] 

    def run(self, example=1):
        self.plots, self.example = self.examples[example - 1]
        
        plt.style.use("seaborn-v0_8-colorblind")

        if self.example in ["Dates", "Solid Line", "Figure Auto Format", "Datetime Formatting"]:
            dates = [
                datetime(2019, 5, 24),
                datetime(2019, 5, 25),
                datetime(2019, 5, 26),
                datetime(2019, 5, 27),
                datetime(2019, 5, 28),
                datetime(2019, 5, 29),
                datetime(2019, 5, 30)
            ]
            y = [0, 1, 3, 4, 6, 5, 7]
        else:
            data_source = '../../../../../Source Files/csv/corey_sachafer_matplotlib_2_data_5.csv'
            df = pd.read_csv(data_source)

            if self.example in ["Dates Sorted"]:
                df["Date"] = pd.to_datetime(df["Date"])
                df.sort_values('Date', inplace=True)

            price_date = df['Date']
            price_close = df['Close']      
            
        self.annot = Annotations(plts=plt)

        if self.example in ["Dates"]:
            self.charts += [plt.plot_date(dates, y)]
        elif self.example in ["Solid Line", "Figure Auto Format", "Datetime Formatting"]:
            self.charts += [plt.plot_date(dates, y, linestyle='solid')]
        elif self.example in ["Bitcoin Prices", "Dates Sorted"]:
            self.charts += [plt.plot_date(price_date, price_close, linestyle='solid')]

        if self.example in ["Figure Auto Format", "Datetime Formatting", "Bitcoin Prices", "Dates Sorted"]:
            plt.gcf().autofmt_xdate()

        if self.example in ["Datetime Formatting"]:
            date_format = mpl_dates.DateFormatter('%b, %d %Y')
            plt.gca().xaxis.set_major_formatter(date_format)

        if not self.example in ["Dates", "Solid Line", "Figure Auto Format", "Datetime Formatting"]:
            plt.title("Bitcoin Prices")
            plt.xlabel('Date')
            plt.ylabel('Closing Price')

        plt.tight_layout()

        return [True, plt]
    
    def savePlot(self, file_path):
        plt.savefig(file_path)

    def setAnnotations(self):
        self.annot.init(self.charts)
    
    def showPlot(self):
        self.setAnnotations()
        plt.show()

if __name__ == "__main__":
    Main(Demo)