#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui.helpui import *

class HelpDialog(QDialog,Ui_Dialog):
  """Окно отображения помощи"""
  def __init__(self):
    QDialog.__init__(self,None)
    self.setupUi(self)
  def setHelpText(self,text):
    self.text_about.setHtml(text)
    
  def setAuthorsText(self,text):
    self.text_authors.setHtml(text)
    
  def setLicenseText(self,text):
    self.text_license.setHtml(text)
  