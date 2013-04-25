# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'launcher.ui'
#
# Created: Thu Aug 12 14:40:32 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(628, 353)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listView = QtGui.QListView(self.centralwidget)
        self.listView.setResizeMode(QtGui.QListView.Adjust)
        self.listView.setViewMode(QtGui.QListView.IconMode)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.bt_ok = QtGui.QPushButton(self.centralwidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/button_ok.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_ok.setIcon(icon)
        self.bt_ok.setObjectName("bt_ok")
        self.horizontalLayout.addWidget(self.bt_ok)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 628, 25))
        self.menubar.setObjectName("menubar")
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea(QtCore.Qt.TopToolBarArea), self.toolBar)
        self.act_exit = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_exit.setIcon(icon1)
        self.act_exit.setObjectName("act_exit")
        self.actIconMode = QtGui.QAction(MainWindow)
        self.actIconMode.setCheckable(True)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/view-list-icons.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actIconMode.setIcon(icon2)
        self.actIconMode.setObjectName("actIconMode")
        self.actListMode = QtGui.QAction(MainWindow)
        self.actListMode.setCheckable(True)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/view-list-tree.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actListMode.setIcon(icon3)
        self.actListMode.setObjectName("actListMode")
        self.menu.addAction(self.act_exit)
        self.menubar.addAction(self.menu.menuAction())
        self.toolBar.addAction(self.actIconMode)
        self.toolBar.addAction(self.actListMode)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.bt_ok.setText(QtGui.QApplication.translate("MainWindow", "Запуск", None, QtGui.QApplication.UnicodeUTF8))
        self.menu.setTitle(QtGui.QApplication.translate("MainWindow", "Файл", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.act_exit.setText(QtGui.QApplication.translate("MainWindow", "Выход", None, QtGui.QApplication.UnicodeUTF8))
        self.actIconMode.setText(QtGui.QApplication.translate("MainWindow", "ListView", None, QtGui.QApplication.UnicodeUTF8))
        self.actListMode.setText(QtGui.QApplication.translate("MainWindow", "TableView", None, QtGui.QApplication.UnicodeUTF8))

