# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from PIL import Image, ImageQt
import numpy as np
from math import floor

class Ui_MainWindow(object):
    def __init__(self):
        self.path_to_tileset = None
        self.tileset = None
        self.tiles = []
        self.imageLabel_tileset = QtWidgets.QLabel()
        self.current_selected_tile = None
        self.map_drawing = QtGui.QPainter()
        self.selected_tileset_overlay_dark = Image.open('selected_tile_overlay_dark.png').convert('RGB')
        self.selected_tileset_overlay_light = Image.open('selected_tile_overlay_light.png').convert('RGB')

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1087, 849)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea_tileset = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_tileset.setGeometry(QtCore.QRect(10, 10, 256, 512))
        self.scrollArea_tileset.setWidgetResizable(True)
        self.scrollArea_tileset.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea_tileset.setObjectName("scrollArea_tileset")
        self.scrollAreaWidgetContents_tileset = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_tileset.setGeometry(QtCore.QRect(0, 0, 254, 510))
        self.scrollAreaWidgetContents_tileset.setObjectName("scrollAreaWidgetContents_tileset")
        self.scrollArea_tileset.setWidget(self.scrollAreaWidgetContents_tileset)
        self.scrollArea_map = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_map.setGeometry(QtCore.QRect(280, 10, 512, 512))
        self.scrollArea_map.setWidgetResizable(True)
        self.scrollArea_map.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea_map.setObjectName("scrollArea_map")
        self.scrollAreaWidgetContents_map = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_map.setGeometry(QtCore.QRect(0, 0, 510, 510))
        self.scrollAreaWidgetContents_map.setObjectName("scrollAreaWidgetContents_map")
        self.scrollArea_map.setWidget(self.scrollAreaWidgetContents_map)
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

        self.link_components()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionImport_tileset.setText(_translate("MainWindow", "Import tileset"))
        self.actionImport_map.setText(_translate("MainWindow", "Import map"))

    def link_components(self):
        self.actionImport_tileset.triggered.connect(self.import_tileset)
        self.imageLabel_tileset.mousePressEvent = self.select_tile

    def import_tileset(self):
        string = QtWidgets.QFileDialog.getOpenFileName(filter="Image Files (*.png *.jpg *.bmp)")
        self.path_to_tileset = string[0]

        if not self.path_to_tileset:
            return

        self.tileset = Image.open(self.path_to_tileset).convert('RGB')

        size_str = self.path_to_tileset.split('/')[-1].split('.')[0].split('_')[-1].split('x')

        try:
            self.tile_size = [int(size_str[0]), int(size_str[1])]
        except ValueError:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText(f"Error: tileset name must end with the size of tiles (MxN). Example: \" mytileset_64x64.png\"")
            msg.exec_()
            return

        self.tileset = ImageQt.ImageQt(self.tileset)
        self.imageLabel_tileset.setPixmap(QtGui.QPixmap.fromImage(self.tileset))

        self.scrollArea_tileset.setWidget(self.imageLabel_tileset)

        self.selected_tileset_overlay_dark.resize((self.tile_size[0], self.tile_size[1]))
        self.selected_tileset_overlay_light.resize((self.tile_size[0], self.tile_size[1]))

        self.split_tileset()

    def split_tileset(self):
        tileset_size = (self.tileset.size().height, self.tileset.size().width)

        for i in range(tileset_size[0]):
            for j in range(tileset_size[1]):
                #TODO
                pass

    def import_map(self):
        pass

    def select_tile(self, event):
        if self.tileset is None:
            return

        x = floor(event.localPos().x() / self.tile_size[0])
        y = floor(event.localPos().y() / self.tile_size[1])

        print(f'{x} / {y}')

    def add_tile_on_map(self):
        #TODO: draw on QPainter()
        pass





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
