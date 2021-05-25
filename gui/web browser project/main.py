
import os
import sys
import json

from PyQt5.QtWidgets import (
	QApplication,
	QWidget, QVBoxLayout, QHBoxLayout,
	QPushButton, QLabel, QLineEdit,
	QTabBar, QTabWidget, QFrame, QStackedLayout,
	QShortcut, QKeySequenceEdit, QSplitter)
from PyQt5.QtGui import QIcon, QWindow, QImage, QKeySequence
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import * 

class AddressBar(QLineEdit):

	def __init__(self):
		super().__init__()

	def mousePressEvent(self, e):
		self.selectAll()

class Application(QFrame):

	def __init__(self):
		super().__init__()
		self.setWindowTitle("Web Browser")
		#self.setMinimumSize(1366, 768)
		self.setBaseSize(1366, 768)
		self.createApp()

	def createApp(self):
		self.layout = QVBoxLayout()
		self.layout.setSpacing(0)
		self.layout.setContentsMargins(0, 0, 0, 0)

		# Create tabs
		self.tabbar = QTabBar(movable=True, tabsClosable=True)
		self.tabbar.tabCloseRequested.connect(self.CloseTab)
		self.tabbar.tabBarClicked.connect(self.SwitchTab)
		self.tabbar.setDrawBase(False)

		self.tabbar.setCurrentIndex(0)

		self.shortcutNewTab = QShortcut(
								QKeySequence("Ctrl+t"), self)
		self.shortcutNewTab.activated.connect(self.AddTab)

		self.shortcutReload = QShortcut(
								QKeySequence("Ctrl+r"), self)
		self.shortcutReload.activated.connect(self.Reload)

		# Keep track of tabs
		self.tabs = []
		self.tabsCount = 0

		# Create address bar
		self.toolbar = QWidget()
		self.toolbar.setObjectName("toolbar")
		self.toolbarLayout = QHBoxLayout()
		self.addressbar = AddressBar()

		self.addressbar.returnPressed.connect(self.BrowseTo)

		# New tab button
		self.addTabButton = QPushButton("+")
		self.addTabButton.clicked.connect(self.AddTab)

		# Set Toolbar buttons
		self.backButton = QPushButton("<")
		self.backButton.clicked.connect(self.GoBack)

		self.forwardButton = QPushButton(">")
		self.forwardButton.clicked.connect(self.GoForward)

		self.reloadButton = QPushButton("R")
		self.reloadButton.clicked.connect(self.Reload)

		self.toolbar.setLayout(self.toolbarLayout)
		self.toolbarLayout.addWidget(self.backButton)
		self.toolbarLayout.addWidget(self.forwardButton)
		self.toolbarLayout.addWidget(self.reloadButton)
		self.toolbarLayout.addWidget(self.addressbar)
		self.toolbarLayout.addWidget(self.addTabButton)

		# Set main view
		self.container = QWidget()
		self.container.layout = QStackedLayout()
		self.container.setLayout(self.container.layout)

		self.layout.addWidget(self.tabbar)
		self.layout.addWidget(self.toolbar)
		self.layout.addWidget(self.container)

		self.setLayout(self.layout)
		self.AddTab()

		self.show()

	def GoBack(self):
		activeIndex = self.tabbar.currentIndex()
		tab_name = self.tabbar.tabData(activeIndex)['object']
		tab_content = self.findChild(QWidget, tab_name).content

		tab_content.back()

	def GoForward(self):
		activeIndex = self.tabbar.currentIndex()
		tab_name = self.tabbar.tabData(activeIndex)['object']
		tab_content = self.findChild(QWidget, tab_name).content

		tab_content.forward()

	def Reload(self):
		activeIndex = self.tabbar.currentIndex()
		tab_name = self.tabbar.tabData(activeIndex)['object']
		tab_content = self.findChild(QWidget, tab_name).content

		tab_content.reload()

	def CloseTab(self, i):
		self.tabbar.removeTab(i)

	def AddTab(self):
		i = self.tabsCount
		self.tabs.append(QWidget())
		self.tabs[i].layout = QVBoxLayout()
		self.tabs[i].layout.setContentsMargins(0, 0, 0, 0)

		# For tab switching
		self.tabs[i].setObjectName("tab" + str(i))

		# open web view
		self.tabs[i].content = QWebEngineView()
		self.tabs[i].content.load(QUrl.fromUserInput("https://google.com"))

		# self.tabs[i].content1 = QWebEngineView()
		# self.tabs[i].content1.load(QUrl.fromUserInput("https://google.com"))

		self.tabs[i].content.titleChanged.connect(lambda: self.SetTabContent(i, "title"))
		self.tabs[i].content.iconChanged.connect(lambda: self.SetTabContent(i, "icon"))
		self.tabs[i].content.urlChanged.connect(lambda: self.SetTabContent(i, "url"))

		# add webview to tabs layout
		self.tabs[i].splitview = QSplitter()
		self.tabs[i].splitview.setOrientation(Qt.Vertical)
		self.tabs[i].layout.addWidget(self.tabs[i].splitview)

		self.tabs[i].splitview.addWidget(self.tabs[i].content)
		# self.tabs[i].splitview.addWidget(self.tabs[i].content1)

		# set top level tab from [] to layout
		self.tabs[i].setLayout(self.tabs[i].layout)

		# add tab to top level stackwidget
		self.container.layout.addWidget(self.tabs[i])
		self.container.layout.setCurrentWidget(self.tabs[i])

		# set the tab at the top of screen
		self.tabbar.addTab("New Tab")
		self.tabbar.setTabData(i,
			{ "object": "tab" + str(i), "initial": i})
		self.tabbar.setCurrentIndex(i)

		self.tabsCount += 1

	def SwitchTab(self, i):
		if self.tabbar.tabData(i):
			tab_data = self.tabbar.tabData(i)['object']
			tab_content = self.findChild(QWidget, tab_data)

			self.container.layout.setCurrentWidget(tab_content)

			new_url = tab_content.content.url().toString()
			self.addressbar.setText(new_url)

	def BrowseTo(self):
		i = self.tabbar.currentIndex()
		tab = self.tabbar.tabData(i)['object']
		wv = self.findChild(QWidget, tab).content

		text = self.addressbar.text()
		if "http" not in text:
			if "." not in text:
				url = "https://www.google.com/search?q=" + text
			else:
				url = "http://" + text
		else:
			url = text
		wv.load(QUrl.fromUserInput(text))

	def SetTabContent(self, i, type):
		#self.tabbar.addTab("New Tab")
		#self.tabbar.setTabData(i,
		#	{ "object": "tab" + str(i), "initial": i})
		tab_name = self.tabs[i].objectName()

		# tab 1
		count = 0
		running = True

		current_tab = self.tabbar.tabData(self.tabbar.currentIndex())["object"]

		if current_tab == tab_name and type == "url":
			new_url = self.findChild(QWidget, tab_name).content.url().toString()
			self.addressbar.setText(new_url)
			return False

		while running:
			tab_data_name = self.tabbar.tabData(count)

			if count >= 99:
				running = False

			if tab_name == tab_data_name["object"]:
				if type == "title":
					new_title = self.findChild(
							QWidget, tab_name).content.title()
					self.tabbar.setTabText(count, new_title)
				elif type == "icon":
					new_icon = self.findChild(QWidget, tab_name).content.icon()
					self.tabbar.setTabIcon(count, new_icon)

				running = False

			else:
				count += 1


if __name__ == "__main__":
	os.environ["QTWEBENGINE_REMOTE_DEBUGGING"] = "8081"

	app = QApplication(sys.argv)
	window = Application()

	with open("style.css") as style:
		app.setStyleSheet(style.read())

	sys.exit(app.exec_())