# Import the required module for text
# to speech conversion
from gtts import gTTS

# These modules are imported so that we can
# play the converted audio
from PyQt5 import QtMultimedia, QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtPrintSupport import *
import os
import sys
import re
rte = __import__('IPI Galaxy Tab Text Editor')


class TTSWindow(QMainWindow, QApplication):
    # constructor
    def __init__(self, *args, **kwargs):
        super(TTSWindow, self).__init__(*args, **kwargs)
        self.grid = QWidget()

        # size the window
        self.setMinimumWidth(950)
        # self.setMinimumHeight(800)
        
        # creating QToolbar for navigation
        # adding this status bar to the main window
        navtb = QToolBar("Navigation")
        self.addToolBar(navtb)
        
        playBtn = QPushButton("Play", self)
        playBtn.clicked.connect(self.play)
        navtb.addWidget(playBtn)
        
        pauseBtn = QPushButton("Pause", self)
        pauseBtn.clicked.connect(self.pause)
        navtb.addWidget(pauseBtn)
        
        quitBtn = QPushButton("Quit", self)
        quitBtn.clicked.connect(self.quit)
        
        resumeBtn = QPushButton("Resume", self)
        resumeBtn.clicked.connect(self.resume)
        navtb.addWidget(resumeBtn)
        navtb.addWidget(quitBtn)
        
        searchBtn = QPushButton("Find mp3s", self)
        searchBtn.clicked.connect(self.find_mp3s)
        navtb.addWidget(searchBtn)
        
        viewBtn = QPushButton("View/Edit Text Files", self)
        viewBtn.clicked.connect(self.edit_files)
        navtb.addWidget(viewBtn)
        
        self.player = None
        self.show()
        
    def edit_files(self):
    	self.setCentralWidget(rte.TextEditor(self))
    
    def find_mp3s(self):
       self.layout = QGridLayout()
       pattern = re.compile('.*\.(mp3|MP3)$')
       mp3s = []
       for root, dirnames, filenames in os.walk('/storage'):
             try:
             	for filename in filter(lambda name:pattern.match(name),filenames):
             		mp3s.append(os.path.join(root, filename))
             except:
             	pass
       
       for root, dirnames, filenames in os.walk('/storage/emulated/0'):
       	for filename in filter(lambda name:pattern.match(name),filenames):
       		mp3s.append(os.path.join(root, filename))
       
       rowNum = 0
       colNum = 0
       btnNum = 0
       self.buttons = {}
       for mPath in mp3s:
       	if colNum == 5:
       		colNum = 0
       		rowNum += 1
       	
       	self.buttons[btnNum] = QToolButton(self)
       	
       	label = QLabel(mPath, self.buttons[btnNum])
       	label.setFixedSize(350, 150)
       	label.setFont(QFont('Arial', 10))
       	label.setWordWrap(True)
       	
       	self.buttons[btnNum].setFixedSize(350, 150)
       	self.buttons[btnNum].clicked.connect(lambda state, x=mPath: self.play_file(x))
       	self.layout.addWidget(self.buttons[btnNum], rowNum, colNum)
       	colNum += 1
       	btnNum += 1
       self.grid.setLayout(self.layout)
       self.setCentralWidget(self.grid)
    
    def pause(self):
    	self.player.pause()
    	
    def play(self):
        self.player = QtMultimedia.QMediaPlayer()
        
        # The text that you want to convert to audio
        mytext = self.clipboard().text() # 'Anything goes' #entry1.get()
        self.save(mytext)
				
				# Playing the converted file
        CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
        filename = os.path.join(CURRENT_DIR, "welcome.mp3")
        
        url = QtCore.QUrl.fromLocalFile(filename)
        self.player.setMedia(QtMultimedia.QMediaContent(url))
        self.player.play()

    def play_file(self, mp3):
    	url = QtCore.QUrl.fromLocalFile(mp3)
    	self.player = QtMultimedia.QMediaPlayer()
    	self.player.setMedia(QtMultimedia.QMediaContent(url))
    	self.player.play()
    
    def quit(self):
    	QtCore.QCoreApplication.quit()
    	
    def resume(self):
    	self.player.play()
    
    def save(self, mytext):
    	# Language in which you want to convert
        language = 'en'
			
				# Passing the text and language to the engine,
				# here we have marked slow=False. Which tells
				# the module that the converted audio should
				# have a high speed
        myobj = gTTS(text=mytext, lang=language, slow=False)
			
				# Saving the converted audio in a mp3 file named
				# welcome
        myobj.save("welcome.mp3")
									
if __name__ == "__main__":
	app = QApplication(sys.argv)
	app.setApplicationName('IPI Galaxy Tab Text to Speech')
	ttsWindow = TTSWindow()
	
	# loop
	app.exec_()
	
