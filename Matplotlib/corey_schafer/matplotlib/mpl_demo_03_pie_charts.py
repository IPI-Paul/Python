from matplotlib import pyplot as plt
from main import Main


class Demo():
    def __init__(self) -> None:
        self.examples = [[1, "Slices"], [1, "Labels"], [1, "Edge Colors"], [1, "Coloured"], [1, "Hex Colours"], [1, "Snippets"], [1, "Snippets Top 5"],
                         [1, "Explode List"], [1, "Shadowed"], [1, "Starting Angle"], [1, "Percentages"]]    

    def run(self, example=1):
        self.plots, self.example = self.examples[example - 1]

        plt.style.use("fivethirtyeight")

        if self.example in ["Slices"]:
            slices = [60, 40]
        elif self.example in ["Labels", "Edge Colors"]:
            slices = [120, 80]
            labels = ['Sixty', 'Forty']
        elif self.example in ["Coloured", "Hex Colours"]:
            slices = [120, 80, 30, 20]
            labels = ['Sixty', 'Forty', 'Extra1', 'Extra2']
            if self.example == "Coloured":
                colors = ['blue', 'red', 'yellow', 'green']
            elif self.example == "Hex Colours":
                colors = ['#008fd5', '#fc4f30', '#e5ae37', '#6d904f']
        elif self.example in ["Snippets", "Snippets Top 5", "Explode List", "Shadowed", "Starting Angle", "Percentages"]:
            slices = [59219, 55466, 47544, 36443, 35917, 31991, 27097,
                      23030, 20524, 18523, 18017, 7920, 7331, 7201, 5833]
            labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java', 'Bash/Shell/Powershell',
                      'C#', 'PHP', 'C++', 'TypeScript', 'C', 'Other(s)', 'Ruby', 'Go', 'Assembly']
            if self.example in ["Snippets Top 5", "Explode List", "Shadowed", "Starting Angle", "Percentages"]:
                slices = slices[0:5]
                labels = labels[0:5]
            if self.example in ["Explode List", "Shadowed", "Starting Angle", "Percentages"]:
                explode = [0, 0, 0, 0.1, 0]

        if self.example in ["Slices"]:
            plt.pie(slices)
        elif self.example in ["Labels"]:
            plt.pie(slices, labels=labels)
        elif self.example in ["Edge Colors", "Snippets", "Snippets Top 5"]:
            plt.pie(slices, labels=labels, wedgeprops={'edgecolor': 'black'})
        elif self.example in ["Coloured", "Hex Colours"]:
            plt.pie(slices, labels=labels, colors=colors, wedgeprops={'edgecolor': 'black'})
        elif self.example in ["Explode List"]:
            plt.pie(slices, labels=labels, explode=explode, wedgeprops={'edgecolor': 'black'})
        elif self.example in ["Shadowed"]:
            plt.pie(slices, labels=labels, explode=explode, shadow=True, wedgeprops={'edgecolor': 'black'})
        elif self.example in ["Starting Angle"]:
            plt.pie(slices, labels=labels, explode=explode, shadow=True, startangle=90, wedgeprops={'edgecolor': 'black'})
        elif self.example in ["Percentages"]:
            plt.pie(slices, labels=labels, explode=explode, shadow=True, startangle=90, autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'})

        plt.title("My Awesome Pie Chart")
        plt.tight_layout()

        return [True, plt]
    
    def savePlot(self, file_path):
        plt.savefig(file_path)

    def setAnnotations(self):
        pass
    
    def showPlot(self):
        plt.show()

if __name__ == "__main__":
    Main(Demo)