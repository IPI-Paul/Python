from matplotlib import pyplot as plt
import numpy as np
import csv
from collections import Counter
import pandas as pd
from main import Main
from annotations import Annotations


class Demo():
    def __init__(self) -> None:
        self.examples = [[1, ""], [3, "Overlay"], [3, "Bars"], [3, "Bar Offsets"], [3, "Tick Labels"], [0, "Standard Library csv"], 
                         [0, "Collections Counter"], [1, "Langauge Popularity"], [1, "Langauge Popularity Horizontally"],
                         [1, "Langauge Popularity Reversed"], [1, "Using Pandas"]]    
        self.charts = []

    def run(self, example=1):
        data_source = '../../../../../Source Files/csv/corey_sachafer_matplotlib_2_data.csv'
        self.plots, self.example = self.examples[example - 1]

        if self.example in ["Standard Library csv", "Collections Counter", "Langauge Popularity", "Langauge Popularity Horizontally", 
                            "Langauge Popularity Reversed"]:
            with open(data_source) as csv_file:
                csv_reader = csv.DictReader(csv_file)

                if self.example == "Standard Library csv":
                    plts = plt
                    row = next(csv_reader)
                    if __name__ == "__main__":
                        print(row)
                        print(row['LanguagesWorkedWith'].split(";"))
                    else:
                        plts = [row, row['LanguagesWorkedWith'].split(";")]
                    
                    return [False, plts]
                elif self.example in ["Collections Counter", "Langauge Popularity", "Langauge Popularity Horizontally", "Langauge Popularity Reversed"]:
                    language_counter = Counter()
                    for row in csv_reader:
                        language_counter.update(row['LanguagesWorkedWith'].split(";"))
            
        if self.example == "Collections Counter":
            plts = plt
            if __name__ == "__main__":
                print(language_counter)
                print(language_counter.most_common(15))
            else:
                plts = [language_counter, language_counter.most_common(15)]
            
            return [False, plts]
        elif self.example in ["Using Pandas"]:
            df = pd.read_csv(data_source)
            ids = df['Responder_id']
            lang_responses = df['LanguagesWorkedWith']

            language_counter = Counter()

            for response in lang_responses:
                language_counter.update(response.split(";"))
            
        if self.example in ["Standard Library csv", "Collections Counter"]:exit()

        if self.example in ["Langauge Popularity", "Langauge Popularity Horizontally", "Langauge Popularity Reversed", "Using Pandas"]:
            self.languages = []
            self.popularity = []
            for item in language_counter.most_common(15):
                self.languages.append(item[0])
                self.popularity.append(item[1])

        if self.example in ["Langauge Popularity Reversed", "Using Pandas"]:
            self.languages.reverse()
            self.popularity.reverse()

        plt.style.use("fivethirtyeight")
        
        if (self.plots == 1 and not self.example in ["Langauge Popularity", "Langauge Popularity Horizontally", "Langauge Popularity Reversed", "Using Pandas"]) or \
            self.example in ["Overlay", "Bars", "Bar Offsets", "Tick Labels"]:
            self.ages_x = range(25, 36)
            dev_y = [38496, 42000, 46752, 49620, 53200,
                    56000, 62316, 64928, 67317, 68748, 73752]
            if self.plots > 1 and self.example in ["Overlay", "Bars", "Bar Offsets", "Tick Labels"]:
                py_dev_y = [45372, 48876, 53850, 57287, 63016,
                            65998, 70003, 70000, 71496, 75370, 83640]
            if self.plots > 2 and self.example in ["Overlay", "Bars", "Bar Offsets", "Tick Labels"]:
                js_dev_y = [37810, 43515, 46823, 49293, 53437,
                            56373, 62375, 66674, 68745, 68746, 74583]
        else:pass                
            
        self.annot = Annotations(plts=plt)

        if self.example in ["Bar Offsets", "Tick Labels"]:
            self.x_indexes = np.arange(len(self.ages_x))            
            width = 0.25

        if (self.plots == 1 and not self.example in ["Langauge Popularity", "Langauge Popularity Horizontally", "Langauge Popularity Reversed", "Using Pandas"]) or \
            self.example in ["Overlay", "Bars"]:
            self.charts += [plt.bar(self.ages_x, dev_y, color="#444444", label="All Devs")]
        elif self.example in ["Bar Offsets", "Tick Labels"]:
            self.charts += [plt.bar(self.x_indexes - width, dev_y, width=width, color="#444444", label="All Devs")]
        elif self.example in ["Langauge Popularity"]:
            self.charts += [plt.bar(self.languages, self.popularity)]
        elif self.example in ["Langauge Popularity Horizontally", "Langauge Popularity Reversed", "Using Pandas"]:
            self.charts += [plt.barh(self.languages, self.popularity)]

        if self.plots > 1:
            if self.example == "Overlay":
                self.charts += [plt.plot(self.ages_x, py_dev_y, color="#008fd5", label="Python")]
            elif self.example == "Bars":
                self.charts += [plt.bar(self.ages_x, py_dev_y, color="#008fd5", label="Python")]
            elif self.example in ["Bar Offsets", "Tick Labels"]:
                self.charts += [plt.bar(self.x_indexes, py_dev_y, width=width, color="#008fd5", label="Python")]

        if self.plots > 2:
            if self.example == "Overlay":
                self.charts += [plt.plot(self.ages_x, js_dev_y, color='#e5ae38', label='JavaScript')]
            elif self.example == "Bars":
                self.charts += [plt.bar(self.ages_x, js_dev_y, color='#e5ae38', label='JavaScript')]
            elif self.example in ["Bar Offsets", "Tick Labels"]:
                self.charts += [plt.bar(self.x_indexes + width, js_dev_y, width=width, color='#e5ae38', label='JavaScript')]
        
        if not self.example in ["Langauge Popularity", "Langauge Popularity Horizontally", "Langauge Popularity Reversed", "Using Pandas"]:
            plt.legend()

        if self.example in ["Tick Labels"]:
            plt.xticks(ticks=self.x_indexes, labels=self.ages_x)
            
        if self.example in ["Langauge Popularity"]:
            plt.title("Most Popular Languages")
            plt.xlabel('Programming Languages')
            plt.ylabel('Number of People Who Use')
        elif self.example in ["Langauge Popularity Horizontally", "Langauge Popularity Reversed", "Using Pandas"]:
            plt.title("Most Popular Languages")
            # plt.ylabel('Programming Languages')
            plt.xlabel('Number of People Who Use')
        else:
            plt.xlabel('Ages')
            plt.ylabel('Median Salary (USD)')
            plt.title("Median Salary (USD) by Age")

        plt.tight_layout()

        return [True, plt]
    
    def savePlot(self, file_path):
        plt.savefig(file_path)

    def setAnnotations(self):
        if self.example in ["Bar Offsets"]:
            self.annot.init(self.charts, xdata=self.x_indexes)
        elif self.example in ["Tick Labels"]:
            self.annot.init(self.charts, xdata=self.ages_x)
        elif self.example in ["Langauge Popularity"]:
            self.annot.init(self.charts, xdata=self.languages)
        elif self.example in ["Langauge Popularity Horizontally", "Langauge Popularity Reversed", "Using Pandas"]:
            self.annot.init(self.charts, xdata=self.languages, ydata=self.popularity)
        else:
            self.annot.init(self.charts)
    
    def showPlot(self):
        self.setAnnotations()
        plt.show()

if __name__ == "__main__":
    Main(Demo)