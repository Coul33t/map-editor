# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1087, 849)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView_map = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_map.setGeometry(QtCore.QRect(280, 10, 512, 512))
        self.graphicsView_map.setObjectName("graphicsView_map")
        self.graphicsView_tileset = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_tileset.setGeometry(QtCore.QRect(10, 10, 256, 512))
        self.graphicsView_tileset.setObjectName("graphicsView_tileset")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1087, 26))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionImport_tileset = QtWidgets.QAction(MainWindow)
        self.actionImport_tileset.setObjectName("actionImport_tileset")
        self.actionImport_map = QtWidgets.QAction(MainWindow)
        self.actionImport_map.setObjectName("actionImport_map")
        self.menuMenu.addAction(self.actionImport_tileset)
        self.menuMenu.addAction(self.actionImport_map)
        self.menuMenu.addSeparator()
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionImport_tileset.setText(_translate("MainWindow", "Import tileset"))
        self.actionImport_map.setText(_translate("MainWindow", "Import map"))

