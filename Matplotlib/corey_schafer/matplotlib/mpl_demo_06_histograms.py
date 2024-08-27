import pandas as pd
from matplotlib import pyplot as plt
from main import Main


class Demo():
    def __init__(self) -> None:
        self.examples = [[1, "Non-Real World"], [1, "Edge Colour"], [1, "Ten Year Bins"], [1, "Exclude Bins"], [1, "Real World"],
                         [1, "Logarithmic Scale"], [1, "Median Age"]]  

    def run(self, example=1):
        self.plots, self.example = self.examples[example - 1]

        plt.style.use("fivethirtyeight")

        if self.example in ["Non-Real World", "Edge Colour", "Ten Year Bins", "Exclude Bins"]:
            ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]
        else:
            data_source = '../../../../../Source Files/csv/corey_sachafer_matplotlib_2_data_3.csv'
            df = pd.read_csv(data_source)
            ids = df['Responder_id']
            ages = df['Age']

        if self.example in ["Ten Year Bins"]:
            bins = [10, 20, 30, 40, 50, 60]
        elif self.example in ["Exclude Bins"]:
            bins = [20, 30, 40, 50, 60]
        elif self.example in ["Real World", "Logarithmic Scale", "Median Age"]:
            bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]   

        if self.example in ["Non-Real World"]:
            plt.hist(ages, bins=5)
        elif self.example in ["Edge Colour"]:
            plt.hist(ages, bins=5, edgecolor='black')
        elif self.example in ["Ten Year Bins", "Exclude Bins", "Real World"]:
            plt.hist(ages, bins=bins, edgecolor='black')
        elif self.example in ["Logarithmic Scale", "Median Age"]:
            plt.hist(ages, bins=bins, edgecolor='black', log=True)
        
        if self.example in ["Median Age"]:
            median_age = df['Age'].median() # 29
            color = '#fc4f30'
            plt.axvline(median_age, color=color, label='Age Median', linewidth=2)
            plt.legend()
            
        plt.title("Ages of Respondents")
        plt.xlabel('Ages')
        plt.ylabel('Total Respondents')

        plt.tight_layout()

        return [True, plt]
    
    def savePlot(self, file_path):
        plt.savefig(file_path)

    def setAnnotations(self):
        pass
    
    def showPlot(self):
        self.setAnnotations()
        plt.show()

if __name__ == "__main__":
    Main(Demo)