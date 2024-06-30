import matplotlib.pyplot as plt


class Charts():
    def __init__(self) -> None:  
        self.chart = None
        self.line_info = None

    def bar_chart(self, results=[], xvalues=[], secondary=None, tooltips=[], title="", xlabel="", ylabel=[""], xticks=[], yticks=[], xlabels=[], ylabels=[], 
                  left=None, right=None, top=None, bottom=None, rotation='horizontal'):
        if not results is None: 
            self.secondary = None
            self.tooltips = tooltips
            self.xlabel = xlabel
            self.ylabel = ylabel
            self.xlables = xlabels
            self.ylables = ylabels
            self.fig = plt.figure()
            self.plot = self.fig.add_subplot(111)
            self.chart = plt.bar(xvalues, results)
            if title != "":
                plt.title(title)
            plt.ylabel(ylabel[0])
            plt.xlabel(xlabel)
            if len(ylabels) != 0:
                plt.yticks(yticks, labels=ylabels, size=8)
            elif len(yticks) != 0:
                plt.yticks(yticks, size=8)
            if len(xlabels) != 0:
                plt.xticks(xticks, labels=xlabels, rotation=rotation, size=8)
            elif len(xticks) != 0:
                plt.xticks(xticks, rotation=rotation, size=8)
            else:
                plt.xticks(rotation=rotation, size=8)
            if not left == None:
                plt.subplots_adjust(left=left)
            if not right == None:
                plt.subplots_adjust(right=right)
            if not top == None:
                plt.subplots_adjust(top=top)
            if not bottom == None:
                plt.subplots_adjust(bottom=bottom)
            self.xdata = xvalues
            self.fig.canvas.mpl_connect('motion_notify_event', lambda event, plot="bar": self.on_plot_hover(event, plot))
            self.set_annot()
            if not secondary is None:
                self.plot1 = self.plot.twinx()
                self.plot1.plot(xvalues, secondary, 'b-')
                self.plot1.set_ylabel(ylabel=ylabel[1], color='b')
                self.secondary = secondary
            else:
                self.plot1 = None

    def line_chart(self, results=[], xvalues=[], secondary=None, tooltips=[], title="", xlabel="", ylabel=[""], xticks=[], yticks=[], xlabels=[], ylabels=[], 
                   left=None, right=None, top=None, bottom=None, rotation='horizontal'):
        if not results is None:
            self.secondary = None
            self.tooltips = tooltips
            self.xlabel = xlabel
            self.ylabel = ylabel
            self.xlables = xlabels
            self.ylables = ylabels
            self.fig = plt.figure()
            self.plot = self.fig.add_subplot(111)
            self.chart = plt.plot(xvalues, results)
            if title != "":
                plt.title(title)
            plt.ylabel(ylabel[0])
            plt.xlabel(xlabel)
            plt.grid()
            if len(ylabels) != 0:
                plt.yticks(yticks, labels=ylabels, size=8)
            elif len(yticks) != 0:
                plt.yticks(yticks, size=8)
            if len(xlabels) != 0:
                plt.xticks(xticks, labels=xlabels, rotation=rotation, size=8)
            elif len(xticks) != 0:
                plt.xticks(xticks, rotation=rotation, size=8)
            else:
                plt.xticks(rotation=rotation, size=8)
            if not left == None:
                plt.subplots_adjust(left=left)
            if not right == None:
                plt.subplots_adjust(right=right)
            if not top == None:
                plt.subplots_adjust(top=top)
            if not bottom == None:
                plt.subplots_adjust(bottom=bottom)
            self.ydata = results
            self.xdata = xvalues
            self.fig.canvas.mpl_connect('motion_notify_event', lambda event, plot="line": self.on_plot_hover(event, plot))
            self.set_annot()
    
    def scatter_plot(self, results=[], xvalues=[], secondary=None, tooltips=[], title="", xlabel="", ylabel=[""], xticks=[], yticks=[], xlabels=[], ylabels=[], 
                     left=None, right=None, top=None, bottom=None, rotation='horizontal'):
        if not results is None:
            self.secondary = None
            self.tooltips = tooltips
            self.xlabel = xlabel
            self.ylabel = ylabel
            self.xlables = xlabels
            self.ylables = ylabels
            self.fig = plt.figure()
            self.plot = self.fig.add_subplot(111)
            self.chart = plt.scatter(xvalues, results)
            if title != "":
                plt.title(title)
            plt.ylabel(ylabel[0])
            plt.xlabel(xlabel)
            if len(ylabels) != 0:
                plt.yticks(yticks, labels=ylabels, size=8)
            elif len(yticks) != 0:
                plt.yticks(yticks, size=8)
            if len(xlabels) != 0:
                plt.xticks(xticks, labels=xlabels, rotation=rotation, size=8)
            elif len(xticks) != 0:
                plt.xticks(xticks, rotation=rotation, size=8)
            else:
                plt.xticks(rotation=rotation, size=8)
            if not left == None:
                plt.subplots_adjust(left=left)
            if not right == None:
                plt.subplots_adjust(right=right)
            if not top == None:
                plt.subplots_adjust(top=top)
            if not bottom == None:
                plt.subplots_adjust(bottom=bottom)
            self.ydata = results
            self.xdata = xvalues
            self.fig.canvas.mpl_connect('motion_notify_event', lambda event, plot="scatter": self.on_plot_hover(event, plot))
            self.set_annot()
    
    def on_plot_hover(self, event, tp="bar"):
        vis = self.annot.get_visible
        if tp == "bar" and (event.inaxes == self.plot or event.inaxes == self.plot1):
            for bar in self.chart:
                cont, idx = bar.contains(event)
                if cont:
                    self.update_annot(bar)
                    self.annot.set_visible(True)
                    self.fig.canvas.draw_idle()
                    return
        elif tp == "line":
             if event.inaxes == self.plot:
                  for line in self.chart:
                    cont, ind = line.contains(event)
                    if cont:
                        self.update_annot([ind, line], "line")
                        self.annot.set_visible(True)
                        self.fig.canvas.draw_idle()
                        return
        else:
             if event.inaxes == self.plot:
                cont, ind = self.chart.contains(event)
                if cont:
                    self.update_annot(ind, "scatter")
                    self.annot.set_visible(True)
                    self.fig.canvas.draw_idle()
                    return
        if vis:
            self.annot.set_visible(False)
            self.fig.canvas.draw_idle()

    def save(self, folder_path):
        plt.savefig(f'{folder_path}mygraph.png', dpi=300)

    def set_annot(self):
        self.annot = self.plot.annotate("", xy=(0, 0), xytext=(-20, 20), textcoords="offset points",
                                    bbox=dict(boxstyle="round", fc="black", ec="b", lw=2),
                                    arrowprops=dict(arrowstyle="->"))
        self.annot.set_visible(False)

    def show(self):    
        # Show plot  
        plt.show()

    def update_annot(self, plot, tp="bar"):
        if tp == "bar":
            x = plot.get_x() + plot.get_width() / 2
            y = plot.get_y() + plot.get_height()
            self.annot.xy = (x, y)
            idx = int(x) - 1 if type(self.xdata[int(x) - 1]) == int else int(x)
            x = self.xdata[idx]
        elif tp == "line":
            ind, line = plot
            x, y = line.get_data()
            self.annot.xy = (x[ind["ind"][0]], y[ind["ind"][0]])
        else:
            ind = plot
            pos = self.chart.get_offsets()[ind["ind"][0]]
            self.annot.xy = pos
        if tp == "line":
            x = int("".join(list(map(str, ind["ind"]))))
            y = int("".join(str(self.ydata.iloc[n].iloc[0]) for n in ind["ind"]))
        if tp == "scatter":
            x = ",".join(list(map(str, ind["ind"])))
            x = self.xdata[int(x.split(",")[0])]
            y = ",".join(str(self.ydata.iloc[n]) for n in ind["ind"])
            y = int(y.split(",")[0])
            tooltip = "\n".join(self.tooltips[x][y])
        if not type(x) == str:
            text = "{}: {:.2g}\n{}: {:,.0f}".format(self.xlabel, x, self.ylabel[0], y)
        else:
            text = "{}: {}\n{}: {:,.0f}".format(self.xlabel, x, self.ylabel[0], y)
        if tp == "scatter":
            text += "\n{}".format(tooltip)
        if not self.secondary is None:
            text += "\n{}: {:,.2f}".format(self.ylabel[1], self.secondary.iloc[idx])
        self.annot.set_text(text)
        self.annot.get_bbox_patch().set_alpha(0.4)
        
        
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    win = Charts()