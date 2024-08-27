from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class Canvas(FigureCanvas):
    def __init__(self, parent, fig):
        super().__init__(fig)
        self.setParent(parent)