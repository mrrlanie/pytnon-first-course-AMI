# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Chooser(object):
    def setupUi(self, Chooser):
        Chooser.setObjectName("Chooser")
        Chooser.resize(296, 276)
        self.centralwidget = QtWidgets.QWidget(Chooser)
        self.centralwidget.setObjectName("centralwidget")
        self.chicken = QtWidgets.QCheckBox(self.centralwidget)
        self.chicken.setGeometry(QtCore.QRect(10, 10, 171, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.chicken.setFont(font)
        self.chicken.setObjectName("chicken")
        self.spin_chicken = QtWidgets.QSpinBox(self.centralwidget)
        self.spin_chicken.setGeometry(QtCore.QRect(240, 20, 42, 22))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.spin_chicken.setFont(font)
        self.spin_chicken.setObjectName("spin_chicken")
        self.spin_Cola = QtWidgets.QSpinBox(self.centralwidget)
        self.spin_Cola.setGeometry(QtCore.QRect(240, 60, 42, 22))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.spin_Cola.setFont(font)
        self.spin_Cola.setObjectName("spin_Cola")
        self.spin_Burgers = QtWidgets.QSpinBox(self.centralwidget)
        self.spin_Burgers.setGeometry(QtCore.QRect(240, 140, 42, 22))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.spin_Burgers.setFont(font)
        self.spin_Burgers.setObjectName("spin_Burgers")
        self.spin_Ice_cream = QtWidgets.QSpinBox(self.centralwidget)
        self.spin_Ice_cream.setGeometry(QtCore.QRect(240, 100, 42, 22))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.spin_Ice_cream.setFont(font)
        self.spin_Ice_cream.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.spin_Ice_cream.setObjectName("spin_Ice_cream")
        self.Burgers = QtWidgets.QCheckBox(self.centralwidget)
        self.Burgers.setGeometry(QtCore.QRect(10, 130, 141, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Burgers.setFont(font)
        self.Burgers.setObjectName("Burgers")
        self.Ice_cream = QtWidgets.QCheckBox(self.centralwidget)
        self.Ice_cream.setGeometry(QtCore.QRect(10, 90, 241, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Ice_cream.setFont(font)
        self.Ice_cream.setObjectName("Ice_cream")
        self.Cola = QtWidgets.QCheckBox(self.centralwidget)
        self.Cola.setGeometry(QtCore.QRect(10, 50, 171, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Cola.setFont(font)
        self.Cola.setObjectName("Cola")
        self.OUTPUT = QtWidgets.QPushButton(self.centralwidget)
        self.OUTPUT.setGeometry(QtCore.QRect(60, 190, 151, 31))
        self.OUTPUT.setObjectName("OUTPUT")
        Chooser.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Chooser)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 296, 21))
        self.menubar.setObjectName("menubar")
        self.menuClear = QtWidgets.QMenu(self.menubar)
        self.menuClear.setFocusPolicy(QtCore.Qt.NoFocus)
        self.menuClear.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.menuClear.setObjectName("menuClear")
        self.menuExit = QtWidgets.QMenu(self.menubar)
        self.menuExit.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.menuExit.setObjectName("menuExit")
        Chooser.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Chooser)
        self.statusbar.setObjectName("statusbar")
        Chooser.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuClear.menuAction())
        self.menubar.addAction(self.menuExit.menuAction())

        self.retranslateUi(Chooser)
        QtCore.QMetaObject.connectSlotsByName(Chooser)

    def retranslateUi(self, Chooser):
        _translate = QtCore.QCoreApplication.translate
        Chooser.setWindowTitle(_translate("Chooser", "Выбор"))
        self.chicken.setText(_translate("Chooser", "Крылышки (200р)"))
        self.Burgers.setText(_translate("Chooser", "Бургер (149 р)"))
        self.Ice_cream.setText(_translate("Chooser", "Мороженное рожок (70 р)"))
        self.Cola.setText(_translate("Chooser", "Напиток (99 р)"))
        self.OUTPUT.setText(_translate("Chooser", "I`M DONE"))
        self.menuClear.setTitle(_translate("Chooser", "Clear"))
        self.menuExit.setTitle(_translate("Chooser", "Exit"))