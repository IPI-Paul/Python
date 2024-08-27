class Main():
    def __init__(self, demo) -> None:
        self.demo = demo()
        self.choice()

    def choice(self):
        choose = True
        while choose:
            self.example = input(f"There are {len(self.demo.examples)} examples!\nWhat example number do you want to run (h + enter to view list): ")
            if self.example.lower() == "h":
                self.help()
            else:
                self.run()
            choose = input("Do you want to run again (y/n): ").lower() == 'y'

    def help(self):
        list = ""
        for idx, demo in enumerate(self.demo.examples):
            plots, caption = demo
            list += f"Example {idx + 1}: Has {plots} plot(s) {'using ' + caption if caption != '' else ''}\n"
        print(list)
        self.choice()

    def run(self):
        plots, caption = self.demo.examples[int(self.example) - 1]
        print(f"Now displaying {plots} plot(s) {'using ' + caption if caption != '' else ''}")
        if self.demo.run(int(self.example))[0]:
            save = input("Do you want to save/show the plot (save/[Enter Key Only]): ")
            if save.lower() == "save":
                folder_path = "../../../../../Source Files/"
                file_path = f"{folder_path}png/plot.png"
                self.demo.savePlot(file_path)
            else:
                self.demo.showPlot()