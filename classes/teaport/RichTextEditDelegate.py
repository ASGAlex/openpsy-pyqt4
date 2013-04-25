# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class RichTextEditDelegate(QItemDelegate):
  def __init__(self):
    QItemDelegate.__init__(self)
    
  def paint(self,painter,option,index):
    QItemDelegate.paint(self,painter,option,index);
    
  def createEditor(self,parent,option,index):
    e=QTextEdit(parent)
    return e
  
  def setEditorData(self,editor,index):
    editor.setText(index.model().data(index, Qt.EditRole).toString())
    
  def setModelData(self,editor,model,index):
    model.setData(index,editor.toPlainText(),Qt.EditRole)
  
  def updateEditorGeometry(self,editor,option,index):
    editor.setGeometry(option.rect);