#!/usr/bin/python
#conding=utf-8

#中文

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qsci import *
from util import ReadStyleSheet
import sys

class ScintillaEditor(QWidget):
	"""docstring for Scintilla"""

	scintilla = None
	font = None
	fontmetrics = None

	def __init__(self,parent=None):
		super(ScintillaEditor, self).__init__(parent)

		self.__init_window__()
		self.__init_ui__()
		self.__layout__()

		self.scintilla.textChanged.connect(self.textChanged)
		self.scintilla.linesChanged.connect(self.linesChanged)

	def linesChanged(self):
		print(self.scintilla.lines())
		self.scintilla.setMarginWidth(0, self.fontmetrics.width(str(self.scintilla.lines())) + 5)
		pass

	def textChanged(self):
		print("textChanged")
		pass

	def keyPressEvent(self,event):
		print("keyPressEvent")

	def __layout__(self):
		self.layout = QVBoxLayout()
		self.layout.setAlignment(Qt.AlignVCenter)
		self.layout.setContentsMargins(0,0,0,0)
		self.layout.setSpacing(0)
		self.layout.addWidget(self.label,False,Qt.AlignVCenter)
		self.layout.addWidget(self.scintilla)
		self.setLayout(self.layout)

	def __init_ui__(self):
		self.__init_scintilla__()
		self.__init_label__()

	def __init_label__(self):
		self.label = QLabel("Coder")
		self.label.setAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
		self.label.setMinimumSize(0,30)

	def __init_window__(self):
		self.setWindowTitle("Coder")
		self.setMinimumSize(800,500)

		#set window no border
		#self.setWindowFlags(Qt.FramelessWindowHint)

		self.font = QFont()
		self.font.setFamily("Microsoft YaHei UI Light")
		self.font.setPointSize(10)
		self.font.setFixedPitch(True)
		self.setFont(self.font)

		self.fontmetrics = QFontMetrics(self.font)

	def __init_scintilla__(self):

		self.scintilla = QsciScintilla()
		self.scintilla.setUtf8(True)

		self.scintilla.setFont(self.font)
		self.scintilla.setMarginsFont(self.font)

		#set line number width
		self.scintilla.setMarginWidth(0, self.fontmetrics.width(str(self.scintilla.lines())) + 5)
		self.scintilla.setMarginLineNumbers(0, True)

		#mesure line
		self.scintilla.setEdgeMode(QsciScintilla.EdgeLine)
		self.scintilla.setEdgeColumn(150)
		self.scintilla.setEdgeColor(QColor("#BBB8B5"))

		#brace match
		self.scintilla.setBraceMatching(QsciScintilla.StrictBraceMatch)

		#current line color
		self.scintilla.setCaretLineVisible(True)
		self.scintilla.setCaretLineBackgroundColor(QColor("#2D2D2D"))
		self.scintilla.setCaretForegroundColor(QColor("white"))

		#selection color
		self.scintilla.setSelectionBackgroundColor(QColor("#606060"))
		self.scintilla.setSelectionForegroundColor(QColor("#FFFFFF"))

		#table relative
		self.scintilla.setIndentationsUseTabs(True)
		self.scintilla.setIndentationWidth(4)
		self.scintilla.setTabIndents(True)
		self.scintilla.setAutoIndent(True)
		self.scintilla.setBackspaceUnindents(True)
		self.scintilla.setTabWidth(4)

		#indentation guides
		self.scintilla.setIndentationGuides(True)

		#line number margin color
		self.scintilla.setMarginsBackgroundColor(QColor("#272727"))
		self.scintilla.setMarginsForegroundColor(QColor("#CCCCCC"))

		#folding margin
		self.scintilla.setFolding(QsciScintilla.PlainFoldStyle)
		self.scintilla.setMarginWidth(2,12)
		#marker
		self.scintilla.markerDefine(QsciScintilla.Minus,QsciScintilla.SC_MARKNUM_FOLDEROPEN)
		self.scintilla.markerDefine(QsciScintilla.Plus,QsciScintilla.SC_MARKNUM_FOLDER)
		self.scintilla.markerDefine(QsciScintilla.Minus,QsciScintilla.SC_MARKNUM_FOLDEROPENMID)
		self.scintilla.markerDefine(QsciScintilla.Plus,QsciScintilla.SC_MARKNUM_FOLDEREND)
		
		#marker define color
		self.scintilla.setMarkerBackgroundColor(QColor("#FFFFFF"),QsciScintilla.SC_MARKNUM_FOLDEREND)
		self.scintilla.setMarkerForegroundColor(QColor("#272727"),QsciScintilla.SC_MARKNUM_FOLDEREND)
		self.scintilla.setMarkerBackgroundColor(QColor("#FFFFFF"),QsciScintilla.SC_MARKNUM_FOLDEROPENMID)
		self.scintilla.setMarkerForegroundColor(QColor("#272727"),QsciScintilla.SC_MARKNUM_FOLDEROPENMID)
		#self.scintilla.setMarkerBackgroundColor(QColor("#FFFFFF"),QsciScintilla.SC_MARKNUM_FOLDERMIDTAIL)
		#self.scintilla.setMarkerForegroundColor(QColor("#272727"),QsciScintilla.SC_MARKNUM_FOLDERMIDTAIL)
		#self.scintilla.setMarkerBackgroundColor(QColor("#FFFFFF"),QsciScintilla.SC_MARKNUM_FOLDERTAIL)
		#self.scintilla.setMarkerForegroundColor(QColor("#272727"),QsciScintilla.SC_MARKNUM_FOLDERTAIL)
		self.scintilla.setMarkerBackgroundColor(QColor("#FFFFFF"),QsciScintilla.SC_MARKNUM_FOLDERSUB)
		self.scintilla.setMarkerForegroundColor(QColor("#272727"),QsciScintilla.SC_MARKNUM_FOLDERSUB)
		self.scintilla.setMarkerBackgroundColor(QColor("#FFFFFF"),QsciScintilla.SC_MARKNUM_FOLDER)
		self.scintilla.setMarkerForegroundColor(QColor("#272727"),QsciScintilla.SC_MARKNUM_FOLDER)
		self.scintilla.setMarkerBackgroundColor(QColor("#FFFFFF"),QsciScintilla.SC_MARKNUM_FOLDEROPEN)
		self.scintilla.setMarkerForegroundColor(QColor("#272727"),QsciScintilla.SC_MARKNUM_FOLDEROPEN)
		self.scintilla.setFoldMarginColors(QColor("#272727"),QColor("#272727"))

		#whitespace
		self.scintilla.setWhitespaceVisibility(QsciScintilla.WsInvisible)
		self.scintilla.setWhitespaceSize(2)
		"""
		the default margin is:

		0: line number,width is not zero
		1: width is zero
		2: folding, width is not zero

		"""
		self.scintilla.setMarginWidth(1,0)

		#set lexer
		self.lexer = QsciLexerPython()
		self.lexer.setFont(self.font)
		self.lexer.setColor(QColor("#ffffff"))
		self.scintilla.setLexer(self.lexer)

		#high light code
		self.lexer.setColor(QColor("#ffffff"))
		self.lexer.setPaper(QColor("#333333"))
		self.lexer.setColor(QColor("#5BA5F7"),QsciLexerPython.ClassName)
		self.lexer.setColor(QColor("#FF0B66"),QsciLexerPython.Keyword)
		self.lexer.setColor(QColor("#00FF40"),QsciLexerPython.Comment)
		self.lexer.setColor(QColor("#BD4FE8"),QsciLexerPython.Number)
		self.lexer.setColor(QColor("#F1E607"),QsciLexerPython.DoubleQuotedString)
		self.lexer.setColor(QColor("#F1E607"),QsciLexerPython.TripleSingleQuotedString)
		self.lexer.setColor(QColor("#F1E607"),QsciLexerPython.TripleDoubleQuotedString)
		self.lexer.setColor(QColor("#F1E607"),QsciLexerPython.DoubleQuotedString)
		self.lexer.setColor(QColor("#04F452"),QsciLexerPython.FunctionMethodName)
		self.lexer.setColor(QColor("#FFFFFF"),QsciLexerPython.Operator)
		self.lexer.setColor(QColor("#FFFFFF"),QsciLexerPython.Identifier)
		self.lexer.setColor(QColor("#F1E607"),QsciLexerPython.CommentBlock)
		self.lexer.setColor(QColor("#F1E607"),QsciLexerPython.UnclosedString)
		self.lexer.setColor(QColor("#F1E607"),QsciLexerPython.HighlightedIdentifier)
		self.lexer.setColor(QColor("#F1E607"),QsciLexerPython.Decorator)

		self.scintilla.setText(open("Editor.py",encoding="UTF8").read())
		self.scintilla.setMarginWidth(0, self.fontmetrics.width(str(self.scintilla.lines())) + 5)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = ScintillaEditor()
	scrollbar = ReadStyleSheet.ReadStyleSheetFile("stylesheet/scrollbar.css")
	scintilla = ReadStyleSheet.ReadStyleSheetFile("stylesheet/scintilla.css")
	common = ReadStyleSheet.ReadStyleSheetFile("stylesheet/common.css")
	stylesheet = scrollbar + scintilla + common
	window.setStyleSheet(stylesheet)
	window.show()
	app.exec_()
	sys.exit()		