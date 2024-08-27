import pandas as pd
from matplotlib import pyplot as plt
from main import Main
from annotations import Annotations


class Demo():
    def __init__(self) -> None:
        self.examples = [[1, "Hard Coded"], [1, "Sized"], [1, "Coloured"], [1, "Edge Colours"], [1, "Colours List"],
                         [1, "Colour Map"], [1, "Colour Bar"], [1, "Sizes List"], [1, "YouTube API"], [1, "Log Scale"],
                         [1, "Ratio Colours"]]    
        self.charts = [] 

    def run(self, example=1):
        self.plots, self.example = self.examples[example - 1]

        plt.style.use("seaborn-v0_8-colorblind")

        if self.example in ["Hard Coded", "Sized", "Coloured", "Edge Colours", "Colours List", "Colour Map", "Colour Bar", "Sizes List"]:
            x = [5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 2, 6, 3, 6, 8, 6, 4, 1]
            y = [7, 4, 3, 9, 1, 3, 2, 5, 2, 4, 8, 7, 1, 6, 4, 9, 7, 7, 5, 1]
        else:
            data_source = '../../../../../Source Files/csv/corey_sachafer_matplotlib_2_data_4.csv'
            df = pd.read_csv(data_source)
            view_count = df['view_count']
            likes = df['likes']
            ratio = df['ratio']

        if self.example in ["Colours List", "Colour Map", "Colour Bar", "Sizes List"]:
            colors = [7, 5, 9, 7, 5, 7, 2, 5, 3, 7, 1, 2, 8, 1, 9, 2,5, 6, 7, 5]

        if self.example in ["Sizes List"]:
            sizes = [209, 486, 381, 255, 191, 315, 185, 228, 174, 
                     538, 239, 394, 399, 153, 273, 293, 436, 501, 397, 539]        
            
        self.annot = Annotations(plts=plt)

        if self.example in ["Hard Coded"]:
            self.charts += [plt.scatter(x, y)]
        elif self.example in ["Sized"]:
            self.charts += [plt.scatter(x, y, s=100)]
        elif self.example in ["Coloured"]:
            self.charts += [plt.scatter(x, y, s=100, c='green', marker='X')]
        elif self.example in ["Edge Colours"]:
            self.charts += [plt.scatter(x, y, s=100, c='green', edgecolor='black', linewidth=1, alpha=0.75)]
        elif self.example in ["Colours List"]:
            self.charts += [plt.scatter(x, y, s=100, c=colors, edgecolor='black', linewidth=1, alpha=0.75)]
        elif self.example in ["Colour Map", "Colour Bar"]:
            self.charts += [plt.scatter(x, y, s=100, c=colors, cmap='Greens', edgecolor='black', linewidth=1, alpha=0.75)]
        elif self.example in ["Sizes List"]:
            self.charts += [plt.scatter(x, y, s=sizes, c=colors, cmap='Greens', edgecolor='black', linewidth=1, alpha=0.75)]
        elif self.example in ["YouTube API", "Log Scale"]:
            self.charts += [plt.scatter(view_count, likes, edgecolor='black', linewidth=1, alpha=0.75)]
        elif self.example in ["Ratio Colours"]:
            self.charts += [plt.scatter(view_count, likes, c=ratio, cmap='summer', edgecolor='black', linewidth=1, alpha=0.75)]

        if self.example in ["Colour Bar", "Sizes List"]:
            cbar = plt.colorbar()
            cbar.set_label('Satisfaction')
        elif self.example in ["Ratio Colours"]:
            cbar = plt.colorbar()
            cbar.set_label('Like/Dislike Ratio')

        if self.example in ["Log Scale", "Ratio Colours"]:
            plt.xscale('log')
            plt.yscale('log')

        if not self.example in ["Hard Coded", "Sized", "Coloured", "Edge Colours", "Colours List", "Colour Map", "Colour Bar", "Sizes List"]:
            plt.title("Trending YouTube Videos")
            plt.xlabel('View Count')
            plt.ylabel('Total Likes')

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