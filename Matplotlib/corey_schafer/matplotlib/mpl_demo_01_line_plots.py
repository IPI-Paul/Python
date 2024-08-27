from matplotlib import pyplot as plt
from main import Main
from annotations import Annotations

class Demo():
    def __init__(self) -> None:
        self.examples = [[1, ""], [2, "Legends"], [2, "Format Strings"], [2, "Markers"], [2, ""], [2, "Hex Colors"], [3, "Hex Colors"],
                         [3, "Line Width"], [3, "Padding"], [3, "Grid"], [0, "See Styles"], [3, "Five Thirty Eight Style"], 
                         [3, "Five Thirty Eight Style Defaults"], [3, "ggplot Style"], [3, "xkcd Comic Style"], [3, "All Ages xkcd Comic Style"]]
        self.charts = []

    def run(self, example=1):
        self.plots, self.example = self.examples[example - 1]
        if self.example == "See Styles":
            plts = plt
            if __name__ == "__main__":
                print(plt.style.available)
            else:
                plts = plt.style.available

            return [False, plts]
        else:
            if self.example == "Five Thirty Eight Style":
                plt.style.use("fivethirtyeight")
            elif self.example == "ggplot Style":
                plt.style.use("ggplot")
            elif self.example in ["xkcd Comic Style", "All Ages xkcd Comic Style"]:
                plt.xkcd()
            if example < len(self.examples):
                ages_x = range(25, 36)
                dev_y = [38496, 42000, 46752, 49620, 53200,
                        56000, 62316, 64928, 67317, 68748, 73752]
            else:
                ages_x = range(18, 56)
                dev_y = [17784, 16500, 18012, 20628, 25206, 30252, 34368, 38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752, 77232,
                         78000, 78508, 79536, 82488, 88935, 90000, 90056, 95000, 90000, 91633, 91660, 98150, 98964, 100000, 98988, 100000, 108923, 105000, 103117]                
            
            self.annot = Annotations(plts=plt)
                
            if self.example == "Legends" or self.plots == 1:
                self.charts += [plt.plot(ages_x, dev_y)]
            elif self.example == "Format Strings":
                self.charts += [plt.plot(ages_x, dev_y, 'k--', label='All Devs')]
            elif self.example == "Markers":
                self.charts += [plt.plot(ages_x, dev_y, color='k', linestyle='--', marker='.', label='All Devs')]
            elif self.example == "Hex Colors":
                self.charts += [plt.plot(ages_x, dev_y, color='#444444', linestyle='--', label='All Devs')]
            elif self.example in ["Line Width", "Padding", "Grid", "Five Thirty Eight Style", "Five Thirty Eight Style Defaults",
                                  "ggplot Style", "xkcd Comic Style", "All Ages xkcd Comic Style"]:
                pass
            else:
                self.charts += [plt.plot(ages_x, dev_y, color='k', linestyle='--', label='All Devs')]

            if self.plots > 1:
                if example < len(self.examples):
                    py_dev_y = [45372, 48876, 53850, 57287, 63016,
                                65998, 70003, 70000, 71496, 75370, 83640]
                else:
                    py_dev_y = [20046, 17100, 20000, 24744, 30500, 37732, 41247, 45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640, 84666,
                         84392, 78254, 85000, 87038, 91991, 100000, 94796, 97962, 93302, 99240, 102736, 112285, 100771, 104708, 108423, 101407, 112542, 122870, 120000]

                if self.example == "Legends":
                    self.charts += [plt.plot(ages_x, py_dev_y)]
                elif self.example == "Format Strings":
                    self.charts += [plt.plot(ages_x, py_dev_y, 'b', label='Python')]
                elif self.example == "Markers":
                    self.charts += [plt.plot(ages_x, py_dev_y, color='b', marker='o', label='Python')]
                elif self.example == "Hex Colors":
                    self.charts += [plt.plot(ages_x, py_dev_y, color='#5a7d9a', label='Python')]
                elif self.example in ["Line Width", "Padding", "Grid", "Five Thirty Eight Style"]:
                    self.charts += [plt.plot(ages_x, py_dev_y, color='#5a7d9a', linewidth=3, label='Python')]
                elif self.example in ["Five Thirty Eight Style Defaults", "ggplot Style", "xkcd Comic Style", "All Ages xkcd Comic Style"]:
                    self.charts += [plt.plot(ages_x, py_dev_y, label='Python')]
                else:
                    self.charts += [plt.plot(ages_x, py_dev_y, color='b', label='Python')]

            if self.plots > 2:
                if example < len(self.examples):
                    js_dev_y = [37810, 43515, 46823, 49293, 53437,
                                56373, 62375, 66674, 68745, 68746, 74583]
                else:
                    js_dev_y = [16446, 16791, 18942, 21780, 25704, 29000, 34372, 37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583, 79000,
                                78508, 79996, 80403, 83820, 88833, 91660, 87892, 96243, 90000, 99313, 91660, 102264, 100000, 100000, 91660, 99240, 108000, 105000, 104000]
                if self.example == "Hex Colors":
                    self.charts += [plt.plot(ages_x, js_dev_y, color='#adad3b', label='JavaScript')]
                elif self.example in ["Line Width", "Padding", "Grid", "Five Thirty Eight Style"]:
                    self.charts += [plt.plot(ages_x, js_dev_y, color='#adad3b', linewidth=3, label='JavaScript')]
                    self.charts += [plt.plot(ages_x, dev_y, color='#444444', linestyle='--', label='All Devs')]
                elif self.example in ["Five Thirty Eight Style Defaults", "ggplot Style", "xkcd Comic Style", "All Ages xkcd Comic Style"]:
                    self.charts += [plt.plot(ages_x, js_dev_y, label='JavaScript')]
                    self.charts += [plt.plot(ages_x, dev_y, color='#444444', linestyle='--', label='All Devs')]

            plt.xlabel('Ages')
            plt.ylabel('Median Salary (USD)')
            plt.title("Median Salary (USD) by Age")

            if self.example == "Legends":
                plt.legend(['All Devs', 'Python'])
            elif self.plots > 1:
                plt.legend()

            # Add Grid
            if self.example in ["Grid", "Five Thirty Eight Style"]:
                plt.grid(True)

            # Add padding
            if self.example in ["Padding", "Grid", "Five Thirty Eight Style", "Five Thirty Eight Style Defaults", "ggplot Style", "xkcd Comic Style", "All Ages xkcd Comic Style"]:
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