#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui.launcherui import *
import sys 

class PyDirModel(QAbstractListModel):
  def __init__(self,path,parent=None):
    QAbstractItemModel.__init__(self,parent)
    directory=QDir(path)
    s_filter=QStringList("*.py")
    self.files=directory.entryList(s_filter,QDir.Files,QDir.Name)
    i=0
    while i< len(self.files):
      if self.files[i].toLower()=="__init__.py" or self.files[i].toLower()=="make_test.py":
        self.files.removeAt(i)
      i=i+1
      
  def rowCount(self,parent=QModelIndex()):
    return self.files.count()
    
  def data(self,index, role=Qt.DisplayRole):
    if index.isValid()==False or index.row() >= self.files.count():
      return QVariant()
    if role == Qt.DisplayRole:
      return self.files[index.row()]
    elif role==Qt.DecorationRole:
      icon=QIcon()
      icon.addPixmap(QPixmap("icons/psy.png"))
      return icon

class LauncherDialog(QMainWindow,Ui_MainWindow):
  def __init__(self,path):
    QMainWindow.__init__(self,None)
    self.setupUi(self)
    
    self.fs_model=PyDirModel(path,self)
    
    self.listView.setModel(self.fs_model)
    #self.listView.setRootIndex(QModelIndex())
    
    self.actIconMode.setChecked(True)
    self.connect(self.act_exit,SIGNAL('triggered()'),qApp.exit)
    
    self.connect(self.actIconMode,SIGNAL('triggered()'),self.onIconMode)
    self.connect(self.actListMode,SIGNAL('triggered()'),self.onListMode)
    
    self.connect(self.listView,SIGNAL('doubleClicked(QModelIndex)'),self.startProgram)
    self.connect(self.bt_ok,SIGNAL('clicked()'),self.startProgram)
    
  def onIconMode(self):
    self.listView.setViewMode(QListView.IconMode)
    self.actIconMode.setChecked(True)
    self.actListMode.setChecked(False)
    
  def onListMode(self):
    self.listView.setViewMode(QListView.ListMode)
    self.actIconMode.setChecked(False)
    self.actListMode.setChecked(True)
    
  def startProgram(self):
    prog_name=self.fs_model.data(self.listView.currentIndex())
    print prog_name
    prog_name=prog_name[:-3]
    expr="""from tests import %s
%s.init()
""" % (prog_name,prog_name)
    exec(expr)
    
    
    
  
  def closeEvent(self,event):
    qApp.exit()
    