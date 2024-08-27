from matplotlib import pyplot as plt
from main import Main


class Demo():
    def __init__(self) -> None:
        self.examples = [[1, "First Minute Pie"], [1, "Stack Plot/Area Chart"], [1, "Labelled Stack Plot"], [1, "Legend Repositioned"], 
                         [1, "Custom Colours"], [1, "Developers"]]  

    def run(self, example=1):
        self.plots, self.example = self.examples[example - 1]

        plt.style.use("fivethirtyeight")

        if self.example in ["First Minute Pie", "Stack Plot/Area Chart", "Labelled Stack Plot", "Legend Repositioned", "Custom Colours"]:
            minutes = range(1, 10)
            player1 = [1, 2, 3, 3, 4, 4, 4, 4, 5]
            player2 = [1, 1, 1, 1, 2, 2, 2, 3, 4]
            player3 = [1, 1, 1, 2, 2, 2, 3, 3, 3]

            if self.example in ["Labelled Stack Plot", "Legend Repositioned", "Custom Colours"]:
                labels = ['player1', 'player2', 'player3']
        elif self.example in ["Developers"]:
            days = range(1, 10)
            developer1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
            developer2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
            developer3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]

            labels = ['developer1', 'developer2', 'developer3']
            
        if self.example in ["Custom Colours", "Developers"]:
            colors = ['#6d904f', '#fc4f30', '#008fd5'] 

        if self.example in ["First Minute Pie"]:
            plt.pie([player1[0], player2[0], player3[0]], labels=["Player 1", "Player 2", "Player 3"])
        elif self.example in ["Stack Plot/Area Chart"]:
            plt.stackplot(minutes, player1, player2, player3)
        elif self.example in ["Labelled Stack Plot", "Legend Repositioned"]:
            plt.stackplot(minutes, player1, player2, player3, labels=labels)
        elif self.example in ["Custom Colours"]:
            plt.stackplot(minutes, player1, player2, player3, labels=labels, colors=colors)
        elif self.example in ["Developers"]:
            plt.stackplot(days, developer1, developer2, developer3, labels=labels, colors=colors)

        if self.example in ["Labelled Stack Plot", "Custom Colours"]:
            plt.legend()
        elif self.example in ["Legend Repositioned"]:
            plt.legend(loc='upper left')
        elif self.example in ["Developers"]:
            plt.legend(loc=(0.07, 0.05))

        plt.title("My Awesome Stack Plot")
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