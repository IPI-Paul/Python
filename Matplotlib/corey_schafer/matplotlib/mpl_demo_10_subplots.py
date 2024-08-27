import pandas as pd
from matplotlib import pyplot as plt
from main import Main
from annotations import Annotations


class Demo():
    def __init__(self) -> None:
        self.examples = [[3, "Staple"], [3, "Subplots"], [1, "Show Axes"], [1, "2 Rows, 1 Column Axes"], [1, "2 Rows, 2 Columns Axes"],
                         [3, "2 Axes"], [3, "2 Axes Plots"], [3, "Single Title"], [3, "Share X"], [3, "2 Figures"]]      
        self.charts = [] 

    def run(self, example=1):
        self.plots, self.example = self.examples[example - 1]
        
        plt.style.use("seaborn-v0_8-colorblind")

        data_source = '../../../../../Source Files/csv/corey_sachafer_matplotlib_2_data_1.csv'
        df = pd.read_csv(data_source)
        ages = df['Age']
        dev_salaries = df['All_Devs']
        py_salaries = df['Python']
        js_salaries = df['JavaScript']

        self.annot1 = None

        if self.example in ["Subplots", "Show Axes"]:
            fig, ax = plt.subplots()
        elif self.example in ["2 Rows, 1 Column Axes"]:
            fig, ax = plt.subplots(nrows=2, ncols=1)
        elif self.example in ["2 Rows, 2 Columns Axes"]:
            fig, ax = plt.subplots(nrows=2, ncols=2)
        elif self.example in ["2 Axes", "2 Axes Plots", "Single Title"]:
            fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)
        elif self.example in ["Share X"]:
            fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)
        elif self.example in ["2 Figures"]:
            self.fig1, ax1 = plt.subplots()
            self.fig2, ax2 = plt.subplots()
        
        if self.example in ["Show Axes", "2 Rows, 1 Column Axes", "2 Rows, 2 Columns Axes", "2 Axes"]:
            plts = plt
            if __name__ == "__main__":
                if self.example in ["2 Axes"]:
                    print(ax1)
                    print(ax2)
                else:
                    print(ax)
            else:
                if self.example in ["2 Axes"]:
                    plts = [ax1, ax2]
                else:
                    plts = [ax]
            return [False, plts]
        
        if self.example in ["Staple"]:
            self.annot = Annotations(plts=plt)
        elif self.example in ["Subplots"]:
            self.annot = Annotations(plts=plt, fig=fig, plot=ax)
        elif self.example in ["2 Axes", "2 Axes Plots", "Single Title", "Share X"]:
            self.annot = Annotations(plts=plt, fig=fig, plot=ax1)
            self.annot1 = Annotations(plts=plt, fig=fig, plot=ax2)
        elif self.example in ["2 Figures"]:
            self.annot = Annotations(plts=plt, fig=self.fig1, plot=ax1)
            self.annot1 = Annotations(plts=plt, fig=self.fig2, plot=ax2)

        if self.example in ["Staple"]:
            self.charts += [plt.plot(ages, py_salaries, label='Python')]
            self.charts += [plt.plot(ages, js_salaries, label='JavaScript')]
            self.charts += [plt.plot(ages, dev_salaries, color='#444444', linestyle='--', label='All Devs')]
        elif self.example in ["Subplots"]:
            self.charts += [ax.plot(ages, py_salaries, label='Python')]
            self.charts += [ax.plot(ages, js_salaries, label='JavaScript')]
            self.charts += [ax.plot(ages, dev_salaries, color='#444444', linestyle='--', label='All Devs')]
        elif self.example in ["2 Axes Plots", "Single Title","Share X", "2 Figures"]:         
            self.charts += [ax1.plot(ages, dev_salaries, color='#444444', linestyle='--', label='All Devs')]
            self.charts += [ax2.plot(ages, py_salaries, label='Python')]
            self.charts += [ax2.plot(ages, js_salaries, label='JavaScript')   ]

        if self.example in ["Staple"]:
            plt.legend()
        elif self.example in ["Subplots"]:
            ax.legend()
        elif self.example in ["2 Axes Plots", "Single Title","Share X", "2 Figures"]:  
            ax1.legend()
            ax2.legend()

        if self.example in ["Staple"]:
            plt.title("Median Salary (USD) by Age")
            plt.xlabel('Ages')
            plt.ylabel('Median Salary (USD)')
        elif self.example in ["Subplots"]:
            ax.set_title("Median Salary (USD) by Age")
            ax.set_xlabel('Ages')
            ax.set_ylabel('Median Salary (USD)')
        elif self.example in ["2 Axes Plots", "Single Title","Share X", "2 Figures"]:  
            ax1.set_title("Median Salary (USD) by Age")
            if not self.example in ["Single Title","Share X"]:
                ax1.set_xlabel('Ages')
            ax1.set_ylabel('Median Salary (USD)')
            if not self.example in ["Single Title","Share X"]:
                ax2.set_title("Median Salary (USD) by Age")
            ax2.set_xlabel('Ages')
            ax2.set_ylabel('Median Salary (USD)')

        plt.tight_layout()

        return [True, plt]
    
    def savePlot(self, file_path):
        if self.example in ["2 Figures"]:
            self.fig1.savefig(file_path)
            self.fig2.savefig('../../../../../Source Files/png/fig2.png')
        else:     
            plt.savefig(file_path)

    def setAnnotations(self):
        self.annot.init(self.charts)
        if self.annot1:
            self.annot1.init(self.charts)
    
    def showPlot(self):
        self.setAnnotations()
        plt.show()

if __name__ == "__main__":
    Main(Demo)