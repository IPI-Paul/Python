from io import StringIO
from os import system
from PyQt5.QtNetwork import QNetworkRequest, QNetworkAccessManager
from PyQt5 import QtWebEngineWidgets
from PyQt5.QtCore import Qt, QUrl, QTextStream
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QFileDialog, QLineEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView, QWebEnginePage
import pandas as pd

pd.options.display.width = 0


class SaveFiles():
    def file_save(self, default=""):
        exts, file_types = self.get_filters(default)
        self.path, ext = QFileDialog.getSaveFileName(self, "Save File", "", file_types)
        try:
            idx = True if self.path.index('.') >= 0 else False
        except Exception as e:
            idx = False
        if not ext.endswith(r'*)') and not idx and self.path != '':
            self.path += f".{exts[ext]}"
        return self.path

    def get_filters(self, default=""):
        file_types = ""
        types = [["Text", "txt"], ["Initialisation", "ini"], ["Log", "log"], ["Python", "py"], ["JavaScript", "js"],
                 ["HTML", "html"], ["VbScript", "vbs"], ["Configuration", "conf"], ["All", "*"], ["CSV", "csv"]]
        exts = {}
        for desc, ext in sorted(types):
            if default == "":
                file_types += f"{desc} Files (*.{ext});;"
                exts[f"{desc} Files (*.{ext})"] = ext
            elif default == desc:
                file_types += f"{desc} Files (*.{ext});;"
                exts[f"{desc} Files (*.{ext})"] = ext
        return exts, file_types


class CustomWebView(QWebView, SaveFiles):
    def __init__(self, parent=None, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.parent = parent
    
    def contextMenuEvent(self, event):
        self.menu = self.page().createStandardContextMenu()
        
        self.find_option = self.menu.addAction('Find Text')
        self.find_option.setIcon(QIcon("./images/preview.png"))
        self.find_option.triggered.connect(self.searchText)

        self.excel = self.menu.addAction('Export to Excel')
        self.excel.setIcon(QIcon("./images/excel.png"))
        self.excel.triggered.connect(self.sendToExcel)

        self.menu.popup(event.globalPos())
    
    def find(self):
        view: QWebView = self.parent.browser
        view.page().findText(self.text_to_find.text(), QWebEnginePage.FindFlags(0))

    def getDataFrame(self, html):
        text = []
        for line in html.splitlines():
            if line.__contains__('title="Watched"'):
                line = line.replace("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;", "Watched")
            if line.__contains__('&nbsp;&nbsp;+&nbsp;&nbsp;'):
                line = line.replace("&nbsp;&nbsp;+&nbsp;&nbsp;", "")
            text += [line]
        text = '''
        '''.join(text)
        df = pd.read_html(StringIO(text))
        df = df[0]
        df.fillna("", inplace=True)   
        df = df.rename({'Unnamed: 4': 'Status'}, axis=1)   
        if self.file_save("CSV") == "":
            return
        df.to_csv(self.path, ",", index_label=False, index=False)
        system('start excel && "' + self.path + '"')

    def searchText(self):
        self.search = QMainWindow()
        self.search.setWindowTitle("Find Text")
        self.text_to_find = QLineEdit(self)
        self.text_to_find.returnPressed.connect(self.find)
        toolbar = self.search.addToolBar("Search Bar")
        toolbar.addWidget(self.text_to_find)
        self.search.setAttribute(Qt.WA_DeleteOnClose)
        self.search.setGeometry(25, 25, 250, 20)
        self.search.show()
    
    def sendToExcel(self):
        view: QWebView = self.parent.browser
        view.page().toHtml(self.getDataFrame)


class SourceViewer(QMainWindow, SaveFiles):
    accessManager = QNetworkAccessManager()

    def __init__(self, url=QUrl(""), save=False, parent=None) -> None:
        super(SourceViewer, self).__init__()
        self.parent = parent
        self.text = ""
        self.view = QWebView(self)
        self.url = url
        self.path = ""

        # Change Network Access Manager
        if not save:
            self.accessManager.finished.connect(self.showSource)
        else:
            self.accessManager.finished.connect(self.saveSource)
    
    def saveText(self, text):
        try:
            with open(self.path, 'w') as f:
                f.write(text)
        except Exception as e:
            print(e)

    # Save source code
    def saveSource(self):        
        if self.file_save("HTML") == "":
            return
        view: QWebView = self.parent.browser
        view.page().toHtml(self.saveText)

    # View source code
    def viewSource(self):
        request = QNetworkRequest(self.url())
        self.reply = self.accessManager.get(request)
        self.view.reload()

    def showSource(self):
        self.textEdit = QTextEdit()
        font = QFont()
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setAttribute(Qt.WA_DeleteOnClose)
        self.textEdit.setGeometry(25, 25, 1000, 800)
        self.textEdit.show()
        view: QWebView = self.parent.browser
        view.page().toHtml(self.textEdit.setPlainText)
        self.deleteLater()