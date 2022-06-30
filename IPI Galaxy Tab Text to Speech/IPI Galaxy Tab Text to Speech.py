# Import the required module for text
# to speech conversion
from gtts import gTTS

# These modules are imported so that we can
# play the converted audio
from PyQt5 import QtMultimedia, QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os
import sys


class TTSWindow(QMainWindow, QApplication):
    # constructor
    def __init__(self, *args, **kwargs):
        super(TTSWindow, self).__init__(*args, **kwargs)
        
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
        
        self.player = None
        self.show()
        
    def pause(self):
    	self.player.pause()
    	
    	
    def play(self):
        self.player = QtMultimedia.QMediaPlayer()
        
        # The text that you want to convert to audio
        mytext = self.clipboard().text() # 'Anything goes' #entry1.get()
			
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
			
				# Playing the converted file
        CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
        filename = os.path.join(CURRENT_DIR, "welcome.mp3")
        
        url = QtCore.QUrl.fromLocalFile(filename)
        self.player.setMedia(QtMultimedia.QMediaContent(url))
        self.player.play()
		

    def quit(self):
    	QtCore.QCoreApplication.quit()
    	
    	
    def resume(self):
    	self.player.play()
			
									
if __name__ == "__main__":
	app = QApplication(sys.argv)
	app.setApplicationName('IPI Galaxy Tab Text to Speech')
	ttsWindow = TTSWindow()
	
	# loop
	app.exec_()
