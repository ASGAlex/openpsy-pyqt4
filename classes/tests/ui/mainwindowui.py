# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Thu Aug 12 02:20:11 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(405, 234)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/psy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_text = QtWebKit.QWebView(self.centralwidget)
        self.main_text.setUrl(QtCore.QUrl("about:blank"))
        self.main_text.setObjectName("main_text")
        self.verticalLayout.addWidget(self.main_text)
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.h_lay = QtGui.QHBoxLayout()
        self.h_lay.setObjectName("h_lay")
        self.bt_prev = QtGui.QPushButton(self.centralwidget)
        self.bt_prev.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_prev.setIcon(icon1)
        self.bt_prev.setObjectName("bt_prev")
        self.h_lay.addWidget(self.bt_prev)
        self.bt_multi = QtGui.QPushButton(self.centralwidget)
        self.bt_multi.setText("")
        self.bt_multi.setObjectName("bt_multi")
        self.h_lay.addWidget(self.bt_multi)
        self.bt_next = QtGui.QPushButton(self.centralwidget)
        self.bt_next.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/foward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_next.setIcon(icon2)
        self.bt_next.setObjectName("bt_next")
        self.h_lay.addWidget(self.bt_next)
        self.verticalLayout.addLayout(self.h_lay)
        self.button_layout = QtGui.QHBoxLayout()
        self.button_layout.setObjectName("button_layout")
        self.verticalLayout.addLayout(self.button_layout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 405, 25))
        self.menubar.setObjectName("menubar")
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtGui.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.act_new_test = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/filenew.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_new_test.setIcon(icon3)
        self.act_new_test.setObjectName("act_new_test")
        self.act_exit = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_exit.setIcon(icon4)
        self.act_exit.setObjectName("act_exit")
        self.act_about = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_about.setIcon(icon5)
        self.act_about.setObjectName("act_about")
        self.act_about_qt = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/qt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_about_qt.setIcon(icon6)
        self.act_about_qt.setObjectName("act_about_qt")
        self.menu.addAction(self.act_new_test)
        self.menu.addAction(self.act_exit)
        self.menu_2.addAction(self.act_about)
        self.menu_2.addAction(self.act_about_qt)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.act_exit, QtCore.SIGNAL("triggered()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "c4psy program", None, QtGui.QApplication.UnicodeUTF8))
        self.progressBar.setFormat(QtGui.QApplication.translate("MainWindow", "Вопрос %v из %m", None, QtGui.QApplication.UnicodeUTF8))
        self.bt_prev.setText(QtGui.QApplication.translate("MainWindow", "Предыдущий вопрос", None, QtGui.QApplication.UnicodeUTF8))
        self.bt_next.setText(QtGui.QApplication.translate("MainWindow", "Следующий вопрос", None, QtGui.QApplication.UnicodeUTF8))
        self.menu.setTitle(QtGui.QApplication.translate("MainWindow", "Тест", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_2.setTitle(QtGui.QApplication.translate("MainWindow", "Помощь", None, QtGui.QApplication.UnicodeUTF8))
        self.act_new_test.setText(QtGui.QApplication.translate("MainWindow", "Начать тест", None, QtGui.QApplication.UnicodeUTF8))
        self.act_exit.setText(QtGui.QApplication.translate("MainWindow", "Выход", None, QtGui.QApplication.UnicodeUTF8))
        self.act_about.setText(QtGui.QApplication.translate("MainWindow", "О программе", None, QtGui.QApplication.UnicodeUTF8))
        self.act_about_qt.setText(QtGui.QApplication.translate("MainWindow", "About Qt", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
