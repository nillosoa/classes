
import sys
from PyQt5.QtWidgets import (
	QWidget, QApplication,
	QHBoxLayout, QVBoxLayout,
	QPushButton, QLabel, QLineEdit)


class MainWindow(QWidget):

	def __init__(self):
		super().__init__()
		self.init_ui()

	def init_ui(self):

		label = QLabel("Name")
		name_input = QLineEdit()
		button = QPushButton("Set name")

		H = QHBoxLayout()
		H.addWidget(label)
		H.addWidget(name_input)

		V = QVBoxLayout()
		V.addLayout(H)
		V.addWidget(button)

		self.setLayout(V)
		self.setWindowTitle("Horizontal layout")
		self.show()


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	sys.exit(app.exec_())