import pandas as pd
from matplotlib import pyplot as plt
from main import Main
from annotations import Annotations


class Demo():
    def __init__(self) -> None:
        self.examples = [[2, "Lines"], [2, "Fill Python"], [2, "Alpha Python"], [2, "Overall Median"], [2, "Conditional"],
                         [2, "Above & Below"], [2, "Above & Below Coloured"], [2, "Between the Lines"], [2, "Labelled Fill"]]        
        self.charts = [] 

    def run(self, example=1):
        self.plots, self.example = self.examples[example - 1]
        if not self.example in ["Between the Lines", "Labelled Fill"]:
            data_source = '../../../../../Source Files/csv/corey_sachafer_matplotlib_2_data_1.csv'
        else:
            data_source = '../../../../../Source Files/csv/corey_sachafer_matplotlib_2_data_2.csv'
        df = pd.read_csv(data_source)

        if self.example in ["Lines", "Fill Python", "Alpha Python", "Overall Median", "Conditional", "Above & Below", 
                            "Above & Below Coloured", "Between the Lines", "Labelled Fill"]:
            ages = df['Age']
            dev_salaries = df['All_Devs']
            py_salaries = df['Python']
            js_salaries = df['JavaScript']    

        if self.example in ["Overall Median","Conditional", "Above & Below", "Above & Below Coloured", "Between the Lines", "Labelled Fill"]:
            # print(df["All_Devs"].median())
            # temp = df
            # print(temp[["All_Devs", "Python", "JavaScript"]].median(axis=1))
            # temp['Overall'] = temp[["All_Devs", "Python", "JavaScript"]].median(axis=1)
            # print(temp['Overall'].median())
            # overall_median = df["All_Devs"].median()
            overall_median = 57287           
            
        self.annot = Annotations(plts=plt)

        if self.example in ["Lines", "Fill Python", "Alpha Python", "Overall Median", "Conditional", "Above & Below", 
                            "Above & Below Coloured", "Between the Lines", "Labelled Fill"]:
            self.charts += [plt.plot(ages, dev_salaries, color='#444444', linestyle='--', label='All Devs')]

        if self.plots > 1:
            if self.example in ["Lines", "Fill Python", "Alpha Python", "Overall Median", "Conditional", "Above & Below", 
                                "Above & Below Coloured", "Between the Lines", "Labelled Fill"]:
                self.charts += [plt.plot(ages, py_salaries, label='Python')]

        if self.example in ["Fill Python"]:
            plt.fill_between(ages, py_salaries)
        elif self.example in ["Alpha Python"]:
            plt.fill_between(ages, py_salaries, alpha=0.25)
        elif self.example in ["Overall Median"]:
            plt.fill_between(ages, py_salaries, overall_median, alpha=0.25)
        elif self.example in ["Conditional", "Above & Below", "Above & Below Coloured"]:
            plt.fill_between(ages, py_salaries, overall_median, where=(py_salaries > overall_median), interpolate=True, alpha=0.25)
            if self.example in ["Above & Below"]:
                plt.fill_between(ages, py_salaries, overall_median, where=(py_salaries <= overall_median), interpolate=True, alpha=0.25)
            elif self.example in ["Above & Below Coloured"]:
                plt.fill_between(ages, py_salaries, overall_median, where=(py_salaries <= overall_median), interpolate=True, color='red', alpha=0.25)
        elif self.example in ["Between the Lines"]:
            plt.fill_between(ages, py_salaries, dev_salaries, where=(py_salaries > dev_salaries), interpolate=True, alpha=0.25)
            plt.fill_between(ages, py_salaries, dev_salaries, where=(py_salaries <= dev_salaries), interpolate=True, color='red', alpha=0.25)
        elif self.example in ["Labelled Fill"]:
            plt.fill_between(ages, py_salaries, dev_salaries, where=(py_salaries > dev_salaries), interpolate=True, alpha=0.25, label='Above Avg')
            plt.fill_between(ages, py_salaries, dev_salaries, where=(py_salaries <= dev_salaries), interpolate=True, color='red', alpha=0.25, label='Below Avg')

        if self.example in ["Lines", "Fill Python", "Alpha Python", "Overall Median", "Conditional", "Above & Below", 
                            "Above & Below Coloured", "Between the Lines", "Labelled Fill"]:
            plt.legend()
            
        plt.title("Median Salary (USD) by Age")
        plt.xlabel('Ages')
        plt.ylabel('Median Salary (USD)')

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