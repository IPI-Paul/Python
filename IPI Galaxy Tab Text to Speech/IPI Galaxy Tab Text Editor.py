from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *
from PyQt5.QtCore import Qt

class TextEditor(QMainWindow):
	def __init__(self, parent=None):
		super(TextEditor, self).__init__()
		self.editor = QTextEdit()
		self.fontSizeBox = QSpinBox()
		
		font = QFont('Times', 12)
		self.editor.setFont(font)
		
		self.setCentralWidget(self.editor)
		self.setWindowTitle('Rich Text Editor')
		self.showMaximized()
		self.create_tool_bar()
		self.editor.setFontPointSize(12)
		self.path = ""
		
	def create_tool_bar(self):
		toolbar = QToolBar()
		
		open_action = QAction(QIcon('images/open.png'), 'open', self)
		open_action.triggered.connect(self.openFile)
		toolbar.addAction(open_action)
		
		save_action = QAction(QIcon('images/save.png'), 'save', self)
		save_action.triggered.connect(self.saveFile)
		toolbar.addAction(save_action)
		
		preview_action = QAction(QIcon('images/preview.png'), 'preview', self)
		preview_action.triggered.connect(self.preview)
		toolbar.addAction(preview_action)
		
		print_action = QAction(QIcon('images/print.png'), 'print', self)
		print_action.triggered.connect(self.print)
		toolbar.addAction(print_action)
		
		toolbar.addSeparator()
		
		undoBtn = QAction(QIcon('images/undo.png'), 'undo', self)
		undoBtn.triggered.connect(self.editor.undo)
		toolbar.addAction(undoBtn)
		
		redoBtn = QAction(QIcon('images/redo.png'), 'redo', self)
		redoBtn.triggered.connect(self.editor.redo)
		toolbar.addAction(redoBtn)
		
		toolbar.addSeparator()
		
		copyBtn = QAction(QIcon('images/copy.png'), 'copy', self)
		copyBtn.triggered.connect(self.editor.copy)
		toolbar.addAction(copyBtn)
		
		cutBtn = QAction(QIcon('images/cut.png'), 'cut', self)
		cutBtn.triggered.connect(self.editor.cut)
		toolbar.addAction(cutBtn)
		
		pasteBtn = QAction(QIcon('images/paste.png'), 'paste', self)
		pasteBtn.triggered.connect(self.editor.paste)
		toolbar.addAction(pasteBtn)
		
		toolbar.addSeparator()
		
		self.fontBox = QComboBox(self)
		self.fontBox.addItems(["Courier Std", "Hellentic Typewriter Regular", "Helvetica", "Arial", "Times", "Monospace", "Sans Serif"])
		self.fontBox.setCurrentText('Times')
		self.fontBox.activated.connect(self.setFont)
		toolbar.addWidget(self.fontBox)
		
		self.fontSizeBox.setValue(12)
		self.fontSizeBox.valueChanged.connect(self.setFontSize)
		toolbar.addWidget(self.fontSizeBox)
		
		toolbar.addSeparator()
		
		leftAlign = QAction(QIcon('images/left-align.png'), 'Left Align', self)
		leftAlign.triggered.connect(lambda : self.editor.setAlignment(Qt.AlignLeft))
		toolbar.addAction(leftAlign)
		
		centerAlign = QAction(QIcon('images/center-align.png'), 'Center Align', self)
		centerAlign.triggered.connect(lambda : self.editor.setAlignment(Qt.AlignCenter))
		toolbar.addAction(centerAlign)
		
		rightAlign = QAction(QIcon('images/right-align.png'), 'Right Align', self)
		rightAlign.triggered.connect(lambda : self.editor.setAlignment(Qt.AlignRight))
		toolbar.addAction(rightAlign)
		
		toolbar.addSeparator()
		
		boldBtn = QAction(QIcon('images/bold.png'), 'bold', self)
		boldBtn.triggered.connect(self.boldText)
		toolbar.addAction(boldBtn)
		
		italicBtn = QAction(QIcon('images/italic.png'), 'italic', self)
		italicBtn.triggered.connect(self.italicText)
		toolbar.addAction(italicBtn)
		
		underlineBtn = QAction(QIcon('images/underline.png'), 'underline', self)
		underlineBtn.triggered.connect(self.underlineText)
		toolbar.addAction(underlineBtn)
		
		toolbar.addSeparator()
		
		indentBtn = QAction(QIcon('images/indent.gif'), 'indent', self)
		indentBtn.triggered.connect(self.indent)
		toolbar.addAction(indentBtn)
		
		outdentBtn = QAction(QIcon('images/outdent.gif'), 'outdent', self)
		outdentBtn.triggered.connect(self.outdent)
		toolbar.addAction(outdentBtn)
		
		self.addToolBar(toolbar)
		
	def boldText(self):
		weight = QFont.Bold if self.editor.fontWeight() != QFont.Bold else QFont.Normal
		self.editor.setFontWeight(weight)
	
	def file_saveas(self):
		exts, file_types = self.get_filters()
		self.path, ext = QFileDialog.getSaveFileName(self, "Save File", "", file_types)
		try:
			idx = True if self.path.index('.') >= 0 else False
		except Exception as e:
			idx = False
		if not ext.endswith(r'*)') and not idx and self.path != '':
			self.path += f".{exts[ext]}"
		return self.path
		
	def get_blocks(self):
		cursor = self.editor.textCursor()
		selectionStart = cursor.selectionStart()
		selectionEnd = cursor.selectionEnd()
		
		cursor.setPosition(selectionStart)
		startBlock = cursor.blockNumber()
		cursor.setPosition(selectionEnd)
		endBlock = cursor.blockNumber()
		
		if endBlock < startBlock:
		      startBlock, endBlock = endBlock, startBlock
		return cursor, selectionStart, startBlock, endBlock
	
	def get_filters(self):
		file_types = ""
		types = [["Text", "txt"], ["Initialisation" , "ini"], ["Log", "log"], ["Python", "py"], ["JavaScript", "js"], ["HTML", "html"],
		["VbScript", "vbs"], ["Configuration", "conf"], ["All", "*"]]
		exts = {}
		for desc, type in sorted(types):
			file_types += f"{desc} Files (*.{type});;"
			exts[f"{desc} Files (*.{type})"] = type
		return exts, file_types
	
	def indent(self):
		cursor, selectionStart, startBlock, endBlock = self.get_blocks()
		cursor.setPosition(selectionStart)
		cursor.movePosition(QTextCursor.StartOfLine)
		cursor.insertText('\t')
		
		for blockNumber in range(startBlock, endBlock):
			cursor.movePosition(QTextCursor.NextBlock)
			cursor.movePosition(QTextCursor.StartOfLine)
			cursor.insertText('\t')
		
	def italicText(self):
		state = self.editor.fontItalic()
		self.editor.setFontItalic(not(state))
	
	def openFile(self):
		file_types = self.get_filters()[1]
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		self.path, _ = QFileDialog.getOpenFileName(self, "Open File", "", file_types, options=options)
		try:
			with open(self.path, 'r') as f:
				text = f.readlines()
				self.editor.setText(''.join(text))
		except Exception as e:
			self.editor.setText(e.args[0])
	
	def outdent(self):
		cursor, selectionStart, startBlock, endBlock = self.get_blocks()
		cursor.setPosition(selectionStart)
		cursor.movePosition(QTextCursor.StartOfLine)
		cursor.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor)
		if cursor.selectedText() == "\t":
			cursor.removeSelectedText()
		
		for blockNumber in range(startBlock, endBlock):
			cursor.movePosition(QTextCursor.NextBlock)
			cursor.movePosition(QTextCursor.StartOfLine)
			cursor.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor)
			if cursor.selectedText() == "\t":
				cursor.removeSelectedText()

	def print(self):
	     dialog = QPrintDialog()
	     if dialog.exec_() == QDialog.Accepted:
	     	self.editor.document().print_(dialog.printer())

	def preview(self):
	     dialog = QPrintPreviewDialog()
	     dialog.paintRequested.connect(self.editor.print_)
	     dialog.exec_()
	
	def saveFile(self):
		if self.path == "":
			if self.file_saveas() == "":
				return
		text = self.editor.toPlainText()
		try:
			with open(self.path, 'w') as f:
				f.write(text)
		except Exception as e:
			print(e)
	
	def setFont(self):
		font = self.fontBox.currentText()
		self.editor.setFont(QFont(font))
	
	def setFontSize(self):
		value = self.fontSizeBox.value()
		self.editor.setFontPointSize(value)
	
	def underlineText(self):
		state = self.editor.fontUnderline()
		self.editor.setFontUnderline(not(state))
	

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = TextEditor()
	window.show()
	sys.exit(app.exec_())