import re
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView, QWebEnginePage
import base64
from analysis import Analysis
from canvas import Canvas



class Display(QMainWindow):
    # constructor
    def __init__(self, *args, **kwargs):
        super(Display, self).__init__(*args, **kwargs)
        self.parent = kwargs['parent'] if kwargs and 'parent' in kwargs else self
        self.central_layout = QVBoxLayout()
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.central_layout)

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
        # adding this status bar to the main window
        navtb = QToolBar("Navigation")
        self.addToolBar(navtb)

        self.functions = QComboBox()
        self.functions.addItems(['', 'Question 1 Object', 'Question 1 Web Image', 'Question 2 Object', 'Question 2 Web Image', 
                                 'Question 3 Object', 'Question 3 Web Image', 'Question 4 Object', 'Question 4 Web Image', 
                                 'Question 5 Object', 'Question 5 Web Image']
                                )
        self.functions.currentIndexChanged.connect(lambda x: self.run_function(x))
        self.functions.setMaxVisibleItems(50)
        navtb.addWidget(self.functions)

        self.show()

    def run_function(self, idx):
        charts = ['question_1', 'question_2', 'question_3', 'question_4', 'question_5']
        dup = []
        folder_path = "../../../../../Source Files/"
        for x in charts:
            dup.append(x)
            dup.append(x)
        if idx != 0:
            self.central_layout.removeWidget(self.canvas)
            self.central_layout.removeWidget(self.browser)
            src = Analysis() 
            eval(f'src.{dup[idx - 1]}("{folder_path}csv/")')
            self.canvas = Canvas(self, src.fig)
        if idx % 2 != 0:
            self.central_layout.addWidget(self.canvas)
        elif idx % 2 == 0 and idx != 0:  
            src.save(f"{folder_path}png/")
            with open(f'{folder_path}png/mygraph.png', 'rb') as f:
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
        self.browser = QWebView()
        # self.browser.titleChanged.connect(self.link_clicked)

        # sending html to page
        self.browser.setHtml(self.my_page)
        self.browser.page().acceptNavigationRequest(QUrl(""), 0, True)
        # self.browser.page().setLinkDelegationPolicy(QWebPage.DelegateAllLinks)

        # set this browser as central widget on main window
        self.central_layout.addWidget(self.browser)
        self.setCentralWidget(self.central_widget)


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
