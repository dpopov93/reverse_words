#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Program for reverse text in one string
and pasting in second string.

Contents GUI PyQt5

Author: Denis Popov
E-mail: spidermind93@gmail.com
Created: 08.11.2017
"""

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QGridLayout, QApplication

class MainWindow(QWidget):
	
	def __init__(self):
		super().__init__()
		
		self.initUI()
		
	def initUI(self):
		
		source = QLabel('Source:')
		result = QLabel('Result:')
		
		global sourceEdit, resultEdit
		sourceEdit = QLineEdit()
		resultEdit = QLineEdit()
		
		buttonSubmit = QPushButton('Reverse text')
		buttonSubmit.clicked.connect(self.submitButtonClicked)
		
		grid = QGridLayout()
		grid.setSpacing(10)
		
		grid.addWidget(source, 1, 0)
		grid.addWidget(sourceEdit, 1, 1, 1, 4)
		grid.addWidget(result, 2, 0)
		grid.addWidget(resultEdit, 2, 1, 1, 4)
		grid.addWidget(buttonSubmit, 3, 4, 1, 1)
		
		self.setLayout(grid)
		self.setWindowTitle('Reverse words')
		self.show()
		
	def submitButtonClicked(self):
		#print(sourceEdit.text())
		resultEdit.setText(self.reverseText(sourceEdit.text()))
	
	def reverseText(self, someText):
		tmpString = str()
		index = len(someText)
		while index:
			index -= 1
			tmpString += someText[index]
		return tmpString
		
		
if __name__ == '__main__':
	
	app = QApplication(sys.argv)
	win = MainWindow()
	sys.exit(app.exec_())