# Import the required module for text
# to speech conversion
from gtts import gTTS

# These modules are imported so that we can
# play the converted audio
from PyQt5 import QtCore, QtMultimedia
from PyQt5.QtWidgets import QApplication
import os
import sys


def main():
	# The text that you want to convert to audio
	mytext = clipboard.text() # 'Anything goes' #entry1.get()

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
	# os.system("mpg321 welcome.mp3")

	CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
	player = QtMultimedia.QMediaPlayer()
	
	def handle_state_changed(state):
	  	         if state == QtMultimedia.QMediaPlayer.PlayingState:
	  	         	print("started")
	  	         elif state == QtMultimedia.QMediaPlayer.StoppedState:
	  	         	print("finished")
	  	         	QtCore.QCoreApplication.quit()
            
            
	filename = os.path.join(CURRENT_DIR, "welcome.mp3")
	app = QtCore.QCoreApplication(sys.argv)
	player.stateChanged.connect(handle_state_changed)

	url = QtCore.QUrl.fromLocalFile(filename)
	player.setMedia(QtMultimedia.QMediaContent(url))
	player.play()

	sys.exit(app.exec_())

if __name__ == "__main__":
	print(sys.argv[0])
	app1 = QApplication(sys.argv)
	clipboard = app1.clipboard()
	main()