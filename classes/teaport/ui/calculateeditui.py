# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculateedit.ui'
#
# Created: Wed Aug 18 03:16:10 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_CalculateEdit(object):
    def setupUi(self, CalculateEdit):
        CalculateEdit.setObjectName("CalculateEdit")
        CalculateEdit.resize(628, 208)
        CalculateEdit.setMinimumSize(QtCore.QSize(628, 208))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(CalculateEdit)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.listResults = QtGui.QListView(CalculateEdit)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listResults.sizePolicy().hasHeightForWidth())
        self.listResults.setSizePolicy(sizePolicy)
        self.listResults.setObjectName("listResults")
        self.verticalLayout.addWidget(self.listResults)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btAddRes = QtGui.QPushButton(CalculateEdit)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btAddRes.sizePolicy().hasHeightForWidth())
        self.btAddRes.setSizePolicy(sizePolicy)
        self.btAddRes.setMaximumSize(QtCore.QSize(16777215, 22))
        self.btAddRes.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/add_test.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btAddRes.setIcon(icon)
        self.btAddRes.setObjectName("btAddRes")
        self.horizontalLayout.addWidget(self.btAddRes)
        self.btDelRes = QtGui.QPushButton(CalculateEdit)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btDelRes.sizePolicy().hasHeightForWidth())
        self.btDelRes.setSizePolicy(sizePolicy)
        self.btDelRes.setMaximumSize(QtCore.QSize(16777215, 22))
        self.btDelRes.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/remove_test.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btDelRes.setIcon(icon1)
        self.btDelRes.setObjectName("btDelRes")
        self.horizontalLayout.addWidget(self.btDelRes)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.listGrades = QtGui.QListView(CalculateEdit)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listGrades.sizePolicy().hasHeightForWidth())
        self.listGrades.setSizePolicy(sizePolicy)
        self.listGrades.setObjectName("listGrades")
        self.verticalLayout_3.addWidget(self.listGrades)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btAddGrade = QtGui.QPushButton(CalculateEdit)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btAddGrade.sizePolicy().hasHeightForWidth())
        self.btAddGrade.setSizePolicy(sizePolicy)
        self.btAddGrade.setMaximumSize(QtCore.QSize(16777215, 22))
        self.btAddGrade.setText("")
        self.btAddGrade.setIcon(icon)
        self.btAddGrade.setObjectName("btAddGrade")
        self.horizontalLayout_2.addWidget(self.btAddGrade)
        self.btDelGrade = QtGui.QPushButton(CalculateEdit)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btDelGrade.sizePolicy().hasHeightForWidth())
        self.btDelGrade.setSizePolicy(sizePolicy)
        self.btDelGrade.setMaximumSize(QtCore.QSize(16777215, 22))
        self.btDelGrade.setText("")
        self.btDelGrade.setIcon(icon1)
        self.btDelGrade.setObjectName("btDelGrade")
        self.horizontalLayout_2.addWidget(self.btDelGrade)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_6 = QtGui.QLabel(CalculateEdit)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setTextFormat(QtCore.Qt.RichText)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtGui.QLabel(CalculateEdit)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineAnswNum = QtGui.QLineEdit(CalculateEdit)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineAnswNum.sizePolicy().hasHeightForWidth())
        self.lineAnswNum.setSizePolicy(sizePolicy)
        self.lineAnswNum.setObjectName("lineAnswNum")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineAnswNum)
        self.labelKeyName = QtGui.QLabel(CalculateEdit)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelKeyName.sizePolicy().hasHeightForWidth())
        self.labelKeyName.setSizePolicy(sizePolicy)
        self.labelKeyName.setObjectName("labelKeyName")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.labelKeyName)
        self.chManualKey = QtGui.QCheckBox(CalculateEdit)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chManualKey.sizePolicy().hasHeightForWidth())
        self.chManualKey.setSizePolicy(sizePolicy)
        self.chManualKey.setObjectName("chManualKey")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.chManualKey)
        self.lineAnswKey = QtGui.QLineEdit(CalculateEdit)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineAnswKey.sizePolicy().hasHeightForWidth())
        self.lineAnswKey.setSizePolicy(sizePolicy)
        self.lineAnswKey.setObjectName("lineAnswKey")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineAnswKey)
        self.verticalLayout_5.addLayout(self.formLayout)
        self.verticalLayout_7.addLayout(self.verticalLayout_5)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtGui.QLabel(CalculateEdit)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setTextFormat(QtCore.Qt.RichText)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtGui.QLabel(CalculateEdit)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.lineGradeFrom = QtGui.QLineEdit(CalculateEdit)
        self.lineGradeFrom.setObjectName("lineGradeFrom")
        self.horizontalLayout_3.addWidget(self.lineGradeFrom)
        self.label_4 = QtGui.QLabel(CalculateEdit)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.lineGradeTo = QtGui.QLineEdit(CalculateEdit)
        self.lineGradeTo.setObjectName("lineGradeTo")
        self.horizontalLayout_3.addWidget(self.lineGradeTo)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout_7.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_7)

        self.retranslateUi(CalculateEdit)
        QtCore.QMetaObject.connectSlotsByName(CalculateEdit)

    def retranslateUi(self, CalculateEdit):
        CalculateEdit.setWindowTitle(QtGui.QApplication.translate("CalculateEdit", "Calculate editor", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("CalculateEdit", "Введите номера ответов, по которым считается результат.\n"
"Положительное число означает, что ответ нужно прибавить к результату, отрицательное - отнять.\n"
"\n"
"", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("CalculateEdit", "Номера ответов:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelKeyName.setText(QtGui.QApplication.translate("CalculateEdit", "Ключи:", None, QtGui.QApplication.UnicodeUTF8))
        self.chManualKey.setText(QtGui.QApplication.translate("CalculateEdit", "Ввести вручную", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("CalculateEdit", "Введите диапазон, в пределах которого первичная оценка будет преобразовываться во вторичную. ", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("CalculateEdit", "От:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("CalculateEdit", "До:", None, QtGui.QApplication.UnicodeUTF8))
