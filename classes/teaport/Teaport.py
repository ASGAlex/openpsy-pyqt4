# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui.teaportui import *
from AnswerEditWidget import *
from CalculateEditWidget import *
from RichTextEditDelegate import *
from GraphEditWidget import *

from classes.alg.TestDescriptor import *
from random import *

class Teaport(QMainWindow,Ui_MainWindow):
  def __init__(self,parent=None):
    QMainWindow.__init__(self,parent)
    self.setupUi(self)
    self.tableInterp.setItemDelegate(RichTextEditDelegate())
    
    self.answEdit=AnswerEditWidget(self.tabAnswers)
    self.tabAnswers.layout().addWidget(self.answEdit)
    
    self.calcEdit=CalculateEditWidget(self.tabCalculate)
    self.tabCalculate.layout().addWidget(self.calcEdit)
    
    self.graphEdit=GraphEditWidget(self.tabGraph)
    self.tabGraph.layout().addWidget(self.graphEdit)
    
    self.Descriptor=TestDescriptor()
    
    self.qNum=QLabel()
    self.aNum=QLabel()
    self.prNum=QLabel()
    self.srNum=QLabel()
    self.statusBar.addWidget(self.qNum)
    self.statusBar.addWidget(self.aNum)
    self.statusBar.addWidget(self.prNum)
    self.statusBar.addWidget(self.srNum)
    self.updateStatusBar()
    
    self.connect(self.text_questions,SIGNAL('textChanged()'),self.updateStatusBar)
    self.connect(self.answEdit,SIGNAL('answersChanged()'),self.updateStatusBar)
    self.connect(self.calcEdit,SIGNAL('gradesChanged()'),self.updateStatusBar)
    self.connect(self.calcEdit,SIGNAL('resultsChanged()'),self.updateStatusBar)
    
    self.connect(self.calcEdit,SIGNAL('gradesChanged()'),self.updateInterpTable)
    self.connect(self.calcEdit,SIGNAL('resultsChanged()'),self.updateInterpTable)
    
    self.connect(self.graphEdit,SIGNAL('dataChanged()'),self.updateImage)
    
    
    self.updateInterpTable()
  def updateStatusBar(self):
    s=self.text_questions.toPlainText()
    sl=s.split("\n",QString.SkipEmptyParts)
    self.qNum.setText(u'Вопросов: '+str(sl.count()))
    self.aNum.setText(u'Ответов: '+str(self.answEdit.getAnswCount()))
    self.prNum.setText(u'Результатов: '+str(self.calcEdit.getRCount()))
    self.srNum.setText(u'Градаций: '+str(self.calcEdit.getGCount()))
  
  def updateInterpTable(self):
    self.tableInterp.setRowCount(self.calcEdit.getGCount())
    self.tableInterp.setColumnCount(self.calcEdit.getRCount())
    self.tableInterp.setHorizontalHeaderLabels(self.calcEdit.getRNames())
    self.tableInterp.setVerticalHeaderLabels(self.calcEdit.getGNames())
    
  def updateImage(self):
    self.collectDescrData()
    
    fake_result=[int(uniform(1,self.calcEdit.getGCount()+1)) for i in range(0,self.calcEdit.getRCount())]
    self.Descriptor.createImage(fake_result)
    self.graphEdit.setImage(self.Descriptor.image)
    
    
  def collectDescrData(self):
    self.Descriptor=TestDescriptor()
    
    r_names=self.calcEdit.getRNames()
    r_keys=self.calcEdit.getRKeys()
    r_values=self.calcEdit.getRValues()
    for i in range(0,len(r_names)):
      self.Descriptor.addResult(r_names[i],r_keys[i],r_values[i])
    
    g_names=self.calcEdit.getGNames()
    g_ranges=self.calcEdit.getGRanges()
    for i in range(0,len(g_names)):
      self.Descriptor.addGradation(g_names[i],g_ranges)
      
    self.Descriptor.setImageType(self.graphEdit.getImgType())
    w,h,f=self.graphEdit.getImgSize()
    self.Descriptor.setImgSize(w,h,f)
    self.Descriptor.setHistroMaximum(self.graphEdit.getHistroMaximum())
    
    #изменить
    self.Descriptor.setCalcSteps(2)
    self.Descriptor.setResultsDescription(u'Результаты')
    self.Descriptor.setGradeDescription(u'Значения')
    

if __name__ == "__main__":
  import sys
  app = QtGui.QApplication(sys.argv)
  window=Teaport()
  window.show()
  sys.exit(app.exec_())