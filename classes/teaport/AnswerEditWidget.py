# -*- coding: utf-8 -*-


from PyQt4.QtCore import *
from PyQt4.QtGui import *

from ui.answereditui import *

#---------------------------------------------------------------
class AnswerSet:
  """Набор ответов
  
  Содержит название набора (для редактора), список ответов и их 'ролей'. Роли добавляются/удаляются синхронно с ответами"""
  def __init__(self,index=0,a_count=2):
    self.sName=u'Набор №'+str(index)
    self.sAnswers=[u'' for i in range(a_count)]
    self.sRoles=[u'' for i in range(a_count)]
    
  def setAnswCount(self,count):
    """Изменяет число ответов в большую или меньшую сторону"""
    if len(self.sAnswers)<count:
      while len(self.sAnswers)<count:
        self.sAnswers.append(u'')
        self.sRoles.append(u'')
    elif len(self.sAnswers)>count:
      self.sAnswers=self.sAnswers[0:count]
      self.sRoles=self.sRoles[0:count]
      
#---------------------------------------------------------------

class AnswerSetModel(QAbstractListModel):
  """Модель для хранения данных о наборах ответов
  
  Представлению доступно только название набора, доступ к остальным данным производится напрямую. 
  Такой изврат нужен для того, чтобы не писать модель дерева, а отделаться моделью списка."""
  def __init__(self,parent=None):
    QAbstractListModel.__init__(self,parent)
    self.a_count=2
    self.counter=1
    self.a_set=[AnswerSet(self.counter)]
    self.counter+=1
    
  def rowCount(self,parent=QModelIndex()):
    """возвращает число наборов ответов"""
    return len(self.a_set)
  
  def data(self,index,role=Qt.DisplayRole):
    """Возвращает представлению название набора ответов"""
    if index.isValid()==False or index.row() >= len(self.a_set):
      return QVariant()
    if role == Qt.DisplayRole:
      return self.a_set[index.row()].sName
  
  def setData(self,index,value,role=Qt.EditRole):
    """Изменяет название набора ответов"""
    if index.isValid()==False or index.row() >= len(self.a_set):
      return False
    if role == Qt.EditRole:
      self.a_set[index.row()].sName=value.toString()
      self.emit(SIGNAL('dataChanged'),index,index)
      return True
  
  def flags(self,index):
    flags=QAbstractListModel.flags(self,index)
    if index.isValid():
      flags=flags | Qt.ItemIsEditable
    return flags
  
  def insertRows(self,row,count,parent=QModelIndex()):
    """Добавляет набор(ы) ответов"""
    if row>len(self.a_set):
      row=len(self.a_set)-1
    if row<0:
      row=0
    count-=1
    QAbstractListModel.beginInsertRows(self,parent,row,row+count)
    self.a_set.insert(row,AnswerSet(self.counter,self.a_count))
    QAbstractListModel.endInsertRows(self)
    self.counter+=1
  
  def removeRows(self,row,count,parent=QModelIndex()):
    """Удаляет набор(ы) ответов"""
    if row>len(self.a_set):
      row=row>len(self.a_set)-1
      count=0
      if row<0:
        row=0
    QAbstractListModel.beginRemoveRows(self,parent,row,row+count)
    for i in range(row,row+count):
      del(self.a_set[i])
    QAbstractListModel.endRemoveRows(self)
  
  def chAnswCount(self,count):
    """Изменяет количество возможных ответов во ВСЕХ наборах"""
    for s in self.a_set:
      s.setAnswCount(count)
      
#---------------------------------------------------------------


class AnswerEditWidget(QWidget,Ui_AnswerEditWidget):
  """Класс виджета для редактирования ответов на вопросы
  
  Осуществляет управление наборами: создание, удаление. Добавление вариантов ответов, изменение ответов"""
  def __init__(self,parent=None):
    QWidget.__init__(self,parent)
    Ui_AnswerEditWidget.setupUi(self,self)
    
    self.as_model=AnswerSetModel()
    self.varsetList.setModel(self.as_model)
    self.a_lines=[]
    self.r_lines=[]
    
    self.connect(self.btOk,SIGNAL('clicked()'),self.onChAnswCount)
    self.connect(self.btAdd,SIGNAL('clicked()'),self.addSet)
    self.connect(self.btDel,SIGNAL('clicked()'),self.delSet)
    self.connect(self.varsetList,SIGNAL('activated(QModelIndex)'),self.onChSet)
    
    #Нулевой элемент будет выделен по-умолчанию
    self.lastRow=0
    self.varsetList.setCurrentIndex(self.as_model.index(0))
    #Сразу добавляем два варианта ответа - разумно для теста. Кому нужен тест с одним вариантом ответа?..
    self.spinNumVariants.setValue(2)
    self.onChAnswCount()
    self.btDel.setDisabled(True)
    
  def onChAnswCount(self):
    """Изменяет число возможных ответов. 
    
    Инициирует добавление/удаление данных в модели, а также добавляет/удаляет QLineEdit в зависимости от нового числа ответов"""
    
    #Изменения в модели
    self.as_model.chAnswCount(self.spinNumVariants.value())
    #Изменяем число виджетов редактирования
    if self.spinNumVariants.value()>len(self.a_lines):
      while self.spinNumVariants.value()>len(self.a_lines):
        self.a_lines.append(QLineEdit(u'Ответ №'+str(len(self.a_lines)+1)))
        self.r_lines.append(QLineEdit(u'Баллов за ответ №'+str(len(self.r_lines)+1)))
        self.layVariants.addWidget(self.a_lines[-1])
        self.layRoles.addWidget(self.r_lines[-1])
      
    elif self.spinNumVariants.value()<len(self.a_lines):
      while self.spinNumVariants.value()<len(self.a_lines):
        self.layVariants.removeWidget(self.a_lines[-1])
        self.layRoles.removeWidget(self.r_lines[-1])
        self.a_lines[-1].hide()
        self.r_lines[-1].hide()
        del(self.a_lines[-1])
        del(self.r_lines[-1])
    self.emit(SIGNAL('answersChanged()'))
  
  def addSet(self):
    """Добавляет набор вариантов ответов в модель"""
    self.as_model.insertRows(len(self.as_model.a_set),1)
    self.btDel.setEnabled(True)
    
  def delSet(self):
    """Удаляет набор вариантов ответов из модели
    
    В процессе удаления сбрасывает указатель на прошлое выделение, чтобы не сохранять удалённые данные
    Устанавливает выделение на следующий по списку элемент"""
    rtd=self.varsetList.currentIndex().row()
    self.varsetList.setCurrentIndex(self.as_model.index(rtd+1))
    self.lastRow=-1
    self.as_model.removeRows(rtd,1)
    if len(self.as_model.a_set)==1:
      self.btDel.setDisabled(True)
    
  def onChSet(self,index):
    """Вызывается при изменении выделения в списке наборов ответов
    
    При изменении выделения сохраняются введённые данные, загружается новые, устанавливается новый указательна "прошлый" элемент"""
    #Сохранение
    if self.lastRow!=-1:
      name=unicode(self.as_model.data(self.as_model.index(self.lastRow,0)))
      for a in self.as_model.a_set:
        if a.sName==name:
          a.sAnswers=[ t.text() for t in self.a_lines]
          a.sRoles=[ t.text() for t in self.r_lines]
          break
    #Заполнение данными из выделенного набора
    self.lastRow=index.row()
    name=unicode(self.as_model.data(self.as_model.index(index.row(),0)))
    for a in self.as_model.a_set:
      if a.sName==name:
        for i in range(0,len(self.a_lines)):
          self.a_lines[i].setText(a.sAnswers[i])
          self.r_lines[i].setText(a.sRoles[i])
        break
  
  def getAList(self):
    """Форматирует введённые данные в список строк, готовый для записи в файл построчно"""
    a_list=[]
    for a_s in self.as_model.a_set:
      answ=''
      for a in a_s.sAnswers:
        answ+='['+a+']'
      a_list.append(answ)
    return a_list

  def getRList(self):
    """Форматирует введённые данные в список строк, готовый для записи в файл построчно"""
    r_list=[]
    for a_s in self.as_model.a_set:
      role=''
      for a in a_s.sRoles:
        role+='['+a+']'
      r_list.append(role)
    return r_list

  def getAnswCount(self):
    """Возвращает число вариантов ответов"""
    return self.spinNumVariants.value()
  
  def getASetCount(self):
    """возвращает число наборов вариантов ответов"""
    return len(self.as_model.a_set)      
#---------------------------------------------------------------


if __name__ == "__main__":
  import sys
  app = QtGui.QApplication(sys.argv)
  window=AnswerEditWidget()
  window.show()
  sys.exit(app.exec_())