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

        self.tileset_overlay_img = Image.open('selected_tile_overlay_small.png').convert('RGBA')
        self.tileset_overlay_pixmap = None

        self.map_overlay_img = Image.open('map_overlay_small.png').convert('RGBA')
        self.map_overlay_pixmap = None

        self.is_dragging = False

        self.last_coordinates = [-1, -1]
        self.map_canvas_size = [-1, -1]

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1087, 849)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView_map = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_map.setGeometry(QtCore.QRect(280, 10, 512, 512))
        self.graphicsView_map.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.graphicsView_map.setObjectName("graphicsView_map")
        self.graphicsView_tileset = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_tileset.setGeometry(QtCore.QRect(10, 10, 256, 512))
        self.graphicsView_tileset.setObjectName("graphicsView_tileset")
        self.groupBox_map_size = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_map_size.setGeometry(QtCore.QRect(280, 530, 131, 111))
        self.groupBox_map_size.setObjectName("groupBox_map_size")
        self.spinBox_map_width = QtWidgets.QSpinBox(self.groupBox_map_size)
        self.spinBox_map_width.setGeometry(QtCore.QRect(10, 50, 51, 22))
        self.spinBox_map_width.setMinimum(1)
        self.spinBox_map_width.setMaximum(999999)
        self.spinBox_map_width.setObjectName("spinBox_map_width")
        self.label_map_width = QtWidgets.QLabel(self.groupBox_map_size)
        self.label_map_width.setGeometry(QtCore.QRect(10, 30, 41, 16))
        self.label_map_width.setObjectName("label_map_width")
        self.spinBox_map_height = QtWidgets.QSpinBox(self.groupBox_map_size)
        self.spinBox_map_height.setGeometry(QtCore.QRect(71, 50, 51, 22))
        self.spinBox_map_height.setMinimum(1)
        self.spinBox_map_height.setMaximum(999999)
        self.spinBox_map_height.setObjectName("spinBox_map_height")
        self.label_map_height = QtWidgets.QLabel(self.groupBox_map_size)
        self.label_map_height.setGeometry(QtCore.QRect(70, 30, 55, 16))
        self.label_map_height.setObjectName("label_map_height")
        self.pushButton_map_size = QtWidgets.QPushButton(self.groupBox_map_size)
        self.pushButton_map_size.setGeometry(QtCore.QRect(10, 80, 93, 28))
        self.pushButton_map_size.setObjectName("pushButton_map_size")
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
        self.hide_components()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_map_size.setTitle(_translate("MainWindow", "Map size"))
        self.label_map_width.setText(_translate("MainWindow", "Width"))
        self.label_map_height.setText(_translate("MainWindow", "Height"))
        self.pushButton_map_size.setText(_translate("MainWindow", "Change size"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionImport_tileset.setText(_translate("MainWindow", "Import tileset"))
        self.actionImport_map.setText(_translate("MainWindow", "Import map"))

    def link_components(self):
        self.actionImport_tileset.triggered.connect(self.import_tileset)
        self.graphicsView_map.setScene(self.graphicsScene_map)
        self.graphicsView_tileset.setScene(self.graphicsScene_tileset)
        self.pushButton_map_size.clicked.connect(self.change_map_size)

        self.graphicsScene_tileset.mousePressEvent = self.select_tile

        self.graphicsScene_map.mousePressEvent = self.mouse_pressed
        self.graphicsScene_map.mouseReleaseEvent = self.mouse_released
        self.graphicsScene_map.mouseMoveEvent = self.mouse_moved

    def hide_components(self):
        self.groupBox_map_size.hide()
        self.graphicsView_map.hide()
        self.graphicsView_tileset.hide()

    def import_tileset(self):
        string = QtWidgets.QFileDialog.getOpenFileName(filter="Image Files (*.png *.jpg *.bmp)")
        self.path_to_tileset = string[0]

        if not self.path_to_tileset:
            return

        self.tileset = Image.open(self.path_to_tileset).convert('RGBA')

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

        self.tileset_overlay_pixmap = ImageQt.ImageQt(self.tileset_overlay_img.resize((self.tile_size[0], self.tile_size[1])))
        self.tileset_overlay_pixmap = self.graphicsScene_tileset.addPixmap(QtGui.QPixmap.fromImage(self.tileset_overlay_pixmap))

        self.map_overlay_pixmap = ImageQt.ImageQt(self.map_overlay_img.resize((self.tile_size[0], self.tile_size[1])))
        self.map_overlay_pixmap = self.graphicsScene_map.addPixmap(QtGui.QPixmap.fromImage(self.map_overlay_pixmap))

        self.split_tileset()

        self.selected_tile = self.all_tiles[0][0]

        self.graphicsView_tileset.show()
        self.groupBox_map_size.show()


    def split_tileset(self):
        tileset_size = (self.tileset.size().height(), self.tileset.size().width())

        w = self.tile_size[0]
        h = self.tile_size[1]

        for i in range(int(tileset_size[0] / self.tile_size[0])):
            row = []
            for j in range(int(tileset_size[1] / self.tile_size[1])):
                y = i * self.tile_size[0]
                x = j * self.tile_size[1]
                row.append(QtGui.QPixmap.fromImage(self.tileset.copy(x, y, w, h)))

            self.all_tiles.append(row)

    def change_map_size(self):
        width = self.spinBox_map_width.value()
        height = self.spinBox_map_height.value()

        # Should never happen since I forced the values to be in the range
        # 1 - 999999
        if width <= 0 or height <= 0:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText(f"Error: Width or Height can't be 0 or less")
            msg.exec_()
            return

        self.map_canvas_size = [width * self.tile_size[0], height * self.tile_size[1]]

        new_canvas = QtGui.QPixmap(self.map_canvas_size[0], self.map_canvas_size[1])
        new_canvas.fill(QtGui.QColor(255, 255, 255, 255))
        self.graphicsScene_map.addPixmap(new_canvas)
        self.graphicsScene_map.setSceneRect(0, 0, self.map_canvas_size[0], self.map_canvas_size[1])

        self.graphicsView_map.show()



    def import_map(self):
        pass

    def select_tile(self, event):
        if self.tileset is None:
            return

        x = floor(event.scenePos().x() / self.tile_size[0]) * self.tile_size[0]
        y = floor(event.scenePos().y() / self.tile_size[1]) * self.tile_size[1]

        self.tileset_overlay_pixmap.setPos(x, y)

        self.selected_tile = self.all_tiles[int(y / self.tile_size[1])][int(x / self.tile_size[0])]


    def add_tile_on_map(self, event):
        x = floor(event.scenePos().x() / self.tile_size[0]) * self.tile_size[0]
        y = floor(event.scenePos().y() / self.tile_size[1]) * self.tile_size[1]

        if x >= self.map_canvas_size[0] or y >= self.map_canvas_size[1]:
            return

        new_tile = self.graphicsScene_map.addPixmap(self.selected_tile.copy())
        new_tile.setPos(x, y)


    def mouse_pressed(self, event):
        self.is_dragging = True
        self.add_tile_on_map(event)


    def mouse_released(self, event):
        self.is_dragging = False
        self.last_coordinates = [-1, -1]

    def mouse_moved(self, event):
        if not self.is_dragging:
            return

        x = floor(event.scenePos().x() / self.tile_size[0])
        y = floor(event.scenePos().y() / self.tile_size[1])

        if x != self.last_coordinates[0] or y != self.last_coordinates[1]:
            self.add_tile_on_map(event)
            self.last_coordinates = [x, y]


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())