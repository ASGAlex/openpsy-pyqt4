# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graphedit.ui'
#
# Created: Wed Aug 18 03:16:10 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_GraphEdit(object):
    def setupUi(self, GraphEdit):
        GraphEdit.setObjectName("GraphEdit")
        GraphEdit.resize(270, 193)
        self.verticalLayout = QtGui.QVBoxLayout(GraphEdit)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtGui.QGroupBox(GraphEdit)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rNone = QtGui.QRadioButton(self.groupBox)
        self.rNone.setObjectName("rNone")
        self.horizontalLayout.addWidget(self.rNone)
        self.rGraph = QtGui.QRadioButton(self.groupBox)
        self.rGraph.setObjectName("rGraph")
        self.horizontalLayout.addWidget(self.rGraph)
        self.rHistro = QtGui.QRadioButton(self.groupBox)
        self.rHistro.setObjectName("rHistro")
        self.horizontalLayout.addWidget(self.rHistro)
        self.verticalLayout.addWidget(self.groupBox)
        self.layPrev = QtGui.QHBoxLayout()
        self.layPrev.setObjectName("layPrev")
        self.groupBox_2 = QtGui.QGroupBox(GraphEdit)
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout = QtGui.QFormLayout(self.groupBox_2)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.spinW = QtGui.QSpinBox(self.groupBox_2)
        self.spinW.setMinimum(1)
        self.spinW.setMaximum(2048)
        self.spinW.setObjectName("spinW")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.spinW)
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.spinH = QtGui.QSpinBox(self.groupBox_2)
        self.spinH.setMinimum(1)
        self.spinH.setMaximum(2048)
        self.spinH.setObjectName("spinH")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.spinH)
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.spinF = QtGui.QSpinBox(self.groupBox_2)
        self.spinF.setMinimum(1)
        self.spinF.setMaximum(50)
        self.spinF.setObjectName("spinF")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.spinF)
        self.lblM = QtGui.QLabel(self.groupBox_2)
        self.lblM.setObjectName("lblM")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.lblM)
        self.spinM = QtGui.QSpinBox(self.groupBox_2)
        self.spinM.setMinimum(0)
        self.spinM.setMaximum(2048)
        self.spinM.setObjectName("spinM")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.spinM)
        self.layPrev.addWidget(self.groupBox_2)
        self.lblImg = QtGui.QLabel(GraphEdit)
        self.lblImg.setText("")
        self.lblImg.setObjectName("lblImg")
        self.layPrev.addWidget(self.lblImg)
        self.verticalLayout.addLayout(self.layPrev)
        spacerItem = QtGui.QSpacerItem(10, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(GraphEdit)
        QtCore.QMetaObject.connectSlotsByName(GraphEdit)

    def retranslateUi(self, GraphEdit):
        GraphEdit.setWindowTitle(QtGui.QApplication.translate("GraphEdit", "Редактор графиков", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("GraphEdit", "Тип графика", None, QtGui.QApplication.UnicodeUTF8))
        self.rNone.setText(QtGui.QApplication.translate("GraphEdit", "Нет", None, QtGui.QApplication.UnicodeUTF8))
        self.rGraph.setText(QtGui.QApplication.translate("GraphEdit", "График", None, QtGui.QApplication.UnicodeUTF8))
        self.rHistro.setText(QtGui.QApplication.translate("GraphEdit", "Гистрограмма", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("GraphEdit", "Размеры", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("GraphEdit", "Ширина:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("GraphEdit", "Высота:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("GraphEdit", "Шрифт:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblM.setText(QtGui.QApplication.translate("GraphEdit", "Максимум:", None, QtGui.QApplication.UnicodeUTF8))
