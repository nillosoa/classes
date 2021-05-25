
import sys
import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Button():
	def __init__(self, text, results):
		self.b = QPushButton(
						text)
		self.text = text
		self.results = results
		self.b.clicked.connect(lambda:
								self.handleInput(self.text))

	def handleInput(self, v):
		if v == "=":
			self.results.setText(
							str(eval(
								self.results.text())))
		elif v == "AC":
			self.results.setText("")
		elif v == "√":
			value = float(self.results.text())
			self.results.setText(str(math.sqrt(value)))
		elif v == "DEL":
			current_value = self.results.text()
			self.results.setText(current_value[:-1])
		else:
			current_value = self.results.text()
			new_value = current_value + str(v)
			self.results.setText(new_value)


class Application(QWidget):

	def __init__(self):
		super().__init__()
		self.setWindowTitle("Calculator")
		self.createApp()

	def createApp(self):

		# Create our grid
		grid = QGridLayout()

		results = QLineEdit()

		buttons = ["AC", "√", "DEL", "/",
					7, 8, 9, "*",
					4, 5, 6, "-",
					1, 2, 3, "+",
					0, ".", "=" ]

		col = 0
		row = 1

		grid.addWidget(results, 0, 0, 1, 4)

		for button in buttons:
			if col > 3:
				col = 0
				row += 1

			buttonObj = Button(str(button), results)

			if button == 0:
				grid.addWidget(buttonObj.b, row, col, 1, 2)
				col += 1
			else:
				grid.addWidget(buttonObj.b, row, col, 1, 1)

			col += 1

		self.setLayout(grid)

		self.show()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = Application()

	sys.exit(app.exec_())