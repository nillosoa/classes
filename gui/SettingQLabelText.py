
import sys
from PyQt5.QtWidgets import (
	QWidget, QApplication,
	QHBoxLayout, QVBoxLayout,
	QPushButton, QLabel, QLineEdit)


class MainWindow(QWidget):

	def __init__(self):
		super().__init__()
		self.init_ui()
		self.counter = 0

	def init_ui(self):
		self.text_label = QLabel("There has been no name entered so I can't do anything yet.") 
		self.label = QLabel("Name")
		self.name_input = QLineEdit()
		self.button = QPushButton("Clicked: @")

		self.button.setText("Set name")
		self.button.clicked.connect(self.alterName)

		H = QHBoxLayout()
		H.addWidget(self.label)
		H.addWidget(self.name_input)

		V = QVBoxLayout()
		V.addWidget(self.text_label)
		V.addLayout(H)
		V.addWidget(self.button)

		self.setLayout(V)
		self.setWindowTitle("Nothing has been clicked")
		self.show()

	def alterName(self):
		inputted_text = self.name_input.text()
		our_string = "You entered: " + inputted_text
		self.text_label.setText(our_string)
		self.setWindowTitle(inputted_text + "'s Window")

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	sys.exit(app.exec_())