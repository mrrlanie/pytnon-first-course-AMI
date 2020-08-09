import sys, os, design
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtPrintSupport
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *


class HtmlEditor(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.parse_text)
    
    def parse_text(self): #перевод текста в html
        textbox = self.INPUT 
        text = textbox.toPlainText()   
        self.OUTPUT.setText(text)

def main():
    app = QtWidgets.QApplication(sys.argv) 
    window = HtmlEditor()
    window.show() 
    app.exec_()

if __name__ == '__main__':
    main()