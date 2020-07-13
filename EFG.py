import sys
import time
import sqlite3
from PyQt5 import uic
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QTextEdit, QTableWidgetItem
DEL = False
ANSWERED = False

class MyWindow(QMainWindow):
    data = []
    def __init__(self):
        super().__init__()
        uic.loadUi('efg.ui',self)
        self.con = sqlite3.connect("films.db")
        self.cur = self.con.cursor()
        self.btn.clicked.connect(self.find_name)
        self.btn_find.clicked.connect(self.find1)
        title = ('ID','Название','Год','Продолжительность')
        self.table.setColumnCount(len(title))
        self.table.setRowCount(0)
        self.table.setHorizontalHeaderLabels(title)
        self.table.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Interactive)
        self.table.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        ls = self.cur.execute(f'SELECT * FROM genres').fetchall()
        ls = [elem[1] for elem in ls]
        ls.sort()
        self.combo.addItems(ls)
        self.save.clicked.connect(self.save_func)
        self.dele.clicked.connect(self.del_prep)
        self.add.clicked.connect(self.add_prep)

    def add_prep(self):
        add.show()

    def del_prep(self):
        notice.show()
        
    def save_func(self):
        to_check = []
        from_check = []
        for i in range(len(self.data)):
            ID = self.table.item(i, 0).text()
            NAME = self.table.item(i, 1).text()
            YEAR = self.table.item(i, 2).text()
            DUR = self.table.item(i, 3).text()
            to_check.append((ID, NAME, YEAR, DUR))
            ID1 = str(self.data[i][0])
            NAME1 = str(self.data[i][1])
            YEAR1 = str(self.data[i][2])
            DUR1 = str(self.data[i][4])
            from_check.append((ID1, NAME1, YEAR1, DUR1))
        for elem in to_check:
            if elem not in from_check:
                self.cur.execute(f'UPDATE films SET title = \'{elem[1]}\', duration = \'{elem[2]}\', year = \'{elem[3]}\' WHERE id = \'{elem[0]}\'')
        self.con.commit()

    def find_name(self):
        name = self.name.text()
        self.data = self.cur.execute(f'SELECT * FROM Films WHERE Title LIKE \'%{name}%\'').fetchmany(100)
        self.prnt()

    def find1(self):
        dur = self.dur.text().isnumeric()
        year = self.year.text().isnumeric()
        f = self.combo.currentText()
        reguest = ''
        if f == 'не выбрано':
            reguest = 'SELECT * FROM Films'
            if dur or year:
                reguest += " WHERE "
            if dur:
                txt = self.dur.text()
                reguest += f'duration = \'{txt}\''
            if dur and year:
                reguest += " AND "
            if year:
                txt = self.year.text()
                reguest += f'year = \'{txt}\''
        else:
            ID = self.cur.execute(f'SELECT * FROM Genres WHERE title = \'{f}\'').fetchall()
            reguest = f'SELECT * FROM Films WHERE genre = \'{ID[0][0]}\''
            if dur:
                txt = self.dur.text()
                reguest += f' AND duration = \'{txt}\''
            if year:
                txt = self.year.text()
                reguest += f' AND year = \'{txt}\''
        self.data = self.cur.execute(reguest).fetchmany(100)
        self.prnt()

    def prnt(self):
        self.table.setRowCount(0)
        for i, line in enumerate(self.data):
                self.table.setRowCount(self.table.rowCount() + 1)
                item = QTableWidgetItem(str(line[0]))
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.table.setItem(i, 0, item)
                self.table.setItem(i, 1, QTableWidgetItem(line[1]))
                self.table.setItem(i, 2, QTableWidgetItem(str(line[2])))
                self.table.setItem(i, 3, QTableWidgetItem(str(line[4])))
        self.table.resizeColumnsToContents()
        
class Notice(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('notice.ui',self)
        self.btn_yes.clicked.connect(self.yes)
        self.btn_no.clicked.connect(self.no)

    def yes(self):
        global DEL 
        global ANSWERED
        ANSWERED = True
        DEL = True
        del_func()
        self.close()

    def no(self):
        global DEL
        global ANSWERED
        ANSWERED = True
        DEL = False
        self.close()

def del_func():
        global ANSWERED
        global DEL
        indexes = main.table.selectionModel().selectedRows()
        indexes.sort()
        if ANSWERED and DEL:
            for i in range(len(indexes)-1, -1, -1):
                main.cur.execute(f'DELETE from films WHERE id = \'{main.data[indexes[i].row()][0]}\'')
                main.table.removeRow(indexes[i].row())
        main.con.commit()
        ANSWERED = False
        DEL = False

class Add(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('add.ui',self)
        self.btn.clicked.connect(self.final)
        ls = main.cur.execute(f'SELECT * FROM genres').fetchall()
        ls = [elem[1] for elem in ls]
        ls.sort()
        self.combo.addItems(ls)

    def final(self):
        add_func()
        self.close()
        

def add_func():
    f = add.combo.currentText()
    GENRE = main.cur.execute(f'SELECT * FROM Genres WHERE title = \'{f}\'').fetchall()
    NAME = add.name.text()
    DUR = add.dur.text()
    YEAR = add.year.text()
    if len(GENRE) != 0 and len(NAME) != 0 and len(DUR) != 0 and len(YEAR) != 0:
        main.cur.execute(f'INSERT INTO films(title,duration,genre,year) VALUES(\'{NAME}\',\'{DUR}\',\'{GENRE[0][0]}\',\'{YEAR}\')')
    add.name.clear()
    add.dur.clear()
    add.year.clear()
    main.con.commit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MyWindow()
    main.show()
    notice = Notice()
    add = Add()
    sys.exit(app.exec_())