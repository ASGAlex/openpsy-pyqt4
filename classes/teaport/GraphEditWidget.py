# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui.grapheditui import *

class GraphEditWidget(QWidget,Ui_GraphEdit):
  def __init__(self,parent=None):
    QWidget.__init__(self,parent)
    Ui_GraphEdit.setupUi(self,self)
    self.spinW.setValue(640)
    self.spinH.setValue(480)
    self.spinF.setValue(10)
    self.spinM.setValue(5)
    
    self.b_group=QButtonGroup(self)
    self.b_group.addButton(self.rGraph)
    self.b_group.addButton(self.rHistro)
    self.b_group.addButton(self.rNone)
    
    self.connect(self.rHistro,SIGNAL('toggled(bool)'),self.setHistro)
    
    self.connect(self.spinW,SIGNAL('valueChanged(int)'),self.onDataChanged)
    self.connect(self.spinH,SIGNAL('valueChanged(int)'),self.onDataChanged)
    self.connect(self.spinF,SIGNAL('valueChanged(int)'),self.onDataChanged)
    self.connect(self.spinM,SIGNAL('valueChanged(int)'),self.onDataChanged)
    self.connect(self.rGraph,SIGNAL('toggled()'),self.onDataChanged)
    self.connect(self.rHistro,SIGNAL('toggled()'),self.onDataChanged)
    self.connect(self.rNone,SIGNAL('toggled()'),self.onDataChanged)
    
  def getImgType(self):
    if self.rGraph.isChecked():
      return 'graph'
    elif self.rHistro.isChecked():
      return 'histro'
    else:
      return 'noimage'
    
  def getImgSize(self):
    w=self.spinW.value()
    h=self.spinH.value()
    f=self.spinF.value()
    return (w,h,f)
  
  def setHistro(self,is_checked):
    if is_checked:
      self.spinM.setEnabled(True)
      self.lblM.setEnabled(True)
    else:
      self.spinM.setDisabled(True)
      self.lblM.setDisabled(True)
  
  def getHistroMaximum(self):
    return self.spinM.value()
    
  def onDataChanged(self):
    self.emit(SIGNAL('dataChanged()'))
    
  def setImage(self,img):
    self.lblImg.setPixmap(QPixmap.fromImage(img))