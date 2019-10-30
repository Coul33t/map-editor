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
        self.graphicsView_map.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.graphicsView_map.setDragMode(QtWidgets.QGraphicsView.NoDrag)
        self.graphicsView_map.setTransformationAnchor(QtWidgets.QGraphicsView.AnchorViewCenter)
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
        self.checkBox_only_display_layer.setGeometry(QtCore.QRect(60, 20, 16, 21))
        self.checkBox_only_display_layer.setText("")
        self.checkBox_only_display_layer.setObjectName("checkBox_only_display_layer")
        self.label_only_display_layer = QtWidgets.QLabel(self.groupBox_layers)
        self.label_only_display_layer.setGeometry(QtCore.QRect(80, 10, 71, 41))
        self.label_only_display_layer.setWordWrap(True)
        self.label_only_display_layer.setObjectName("label_only_display_layer")
        self.spinBox_current_layer = QtWidgets.QSpinBox(self.groupBox_layers)
        self.spinBox_current_layer.setGeometry(QtCore.QRect(10, 20, 42, 22))
        self.spinBox_current_layer.setObjectName("spinBox_current_layer")
        self.pushButton_clear_layer = QtWidgets.QPushButton(self.groupBox_layers)
        self.pushButton_clear_layer.setGeometry(QtCore.QRect(10, 80, 93, 28))
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

