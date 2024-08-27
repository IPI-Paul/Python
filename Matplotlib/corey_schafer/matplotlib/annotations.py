import matplotlib.pyplot as plt


class Annotations():
    def __init__(self, plts: plt=None, fig=None, plot=None, tooltips=[]) -> None:
        self.plt = plts
        self.fig = fig if not fig is None else self.plt.gcf()
        self.plot = plot if not plot is None else self.fig.add_subplot(111)
        self.tooltips = tooltips
    
    def init(self, charts=None, xlabel=None, ylabel=None, xdata=[], ydata=[]):
        self.charts = charts
        self.xlabel = xlabel if not xlabel is None else self.plt.gca().get_xlabel() if self.plt.gca().get_xlabel() else 'x-axis'
        self.ylabel = ylabel if not ylabel is None else [self.plt.gca().get_ylabel()] if self.plt.gca().get_ylabel() else ['y-axis']
        self.xdata = xdata
        self.ydata = ydata
        self.fig.canvas.mpl_connect('motion_notify_event', lambda event: self.on_plot_hover(event))
        self.set_annot()
    
    def on_plot_hover(self, event):
        vis = self.annot.get_visible
        for chart in self.charts:
            if type(chart).__name__ == "PathCollection":
                tp = "PathCollection"
            else:
                tp = type(chart[0]).__name__
            if tp in ["Rectangle"] and (event.inaxes == self.plot): 
                self.x_data = []
                for bar in chart:self.x_data += [bar.get_x() + bar.get_width() / 2]
                for bar in chart:
                    cont, idx = bar.contains(event)
                    if cont:
                        self.update_annot(chart, bar)
                        self.annot.set_visible(True)
                        self.fig.canvas.draw_idle()
                        return
            elif tp in ["Line2D", "PolyCollection"]:
                if event.inaxes == self.plot:
                    for line in chart:
                        cont, ind = line.contains(event)
                        if cont:
                            self.update_annot(chart, [ind, line], "line")
                            self.annot.set_visible(True)
                            self.fig.canvas.draw_idle()
                            return
            elif tp in ["PathCollection"]:
                if event.inaxes == self.plot:
                    cont, ind = chart.contains(event)
                    if cont:
                        self.update_annot(chart, ind, "scatter")
                        self.annot.set_visible(True)
                        self.fig.canvas.draw_idle()
                        return
            else:
                return
        if vis:
            self.annot.set_visible(False)
            self.fig.canvas.draw_idle()

    def set_annot(self):
        self.annot = self.plot.annotate("", xy=(0, 0), xytext=(-20, 20), textcoords="offset points",
                                    bbox=dict(boxstyle="round", fc="black", ec="b", lw=2),
                                    arrowprops=dict(arrowstyle="->"))
        self.annot.set_visible(False)

    def update_annot(self, chart, plot, tp="bar"):
        legend = ""
        if tp == "bar":
            x = plot.get_x() + plot.get_width() / 2
            y = plot.get_y() + plot.get_height()
            self.annot.xy = (x, y)
            try:
                if plot.axes.get_legend() or not plot.axes.get_legend() is None:legend = plot.axes.get_legend().texts[self.charts.index(chart)].get_text()
            except:
                pass
            if not self.ylabel == '' and not len(self.ydata) == 0:
                y = self.ydata[int(y)]
                x = self.xdata[self.x_data.index(x)]
            elif not len(self.xdata) == 0:x = self.xdata[self.x_data.index(x)]
        elif tp == "line":
            ind, line = plot
            x, y = line.get_data()
            self.annot.xy = (x[ind["ind"][0]], y[ind["ind"][0]])
        else:
            ind = plot
            pos = chart.get_offsets()[ind["ind"][0]]
            self.annot.xy = pos
        if tp == "line":
            x = ",".join(list(map(str, ind["ind"])))
            x = plot[1].get_xdata()[int(x.split(",")[0])]
            y = float("".join(str(plot[1].get_ydata()[n]) for n in ind["ind"]))
            if plot[1].axes and not plot[1].axes.get_legend() is None:
                legend = plot[1].axes.get_legend().texts[plot[1].axes.get_lines().index(plot[1])].get_text()
        if tp == "scatter":
            x, y = chart.get_offsets()[ind["ind"][0]]
            if chart.axes.get_legend():
                legend = chart.axes.get_legend().texts[self.charts.index(chart)].get_text()
        if not type(x).__name__ in ["str", "datetime", "datetime64"]:
            text = "{}\n{}: {:,.0f}\n{}: {:,.0f}".format(legend, self.xlabel, x, self.ylabel[0], y)
        else:
            text = "{}\n{}: {}\n{}: {:,.0f}".format(legend, self.xlabel, x, self.ylabel[0], y)
        self.annot.set_text(text)
        self.annot.get_bbox_patch().set_alpha(0.4)