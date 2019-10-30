# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from PIL import Image, ImageQt
from math import floor

import numpy as np

DEBUG = True

# TODO: draggable area in tileset to multidraw
#       obstacle layer, etc.

class Ui_MainWindow(object):
    def __init__(self):
        self.graphicsScene_tileset = QtWidgets.QGraphicsScene()
        self.graphicsScene_map = QtWidgets.QGraphicsScene()

        self.path_to_tileset = None
        self.tileset = None

        self.tile_size = []

        self.all_tiles = []
        self.selected_tile = None
        self.selected_tile_coord = (-1, -1)

        self.tileset_overlay_img = Image.open('selected_tile_overlay_small.png').convert('RGBA')
        self.tileset_overlay_pixmap = None

        self.map_overlay_img = Image.open('map_overlay_small.png').convert('RGBA')
        self.map_overlay_pixmap = None

        self.is_dragging = False

        self.last_coordinates = [-1, -1]
        self.map_canvas_size = [-1, -1]

        self.current_layer = 0
        self.number_of_layers = 5

        self.map_as_array = None

        self.remove_mode = False

        self.drawing_style = 'paint'

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1087, 849)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView_map = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_map.setGeometry(QtCore.QRect(280, 10, 512, 512))
        self.graphicsView_map.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
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
        self.groupBox_layers = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_layers.setGeometry(QtCore.QRect(420, 530, 161, 111))
        self.groupBox_layers.setObjectName("groupBox_layers")
        self.checkBox_only_display_layer = QtWidgets.QCheckBox(self.groupBox_layers)
        self.checkBox_only_display_layer.setGeometry(QtCore.QRect(10, 80, 16, 21))
        self.checkBox_only_display_layer.setText("")
        self.checkBox_only_display_layer.setObjectName("checkBox_only_display_layer")
        self.label_only_display_layer = QtWidgets.QLabel(self.groupBox_layers)
        self.label_only_display_layer.setGeometry(QtCore.QRect(40, 70, 71, 41))
        self.label_only_display_layer.setWordWrap(True)
        self.label_only_display_layer.setObjectName("label_only_display_layer")
        self.spinBox_current_layer = QtWidgets.QSpinBox(self.groupBox_layers)
        self.spinBox_current_layer.setGeometry(QtCore.QRect(10, 20, 42, 22))
        self.spinBox_current_layer.setObjectName("spinBox_current_layer")
        self.spinBox_current_layer.setMinimum(0)
        self.spinBox_current_layer.setMaximum(self.number_of_layers)
        self.pushButton_clear_layer = QtWidgets.QPushButton(self.groupBox_layers)
        self.pushButton_clear_layer.setGeometry(QtCore.QRect(60, 20, 93, 28))
        self.pushButton_clear_layer.setObjectName("pushButton_clear_layer")
        self.groupBox_drawing = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_drawing.setGeometry(QtCore.QRect(590, 530, 201, 111))
        self.groupBox_drawing.setObjectName("groupBox_drawing")
        self.radioButton_paint = QtWidgets.QRadioButton(self.groupBox_drawing)
        self.radioButton_paint.setGeometry(QtCore.QRect(10, 20, 95, 20))
        self.radioButton_paint.setObjectName("radioButton_paint")
        self.radioButton_fill = QtWidgets.QRadioButton(self.groupBox_drawing)
        self.radioButton_fill.setGeometry(QtCore.QRect(10, 40, 95, 20))
        self.radioButton_fill.setObjectName("radioButton_fill")
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
        self.groupBox_layers.setTitle(_translate("MainWindow", "Layers"))
        self.label_only_display_layer.setText(_translate("MainWindow", "Only display this layer"))
        self.pushButton_clear_layer.setText(_translate("MainWindow", "Clear layer"))
        self.groupBox_drawing.setTitle(_translate("MainWindow", "Drawing"))
        self.radioButton_paint.setText(_translate("MainWindow", "Paint"))
        self.radioButton_fill.setText(_translate("MainWindow", "Fill"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionImport_tileset.setText(_translate("MainWindow", "Import tileset"))
        self.actionImport_map.setText(_translate("MainWindow", "Import map"))

    def link_components(self):
        self.actionImport_tileset.triggered.connect(self.import_tileset)
        self.graphicsView_map.setScene(self.graphicsScene_map)
        self.graphicsView_tileset.setScene(self.graphicsScene_tileset)
        self.pushButton_map_size.clicked.connect(self.change_map_size)
        self.spinBox_current_layer.valueChanged.connect(self.change_layer)
        self.checkBox_only_display_layer.stateChanged.connect(self.draw_map)
        self.pushButton_clear_layer.clicked.connect(self.clear_layer)

        self.radioButton_paint.toggled.connect(lambda:self.change_drawing_style(self.radioButton_paint))
        self.radioButton_fill.toggled.connect(lambda:self.change_drawing_style(self.radioButton_fill))

        self.graphicsScene_tileset.mousePressEvent = self.select_tile

        self.graphicsScene_map.mousePressEvent = self.mouse_pressed
        self.graphicsScene_map.mouseReleaseEvent = self.mouse_released
        self.graphicsScene_map.mouseMoveEvent = self.mouse_moved

    def hide_components(self):
        self.groupBox_map_size.hide()
        self.groupBox_layers.hide()
        self.groupBox_drawing.hide()
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

        self.map_as_array = np.zeros((height, width, self.number_of_layers), dtype=('int', 2)) - 1

        new_canvas = QtGui.QPixmap(self.map_canvas_size[0], self.map_canvas_size[1])
        new_canvas.fill(QtGui.QColor(255, 255, 255, 255))
        self.graphicsScene_map.addPixmap(new_canvas)
        self.graphicsScene_map.setSceneRect(0, 0, self.map_canvas_size[0], self.map_canvas_size[1])

        self.graphicsView_map.show()
        self.groupBox_layers.show()
        self.groupBox_drawing.show()
        self.radioButton_paint.setChecked(True)

    def import_map(self):
        pass

    def select_tile(self, event):
        if self.tileset is None:
            return

        # Grid coordinates
        x = int(floor(event.scenePos().x() / self.tile_size[0]))
        y = int(floor(event.scenePos().y() / self.tile_size[1]))

        self.selected_tile = self.all_tiles[y][x]
        self.selected_tile_coord = (x, y)

        # Pixel coordinates
        self.tileset_overlay_pixmap.setPos(x * self.tile_size[0], y * self.tile_size[1])


    def change_layer(self):
        """
            Used to avoid querying the spinBox value for every drawing.
        """
        self.current_layer = self.spinBox_current_layer.value()

    def change_drawing_style(self, button):
        if button.text() == 'Paint':
            self.drawing_style = 'paint'
        elif button.text() == 'Fill':
            self.drawing_style = 'fill'

    def add_tile_on_map(self, event):
        x = floor(event.scenePos().x() / self.tile_size[0]) * self.tile_size[0]
        y = floor(event.scenePos().y() / self.tile_size[1]) * self.tile_size[1]

        if x >= self.map_canvas_size[0] or y >= self.map_canvas_size[1]:
            return
        # Grid coordinates
        x_grid = int(x / self.tile_size[0])
        y_grid = int(y / self.tile_size[1])

        self.map_as_array[x_grid, y_grid, self.current_layer] = [self.selected_tile_coord[0],
                                                                 self.selected_tile_coord[1]]

        # Redraws
        tile_to_delete = self.graphicsScene_map.itemAt(x, y, QtGui.QTransform())

        if tile_to_delete:
            self.graphicsScene_map.removeItem(tile_to_delete)

        self.draw_map()

    def get_neighbors(self, origin, node_list):
        nei = [(origin[0] - 1, origin[1]),
               (origin[0] + 1, origin[1]),
               (origin[0], origin[1] - 1),
               (origin[0], origin[1] + 1)]

        if set(nei) <= set(node_list):
            return nei

        return [x for x in nei if x in node_list]

    def get_adjacent(self, x_origin, y_origin, original_tile):
        final_tile_list = set()
        visited_nodes = set()
        queue = []
        queue.append((x_origin, y_origin))
        node_list = [(x, y) for x in range(floor(self.map_canvas_size[0] / self.tile_size[0])) for y in range(floor(self.map_canvas_size[1] / self.tile_size[1]))]

        while queue:
            node = queue.pop(0)
            if (node not in visited_nodes
            and np.array_equal(self.map_as_array[node[0], node[1], self.current_layer], original_tile)):
                final_tile_list.add(node)
                visited_nodes.add(node)

                for neighbor in self.get_neighbors(node, node_list):
                    if neighbor not in final_tile_list:
                        queue.append(neighbor)

        return final_tile_list


    def fill_with_tile(self, event):

        x = event.scenePos().x()
        y = event.scenePos().y()

        x_grid = floor(x / self.tile_size[0])
        y_grid = floor(y / self.tile_size[1])

        original_tile = self.map_as_array[x_grid, y_grid, self.current_layer]

        tiles_to_fill = list(self.get_adjacent(x_grid, y_grid, original_tile))

        for tile_to_paint in tiles_to_fill:
            self.map_as_array[tile_to_paint[0], tile_to_paint[1], self.current_layer] = self.selected_tile_coord

        self.draw_map()

    def draw_map(self):
        self.graphicsScene_map.clear()

        if self.checkBox_only_display_layer.isChecked():
            for i in range(len(self.map_as_array)):
                for j in range(len(self.map_as_array[0])):
                    tiles_coordinates = self.map_as_array[i][j][self.current_layer]
                    if tiles_coordinates[0] >= 0 and tiles_coordinates[1] >= 0:
                        new_tile = self.graphicsScene_map.addPixmap(self.all_tiles[tiles_coordinates[1]][tiles_coordinates[0]].copy())
                        new_tile.setPos(i * self.tile_size[0], j * self.tile_size[1])

        else:
            for i in range(len(self.map_as_array)):
                for j in range(len(self.map_as_array[0])):
                    for k in range(self.number_of_layers):
                        tiles_coordinates = self.map_as_array[i][j][k]
                        if tiles_coordinates[0] >= 0 and tiles_coordinates[1] >= 0:
                            new_tile = self.graphicsScene_map.addPixmap(self.all_tiles[tiles_coordinates[1]][tiles_coordinates[0]].copy())
                            new_tile.setPos(i * self.tile_size[0], j * self.tile_size[1])

    def clear_layer(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText(f"Are you sure you want to delete layer {self.current_layer}? There's no turning back.")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        ret = msg.exec_()

        if ret == QtWidgets.QMessageBox.Ok:
            self.map_as_array[:,:,self.current_layer] = [-1,-1]
            self.draw_map()

    def mouse_pressed(self, event):
        if self.drawing_style == 'paint':
            self.is_dragging = True
            self.add_tile_on_map(event)

        elif self.drawing_style == 'fill':
            self.fill_with_tile(event)


    def mouse_released(self, event):
        if self.drawing_style == 'paint':
            self.is_dragging = False
            self.last_coordinates = [-1, -1]

    def mouse_moved(self, event):
        if not self.is_dragging:
            return

        # No need to do the rest of the function if the mouse isn't in the map
        if event.scenePos().x() > self.map_canvas_size[0] or event.scenePos().y() > self.map_canvas_size[1]:
            return

        # For now, this function is only used to paint
        if self.drawing_style != 'paint':
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