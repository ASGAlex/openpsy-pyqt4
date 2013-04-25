# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'help.ui'
#
# Created: Thu Aug 12 02:20:10 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tablist = QtGui.QTabWidget(Dialog)
        self.tablist.setObjectName("tablist")
        self.tab_test = QtGui.QWidget()
        self.tab_test.setObjectName("tab_test")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_test)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.text_about = QtWebKit.QWebView(self.tab_test)
        self.text_about.setUrl(QtCore.QUrl("about:blank"))
        self.text_about.setObjectName("text_about")
        self.verticalLayout_2.addWidget(self.text_about)
        self.tablist.addTab(self.tab_test, "")
        self.tab_me = QtGui.QWidget()
        self.tab_me.setObjectName("tab_me")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_me)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.text_authors = QtWebKit.QWebView(self.tab_me)
        self.text_authors.setUrl(QtCore.QUrl("about:blank"))
        self.text_authors.setObjectName("text_authors")
        self.verticalLayout_3.addWidget(self.text_authors)
        self.tablist.addTab(self.tab_me, "")
        self.tab_license = QtGui.QWidget()
        self.tab_license.setObjectName("tab_license")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab_license)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.text_license = QtWebKit.QWebView(self.tab_license)
        self.text_license.setUrl(QtCore.QUrl("about:blank"))
        self.text_license.setObjectName("text_license")
        self.verticalLayout_4.addWidget(self.text_license)
        self.tablist.addTab(self.tab_license, "")
        self.verticalLayout.addWidget(self.tablist)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.bt_ok = QtGui.QPushButton(Dialog)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/button_ok.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_ok.setIcon(icon)
        self.bt_ok.setObjectName("bt_ok")
        self.horizontalLayout.addWidget(self.bt_ok)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.tablist.setCurrentIndex(0)
        QtCore.QObject.connect(self.bt_ok, QtCore.SIGNAL("clicked()"), Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.tablist.setTabText(self.tablist.indexOf(self.tab_test), QtGui.QApplication.translate("Dialog", "О тесте", None, QtGui.QApplication.UnicodeUTF8))
        self.tablist.setTabText(self.tablist.indexOf(self.tab_me), QtGui.QApplication.translate("Dialog", "Авторы", None, QtGui.QApplication.UnicodeUTF8))
        self.tablist.setTabText(self.tablist.indexOf(self.tab_license), QtGui.QApplication.translate("Dialog", "Лицензия", None, QtGui.QApplication.UnicodeUTF8))
        self.bt_ok.setText(QtGui.QApplication.translate("Dialog", "Ok", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
