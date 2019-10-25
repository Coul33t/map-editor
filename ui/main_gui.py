# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from PIL import Image, ImageQt
from math import floor

# TODO: drag and draw (use mouseevents, pressed, set bool, then in draw function)
# Use mouse events
# look for pressed, set bool to true
# if release, set bool to false
# In draw function, if mouse moved (map coordinates), draw new tile
class Ui_MainWindow(object):
    def __init__(self):
        self.graphicsScene_tileset = QtWidgets.QGraphicsScene()
        self.graphicsScene_map = QtWidgets.QGraphicsScene()

        self.path_to_tileset = None
        self.tileset = None

        self.tile_size = []

        self.all_tiles = []
        self.selected_tile = None

        self.ts_sel_light_img = Image.open('selected_tile_overlay_light.png')
        self.ts_sel_light_pixmap = None

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

        self.link_components()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionImport_tileset.setText(_translate("MainWindow", "Import tileset"))
        self.actionImport_map.setText(_translate("MainWindow", "Import map"))

    def link_components(self):
        self.actionImport_tileset.triggered.connect(self.import_tileset)
        self.graphicsView_map.setScene(self.graphicsScene_map)
        self.graphicsView_tileset.setScene(self.graphicsScene_tileset)

        self.graphicsScene_tileset.mousePressEvent = self.select_tile
        self.graphicsScene_map.mousePressEvent = self.add_tile_on_map

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
        self.graphicsScene_tileset.addPixmap(QtGui.QPixmap.fromImage(self.tileset))

        self.ts_sel_light_pixmap =  ImageQt.ImageQt(self.ts_sel_light_img.resize((self.tile_size[0], self.tile_size[1])))
        self.ts_sel_light_pixmap = self.graphicsScene_tileset.addPixmap(QtGui.QPixmap.fromImage(self.ts_sel_light_pixmap))
        self.split_tileset()

    def split_tileset(self):
        tileset_size = (self.tileset.size().height(), self.tileset.size().width())
        rect = QtCore.QRect()

        w = self.tile_size[0]
        h = self.tile_size[1]

        for i in range(int(tileset_size[0] / self.tile_size[0])):
            row = []
            for j in range(int(tileset_size[1] / self.tile_size[1])):
                x = i * self.tile_size[0]
                y = j * self.tile_size[1]
                row.append(QtGui.QPixmap.fromImage(self.tileset.copy(x, y, w, h)))

            self.all_tiles.append(row)
        print(self.all_tiles[0][0])
        print(self.all_tiles[0][0].size())

    def import_map(self):
        pass

    def select_tile(self, event):
        if self.tileset is None:
            return

        x = floor(event.scenePos().x() / self.tile_size[0]) * self.tile_size[0]
        y = floor(event.scenePos().y() / self.tile_size[1]) * self.tile_size[1]

        self.ts_sel_light_pixmap.setPos(x, y)

        self.selected_tile = self.all_tiles[int(x / self.tile_size[0])][int(y / self.tile_size[1])]


    def add_tile_on_map(self, event):
        x = floor(event.scenePos().x() / self.tile_size[0]) * self.tile_size[0]
        y = floor(event.scenePos().y() / self.tile_size[1]) * self.tile_size[1]

        new_tile = self.graphicsScene_map.addPixmap(self.selected_tile.copy())
        new_tile.setPos(x, y)





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())