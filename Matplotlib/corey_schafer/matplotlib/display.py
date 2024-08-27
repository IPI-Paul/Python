import re
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView, QWebEnginePage
import base64
from mpl_demo_01_line_plots import Demo as Demo_1
from mpl_demo_02_bar_charts import Demo as Demo_2
from mpl_demo_03_pie_charts import Demo as Demo_3
from mpl_demo_04_stack_plots import Demo as Demo_4
from mpl_demo_05_line_plot_fills import Demo as Demo_5
from mpl_demo_06_histograms import Demo as Demo_6
from mpl_demo_07_scatter_plots import Demo as Demo_7
from mpl_demo_08_time_series_line_plots import Demo as Demo_8
from mpl_demo_09_line_plot_real_time import Demo as Demo_9
from mpl_demo_10_subplots import Demo as Demo_10
from canvas import Canvas
from context_menu import CustomWebView, SourceViewer



class Display(QMainWindow):
    # constructor
    def __init__(self, *args, **kwargs):
        super(Display, self).__init__(*args, **kwargs)
        self.parent = kwargs['parent'] if kwargs and 'parent' in kwargs else self
        self.central_layout = QVBoxLayout()
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.central_layout)
        self.plt = None

        self.examples = []
        demos = [Demo_1, Demo_2, Demo_3, Demo_4, Demo_5, Demo_6, Demo_7, Demo_8, Demo_9, Demo_10]
        for idx, cls in enumerate(demos):
            demo = cls()
            self.examples += [[idx, demo, demo.examples]]

        self.options = ['Line Plot', 'Bar Chart', 'Pie Chart', 'Stack Plot', 'Line Plot Fill', 'Histogram', 'Scatter Plot', 'Time Series Line Plot', 'Line Plot Real Time', 'Sub plot']

        # size the window
        if kwargs and 'geometry' in kwargs:
            self.setGeometry(kwargs['geometry'])
        else:
            self.setGeometry(100, 100, 950, 500)
        # default text
        self.my_page = """
<html>
    <head>
        <style> 
            table, td {padding: 5px; border: 1pt; font-size: 9pt} 
            h2 { text-align: center } 
            th { background-color: navy; color: white; } 
        </style>
    </head>
    <body>
        <h2>Use this Python App to View Charts.</h2>
    </body>
</html>
        """
        self.regex = re.compile(r"(?=\<\/body\>)")
        self.groups = self.regex.split(self.my_page.strip())
            
        self.browser = None
        self.canvas = None
        self.show_browser()

        # creating QToolbar for navigation
        # adding this toolbar to the main window
        navtb = QToolBar("Navigation")
        self.addToolBar(navtb)

        # creating a status bar object
        # adding status bar to the main window
        self.status = QStatusBar()
        self.setStatusBar(self.status)
        self.status_text = QLabel()
        self.status.addPermanentWidget(self.status_text)
        self.status_text.setMinimumWidth(75)

        self.functions = QComboBox()
        self.functions.addItems([''])
        self.demos = []
        ids = 0
        num = 0
        for example in self.examples:
            idx, demo, examples = example
            for itm in examples:
                if ids != idx:
                    ids = idx
                    num = 1
                else:
                    num += 1
                self.demos += [[idx, demo, num]]
                plots, caption = itm
                self.functions.addItems([f"{self.options[idx]}: {plots} plot{'' if plots == 1 else 's'}{' using ' + caption if caption != '' else ''}"])
        self.functions.currentIndexChanged.connect(lambda x: self.run_function(x))
        self.functions.setMaxVisibleItems(50)
        navtb.addWidget(self.functions)

        self.btn = QCheckBox('Save and Show', self)
        self.btn.setStyleSheet("""
            QCheckBox {
                margin-left: 20px;
            }
        """)
        navtb.addWidget(self.btn)

        self.show()

    def run_function(self, idx):
        folder_path = "../../../../../Source Files/"
        if idx != 0:
            if not self.plt is None and type(self.plt).__name__ != 'list':
                self.plt.close('all')
                self.plt.style.use('default')
            self.status_text.setText(self.functions.currentText())
            self.central_layout.removeWidget(self.canvas)
            self.central_layout.removeWidget(self.browser)
            ids, src, ex = self.demos[idx - 1] 
            ok, self.plt = src.run(ex)
            if not ok:  
                html = "<table><tr><th>Type</th><th>Output</th></tr>"
                for out in self.plt:
                    html += f"<tr><td>{type(out).__name__}</td><td>{out}</td></tr>"
                html += "</table>"
                self.show_browser()
                self.browser.setHtml(html)
            else:
                src.setAnnotations()
                self.canvas = Canvas(self, self.plt.gcf())
                if not self.btn.isChecked():
                    self.central_layout.addWidget(self.canvas)
                else:  
                    demo, _, demos = self.examples[ids]
                    plots, caption = demos[ex - 1]
                    file_path = f"{folder_path}png/{self.options[demo]} - {plots} plot{'' if plots == 1 else 's'}{' using ' + caption.replace('/', '-') if caption != '' else ''}.png"
                    src.savePlot(file_path)
                    with open(file_path, 'rb') as f:
                        img = f.read()
                    img = base64.b64encode(img).decode('utf-8')
                    new_groups = self.regex.split(self.my_page)
                    new_groups[0] = re.compile(r"(?=\<h2\>)").split(self.groups[0])[0]
                    img = f"data:image/png;base64, {img}"
                    style = '''
                    .container {
                        display: flex;
                        flex-direction: column;
                        justify-items: center;
                        align-items: center;
                        margin: 0;
                    }
                    img {
                        width: auto;
                        height: 95vh;
                    }
                </style>
                    '''
                    new_groups[0] = new_groups[0].replace(r'</style>', style)
                    new_groups[0] += f"<div class='container'><img src='{img}' /></div>"
                    self.show_browser()
                    self.browser.setHtml(new_groups[0] + new_groups[1])
                    self.canvas = None
        if idx != 0:
            self.functions.setCurrentIndex(0)

    def show_browser(self, clean=True):
        # creating a QWebEngineView
        self.browser = CustomWebView(parent=self)
        # self.browser.titleChanged.connect(self.link_clicked)
        self.browser.pageAction(QWebPage.SavePage).triggered.connect(lambda: self.view_source(QUrl(""), True))
        self.browser.pageAction(QWebPage.ViewSource).triggered.connect(lambda: self.view_source(QUrl("")))

        # sending html to page
        self.browser.setHtml(self.my_page)
        self.browser.page().acceptNavigationRequest(QUrl(""), 0, True)
        # self.browser.page().setLinkDelegationPolicy(QWebPage.DelegateAllLinks)

        # set this browser as central widget on main window
        self.central_layout.addWidget(self.browser)
        self.setCentralWidget(self.central_widget)
    
    def view_source(self, url=QUrl(""), save=False):
        self.source_viewer = SourceViewer(url, save, self)
        if not save:
            self.source_viewer.showSource()
        else:
            self.source_viewer.saveSource()


class QWebPage(QWebEnginePage):
    def acceptNavigationRequest(self, url, navtype, mainframe):
        return False
    

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # creating a pyQt5 application
    sys.argv.append("--disable-web-security")
    app = QApplication(sys.argv)

    # setting name to the application
    app.setApplicationName('IPI Charts')

    # set styles
    app.setStyleSheet("""
        QWidget {
                      font-size: 10px
                }
""")

    # creating a main window object
    window = Display()

    # loop
    app.exec_()
