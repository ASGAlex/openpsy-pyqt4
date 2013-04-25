# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'image.ui'
#
# Created: Thu Aug 12 02:20:10 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(411, 268)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_image = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_image.sizePolicy().hasHeightForWidth())
        self.lbl_image.setSizePolicy(sizePolicy)
        self.lbl_image.setText("")
        self.lbl_image.setObjectName("lbl_image")
        self.verticalLayout.addWidget(self.lbl_image)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bt_save = QtGui.QPushButton(Form)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/filesaveas.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_save.setIcon(icon)
        self.bt_save.setObjectName("bt_save")
        self.horizontalLayout.addWidget(self.bt_save)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.bt_close = QtGui.QPushButton(Form)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_close.setIcon(icon1)
        self.bt_close.setObjectName("bt_close")
        self.horizontalLayout.addWidget(self.bt_close)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.bt_close, QtCore.SIGNAL("clicked()"), Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Image", None, QtGui.QApplication.UnicodeUTF8))
        self.bt_save.setText(QtGui.QApplication.translate("Form", "Сохранить как...", None, QtGui.QApplication.UnicodeUTF8))
        self.bt_close.setText(QtGui.QApplication.translate("Form", "Закрыть", None, QtGui.QApplication.UnicodeUTF8))

