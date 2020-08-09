from PyQt5 import QtWidgets
from PyQt5 import QtPrintSupport
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys, os, design

zero_error = 'Делить на 0' + '\n' + 'нельзя !'
uncorrect = 'Неправильная' + '\n' + 'запись!'

 
class Calculator(QtWidgets.QMainWindow, design.Ui_Calculator):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #кнопки 0 - 9

        self.button_0.clicked.connect(self.print_l)
        self.button_1.clicked.connect(self.print_l)
        self.button_2.clicked.connect(self.print_l)
        self.button_3.clicked.connect(self.print_l)
        self.button_4.clicked.connect(self.print_l)
        self.button_5.clicked.connect(self.print_l)
        self.button_6.clicked.connect(self.print_l)
        self.button_7.clicked.connect(self.print_l)
        self.button_8.clicked.connect(self.print_l)
        self.button_9.clicked.connect(self.print_l)

        
        self.div.clicked.connect(self.print_l)
        self.mul.clicked.connect(self.print_l)
        self.sub.clicked.connect(self.print_l)
        self.add.clicked.connect(self.print_l)
        self.back_d.clicked.connect(self.print_l)
        self.normal_d.clicked.connect(self.print_l)
  

        self.equal.clicked.connect(self.calc)
        self.clear.clicked.connect(self.res)

    def print_l(self):
        if self.Output.text() == '0' or self.Output.text() == zero_error or self.Output.text() == uncorrect:
            self.Output.setText('')
        sender = self.Output.text() + self.sender().text()
        self.Output.setText(sender)
    
    def calc(self):
        try:
            answer = eval(self.Output.text())
            self.Output.setText(str(answer))
        except ArithmeticError:
            self.Output.setText(str(zero_error))
        except Exception:
            self.Output.setText(uncorrect)

    def res(self):
        self.Output.setText('')

def main():
    app = QtWidgets.QApplication(sys.argv)  
    window = Calculator()  
    window.show()  
    app.exec_()


if __name__ == '__main__': 
    main()  