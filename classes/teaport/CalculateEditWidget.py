# -*- coding: utf-8 -*-


from PyQt4.QtCore import *
from PyQt4.QtGui import *

from ui.calculateeditui import *
from math import *

class ResultCalc:
  """Данные о способах расчёта результатов
  
  Содержит в себе нвзвание результата, значения, ключи"""
  def __init__(self, count=1):
    self.numbers=''
    self.keys=''
    self.name=u'Результат №'+str(count)
    self.fr=[0]
    self.to=[0]
    
  
  def nFromLine(self):
    """Преобразует строку в список номеров ответов"""
    try:
      s_to_exec=str("numbers=["+self.numbers+"]")
      exec(s_to_exec)
      #меняем отрицательные значения на положительные"""
      numbers=[ n*(-1) for n in self.numbers if n<0]
      return numbers
    except SyntaxError:
      return u'Введены недопустимые символы в список номеров ответов'
  
  def kFromLine(self):
    """Преобразует строку в список ключей"""
    try:
      s_to_exec=str('keys=['+self.keys+']')
      exec(s_to_exec)
      return keys
    except SyntaxError:
      return u'Введены недопустимые символы в список ключей'
  
  def genKey(self):
    """Герерирует простой ключ по списку номеров ответов"""
    keys=[ n/abs(n) for n in self.numbers]
    return keys
    

  def chGCount(self,count):
    if len(self.fr)<count:
      while len(self.fr)<count:
        self.fr.append(0)
        self.to.append(0)
    elif len(self.fr)>count:
      self.fr=self.fr[0:count]
      self.to=self.to[0:count]


class Grades:
  """Данные о градации оценки
  
  Содержит название градации и её диапазон"""
  def __init__(self, count=1):
    self.name=u'Градация №'+str(count)
  




class ResultCalcModel(QAbstractListModel):
  """Модель управляет списком результатов"""
  def __init__(self,parent=None):
    QAbstractListModel.__init__(self,parent)
    self.a_calc=[ResultCalc()]
    self.counter=2
    
  def rowCount(self,parent=QModelIndex()):
    """возвращает число наборов ответов"""
    return len(self.a_calc)
  
  def data(self,index,role=Qt.DisplayRole):
    """Возвращает представлению название набора ответов"""
    if index.isValid()==False or index.row() >= len(self.a_calc):
      return QVariant()
    if role == Qt.DisplayRole:
      return self.a_calc[index.row()].name
  
  def setData(self,index,value,role=Qt.EditRole):
    """Изменяет название набора ответов"""
    if index.isValid()==False or index.row() >= len(self.a_calc):
      return False
    if role == Qt.EditRole:
      self.a_calc[index.row()].name=value.toString()
      self.emit(SIGNAL('dataChanged'),index,index)
      return True
  
  def flags(self,index):
    flags=QAbstractListModel.flags(self,index)
    if index.isValid():
      flags=flags | Qt.ItemIsEditable
    return flags
  
  def insertRows(self,row,count,parent=QModelIndex()):
    """Добавляет набор(ы) ответов"""
    if row>len(self.a_calc):
      row=len(self.a_calc)-1
    if row<0:
      row=0
    count-=1
    QAbstractListModel.beginInsertRows(self,parent,row,row+count)
    self.a_calc.insert(row,ResultCalc(self.counter))
    QAbstractListModel.endInsertRows(self)
    self.counter+=1
  
  def removeRows(self,row,count,parent=QModelIndex()):
    """Удаляет набор(ы) ответов"""
    if row>len(self.a_calc):
      row=row>len(self.a_calc)-1
      count=0
      if row<0:
        row=0
    QAbstractListModel.beginRemoveRows(self,parent,row,row+count)
    for i in range(row,row+count):
      del(self.a_calc[i])
    QAbstractListModel.endRemoveRows(self)


class GradeModel(QAbstractListModel):
  """Модель управляет списком результатов"""
  def __init__(self,parent=None):
    QAbstractListModel.__init__(self,parent)
    self.grades=[Grades()]
    self.counter=2
    
  def rowCount(self,parent=QModelIndex()):
    """возвращает число наборов ответов"""
    return len(self.grades)
  
  def data(self,index,role=Qt.DisplayRole):
    """Возвращает представлению название набора ответов"""
    if index.isValid()==False or index.row() >= len(self.grades):
      return QVariant()
    if role == Qt.DisplayRole:
      return self.grades[index.row()].name
  
  def setData(self,index,value,role=Qt.EditRole):
    """Изменяет название набора ответов"""
    if index.isValid()==False or index.row() >= len(self.grades):
      return False
    if role == Qt.EditRole:
      self.grades[index.row()].name=value.toString()
      self.emit(SIGNAL('dataChanged'),index,index)
      return True
  
  def flags(self,index):
    flags=QAbstractListModel.flags(self,index)
    if index.isValid():
      flags=flags | Qt.ItemIsEditable
    return flags
  
  def insertRows(self,row,count,parent=QModelIndex()):
    """Добавляет набор(ы) ответов"""
    if row>len(self.grades):
      row=len(self.grades)-1
    if row<0:
      row=0
    count-=1
    QAbstractListModel.beginInsertRows(self,parent,row,row+count)
    self.grades.insert(row,Grades(self.counter))
    QAbstractListModel.endInsertRows(self)
    self.counter+=1
  
  def removeRows(self,row,count,parent=QModelIndex()):
    """Удаляет набор(ы) ответов"""
    if row>len(self.grades):
      row=row>len(self.grades)-1
      count=0
      if row<0:
        row=0
    QAbstractListModel.beginRemoveRows(self,parent,row,row+count)
    for i in range(row,row+count):
      del(self.grades[i])
    QAbstractListModel.endRemoveRows(self)



class CalculateEditWidget(QWidget,Ui_CalculateEdit):
  def __init__(self,parent=None):
    QWidget.__init__(self,parent)
    Ui_CalculateEdit.setupUi(self,self)
    self.g_model=GradeModel()
    self.r_model=ResultCalcModel()
    self.listResults.setModel(self.r_model)
    self.listGrades.setModel(self.g_model)
    
    self.connect(self.btAddRes,SIGNAL('clicked()'),self.onAddRes)
    self.connect(self.btDelRes,SIGNAL('clicked()'),self.onDelRes)
    
    self.connect(self.btAddGrade,SIGNAL('clicked()'),self.onAddGrade)
    self.connect(self.btDelGrade,SIGNAL('clicked()'),self.onDelGrade)
    
    
    self.connect(self.listResults,SIGNAL('activated(QModelIndex)'),self.onChR)
    self.connect(self.listGrades,SIGNAL('activated(QModelIndex)'),self.onChG)
    
    self.connect(self.chManualKey,SIGNAL('toggled(bool)'),self.onManualKey)
    self.chManualKey.setChecked(False)
    self.onManualKey(False)
    
    self.r_lastRow=0
    self.listResults.setCurrentIndex(self.r_model.index(0))
    self.g_lastRow=0
    self.listGrades.setCurrentIndex(self.g_model.index(0))
    self.btDelGrade.setDisabled(True)
    self.btDelRes.setDisabled(True)
  
  def onAddRes(self):
    self.r_model.insertRows(len(self.r_model.a_calc),1)
    for a in self.r_model.a_calc:
      a.chGCount(len(self.g_model.grades))
    self.btDelRes.setEnabled(True)
    self.emit(SIGNAL('resultsChanged()'))
    
  def onDelRes(self):
    rtd=self.listResults.currentIndex().row()
    self.listResults.setCurrentIndex(self.r_model.index(rtd+1))
    self.r_lastRow=-1
    self.r_model.removeRows(rtd,1)
    for a in self.r_model.a_calc:
      a.chGCount(len(self.g_model.grades))
    if len(self.r_model.a_calc)==1:
      self.btDelRes.setDisabled(True)
    self.emit(SIGNAL('resultsChanged()'))
    
  def onAddGrade(self):
    self.g_model.insertRows(len(self.g_model.grades),1)
    for a in  self.r_model.a_calc:
      a.fr.append(0)
      a.to.append(0)
    self.btDelGrade.setEnabled(True)
    self.emit(SIGNAL('gradesChanged()'))
    
  def onDelGrade(self):
    rtd=self.listResults.currentIndex().row()
    self.listResults.setCurrentIndex(self.g_model.index(rtd+1))
    for a in  self.r_model.a_calc:
      del a.fr[rtd]
      del a.to[rtd]
    self.g_lastRow=-1
    self.g_model.removeRows(rtd,1)
    if len(self.g_model.grades)==1:
      self.btDelGrade.setDisabled(True)
    self.emit(SIGNAL('gradesChanged()'))
    
    
    
  def onChR(self,index):
    #Сохранение
    if self.r_lastRow!=-1:
      name=unicode(self.r_model.data(self.r_model.index(self.r_lastRow,0)))
      for a in self.r_model.a_calc:
        if a.name==name:
          a.numbers=self.lineAnswNum.text()
          a.keys=self.lineAnswKey.text()
          a.fr[self.listGrades.currentIndex().row()]=self.lineGradeFrom.text()
          a.to[self.listGrades.currentIndex().row()]=self.lineGradeTo.text()
          break
    #Заполнение данными из выделенного набора
    self.r_lastRow=index.row()
    name=unicode(self.r_model.data(self.r_model.index(index.row(),0)))
    for a in self.r_model.a_calc:
      if a.name==name:
        self.lineAnswNum.setText(a.numbers)
        self.lineAnswKey.setText(a.keys)
        self.lineGradeFrom.setText(str(a.fr[self.listGrades.currentIndex().row()]))
        self.lineGradeTo.setText(str(a.to[self.listGrades.currentIndex().row()]))
        break


  def onChG(self,index):
    #Сохранение
    if self.g_lastRow!=-1:
      name=unicode(self.g_model.data(self.g_model.index(self.g_lastRow,0)))
      for g in self.g_model.grades:
        if g.name==name:
          self.r_model.a_calc[self.listResults.currentIndex().row()].fr[self.g_lastRow]=self.lineGradeFrom.text()
          self.r_model.a_calc[self.listResults.currentIndex().row()].to[self.g_lastRow]=self.lineGradeTo.text()
          break
    #Заполнение данными из выделенного набора
    self.g_lastRow=index.row()
    name=unicode(self.g_model.data(self.g_model.index(index.row(),0)))
    for g in self.g_model.grades:
      if g.name==name:
        self.lineGradeFrom.setText(str(self.r_model.a_calc[self.listResults.currentIndex().row()].fr[index.row()]))
        self.lineGradeTo.setText(str(self.r_model.a_calc[self.listResults.currentIndex().row()].to[index.row()]))
        break
  
  def onManualKey(self,enabled):
    self.lineAnswKey.setEnabled(enabled)
    self.labelKeyName.setEnabled(enabled)
    
  def getRCount(self):
    return len(self.r_model.a_calc)
  
  def getGCount(self):
    return len(self.g_model.grades)
    
  def getRNames(self):
    return [ r.name for r in self.r_model.a_calc]
  
  def getRValues(self):
    """На выходе выдаёт массив, содержащий списки переменных 
    
    [
      [Список, ответов, для, вычислдения, результатов], #результат №
      [...],
      ...
      [...]
    ]"""
    return [ r.nFromLine() for r in self.r_model.a_calc]
  
  def getRKeys(self):
    """На выходе выдаёт массив, содержащий списки ключей (см. выше)"""
    if self.chManualKey.isEnabled()==False:
      return [ r.genKey() for r in self.r_model.a_calc]
    else:
      return [ r.kFromLine() for r in self.r_model.a_calc]
    
  def getGNames(self):
    return [ g.name for g in self.g_model.grades]

  def getGRanges(self):
    arr=[]
    for i in range(0,len(self.g_model.grades)):
      row=[]
      for j in range(0,len(self.r_model.a_calc)):
        row.append([self.r_model.a_calc[j].fr[i],self.r_model.a_calc[j].to[i]])
      arr.append(row)
    return arr
  