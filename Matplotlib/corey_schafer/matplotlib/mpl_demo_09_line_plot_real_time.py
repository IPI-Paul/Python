import random
from itertools import count
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from main import Main
from data_gen import DataWriter
from annotations import Annotations


class Demo():
    def __init__(self) -> None:
        self.examples = [[1, "Hard Coded"], [1, "Animate"], [1, "Clear Axis"], [1, "Real-Time"]]        
        self.charts = [] 

    def run(self, example=1):
        self.plots, self.example = self.examples[example - 1]

        plt.style.use("fivethirtyeight")

        if self.example in ["Hard Coded"]:
            x_vals = range(0, 6)
            y_vals = [0, 1, 3, 2, 3, 5]
        elif self.example in ["Animate", "Clear Axis"]:
            x_vals = []
            y_vals = []

            index = count()
        elif self.example in ["Real-Time"]:   
            self.gen_data = DataWriter() 
            
        self.annot = Annotations(plts=plt)

        if self.example in ["Hard Coded"]:
            self.charts += [plt.plot(x_vals, y_vals)]
        elif self.example in ["Animate", "Clear Axis"]:   
            def animate(i):
                x_vals.append(next(index))
                y_vals.append(random.randint(0, 5))         
                if self.example in ["Clear Axis"]:   
                    plt.cla()
                self.charts += [plt.plot(x_vals, y_vals)]
        elif self.example in ["Real-Time"]:   
            def animate(i):
                df = pd.read_csv(self.gen_data.data_source)
                x = df['x_value']
                y1 = df['total_1']
                y2 = df['total_2']
                
                plt.cla()
                self.charts += [plt.plot(x, y1, label='Channel 1')]
                self.charts += [plt.plot(x, y2, label='Channel 2')]

                plt.legend(loc='upper left')
                plt.tight_layout()

        if self.example in ["Animate", "Clear Axis", "Real-Time"]:   
            self.ani = FuncAnimation(plt.gcf(), animate, interval=1000)

        if not self.example in ["Hard Coded", "Animate", "Clear Axis", "Real-Time"]:
            plt.title("Ages of Respondents")
            plt.xlabel('Ages')
            plt.ylabel('Total Respondents')

        if not self.example in ["Real-Time"]:
            plt.tight_layout()

        return [True, plt]
    
    def savePlot(self, file_path):
        plt.savefig(file_path)

    def setAnnotations(self):
        if self.example in ["Real-Time"]: 
            self.gen_data.t1.daemon = True
            self.gen_data.t1.start()
        self.annot.init(self.charts)
    
    def showPlot(self):
        self.setAnnotations()
        plt.show()

if __name__ == "__main__":
    Main(Demo)