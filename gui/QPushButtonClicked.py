
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

		label = QLabel("Name")
		name_input = QLineEdit()
		self.button = QPushButton("Clicked")
		# button.clicked.connect(self.clickedButton)
		self.button.pressed.connect(self.pressButton)
		self.button.released.connect(self.clickedButton)

		H = QHBoxLayout()
		H.addWidget(label)
		H.addWidget(name_input)

		V = QVBoxLayout()
		V.addLayout(H)
		V.addWidget(self.button)

		self.setLayout(V)
		self.setWindowTitle("Horizontal layout")
		self.show()

	def pressButton(self):
		print("Button is being pressed.")

	def clickedButton(self):
		self.counter += 1
		self.button.setText("Clicked: " + str(self.counter))

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	sys.exit(app.exec_())