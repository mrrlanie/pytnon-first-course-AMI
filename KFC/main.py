import sys, os, design
import check_design
from PyQt5 import QtWidgets
from PyQt5 import QtPrintSupport
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import re
import random
import datetime


class HtmlEditor(QtWidgets.QMainWindow, design.Ui_Chooser):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.OUTPUT.clicked.connect(self.run)
        self.menuExit.triggered.connect(self.app_exit)
        self.menuClear.triggered.connect(self.reset)
        self.dialog = Dialog()
        self.basket = []

    def check_field(self, obj, spin):
        return obj.isChecked() or spin.value() != 0

    def get_item_name(self, obj):
        return re.search('\w+', obj.text()).group()

    def get_item_price(self, obj):
        return int(re.search('\d+', obj.text()).group())

    def add_to_basket(self, obj, spin):
        name = self.get_item_name(obj)
        price_per_one = self.get_item_price(obj)
        count = spin.value()
        if count == 0 and obj.isChecked():
            count = 1
        self.basket.append((name, count, price_per_one * count))

    def check_all(self):
        objs = (
            (self.chicken, self.spin_chicken),
            (self.Cola, self.spin_Cola),
            (self.Ice_cream, self.spin_Ice_cream),
            (self.Burgers, self.spin_Burgers),
        )
        for obj, spin in objs:
            if self.check_field(obj, spin):
                self.add_to_basket(obj, spin)

    def run(self):
        self.basket = []
        self.show_dialog()
        self.generate_receipt_head()
        self.check_all()
        self.print_check()


    def show_dialog(self):
        self.dialog.show()

    def print_check(self):
        for item, count, price in self.basket: 
            self.dialog.textBrowser.append((f"<br><hr><ul><li>{item} X {count} = {price} ₽</li>"))
        self.print_final_price()

    def print_final_price(self):
        self.dialog.textBrowser.append((f"<br><hr> ИТОГО:{sum(k[2] for k in self.basket)} ₽"))

    def generate_receipt_head(self):
        self.dialog.textBrowser.setText(('<hr><h5 align="center">Ваш номер заказа в очереди</h5>'))
        self.dialog.textBrowser.append((f"<h1> {random.randint(100, 999)}</h1>"))
        time = datetime.datetime.now()
        time = time.strftime("%H:%M %d-%m-%Y")
        self.dialog.textBrowser.append((f"Время: {time}"))

    
    def app_exit(self):
        self.action_exit = sys.exit()

    def reset(self):
        self.chicken.setCheckState(False)
        self.Cola.setCheckState(False)
        self.ice.setCheckState(False)
        self.Burgers.setCheckState(False)
        self.spinBox.setValue(0)
        self.spinBox_2.setValue(0)
        self.spinBox_3.setValue(0)
        self.spinBox._4setValue(0)


        

class Dialog(QtWidgets.QDialog, check_design.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv) 
    window = HtmlEditor() 
    window.show()
    app.exec_()


if __name__ == '__main__':  
    main()  

u_t = "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt;\">Продукция KFC рекомендуется для потребления на территории предприятия</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">------------------------------------------------------------------</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Ваш номер заказа в очереди</span></p></body></html>"