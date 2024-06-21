import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from line_charts import LineCharts
from bar_charts import BarCharts
from rw_box_plot import BoxPlots
from rw_line_charts import LineCharts as RWLineCharts
from rw_histogram import Histogram
from rw_pie_charts import PieCharts
from rw_simple_pie_charts import SimplePieCharts


class Canvas(FigureCanvas):
    def __init__(self, parent):
        self.fig, self.plt = plt.subplots(figsize=(15, 6))
        super().__init__(self.fig)
        self.setParent(parent)
        self.chart = None

    def bar_chart(self):
        super().__init__(self.fig)
        self.chart = BarCharts()

    def line_chart(self):
        super().__init__(self.fig)
        # Basic Graph
        self.chart = LineCharts()

    def rw_box_plot(self):
        super().__init__(self.fig)
        self.chart = BoxPlots()

    def rw_histogram(self):
        super().__init__(self.fig)
        self.chart = Histogram()

    def rw_line_chart(self):
        super().__init__(self.fig)
        self.chart = RWLineCharts()

    def rw_pie_chart(self):
        super().__init__(self.fig)
        self.chart = PieCharts()

    def rw_simple_pie_chart(self):
        super().__init__(self.fig)
        self.chart = SimplePieCharts()

        
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    win = RWLineCharts()
    win.show()