#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from ui.mainwindowui import *
from HelpDialog import *
from ImageDialog import *

class BasicTestWindow(QMainWindow,Ui_MainWindow):
  """Базовый класс окна тестов"""
  def __init__(self):
    QMainWindow.__init__(self,None)
    #Инициализация интерфейса Designer
    self.setupUi(self)
    self.bt_next.hide()
    self.bt_prev.hide()
    self.bt_multi.hide()
    self.progressBar.hide()
    #self.main_text.setReadOnly(True)
    #Соединяем сигналы и слоты
    self.connect(self.act_new_test,SIGNAL("triggered()"),self.onNewTest)

    #help
    self.connect(self.act_about,SIGNAL("triggered()"),self.onAbout)
    self.connect(self.act_about_qt,SIGNAL("triggered()"),qApp.aboutQt)


    #basic variables
    self.QuestionsCount=0
    self.CurrentQuestion=0
    self.state="NO_TEST"
    self.image=0
    self.zoom=1.0

    #preparing non-modal image dialog
    self.image_dialog=ImageDialog()

    #text data
    self.hello_text="hello_text"
    self.instruction_text="instruction"
    self.help_text="help"
    self.authors_text="authors"
    self.license_text="license"


  def setHelloText(self):
    """setting hello_text to main_text"""
    self.main_text.setHtml(self.hello_text)

  def onNewTest(self):
    """выбран пункт меню 'Начать тест'"""
    self.CurrentQuestion=0
    self.main_text.setHtml(self.instruction_text)
    self.state="NEW_STARTED"
    self.bt_multi.setText(QString.fromUtf8("Начать тестирование"))
    self.main_text.setHtml(self.instruction_text)
    self.bt_multi.show()

  def onMulti(self):
    if self.state=="NEW_STARTED":
      #настроить вид мульти-кнопки
      self.bt_multi.hide()
      self.bt_multi.setText(QString.fromUtf8("Завершить тест"))

      #Настроить счётчик
      self.progressBar.show()
      self.progressBar.setMinimum(0)
      self.progressBar.setMaximum(self.QuestionsCount)
      self.progressBar.setValue(self.CurrentQuestion+1)

      #настроить кнопки"вперёд-назад"
      self.bt_prev.show()
      self.bt_prev.setDisabled(True)
      self.bt_next.show()
      self.bt_next.setDisabled(True)
    elif self.state=="TEST_FINISHED":
      #настроить вид мульти-кнопки
      try:
        print 'image width='+str(self.image.width())
        print 'image height='+str(self.image.height())
        self.state="SHOW_PIC"
      except AttributeError:
        print 'no image, hiding button'
        self.bt_multi.hide()
      self.bt_multi.setText(QString.fromUtf8("Показать график"))
      self.bt_multi.setEnabled(True)

      #настроить кнопки"вперёд-назад"
      self.bt_prev.setDisabled(True)
      self.bt_next.setDisabled(True)

      #Настроить счётчик
      self.progressBar.hide()
    elif self.state=="SHOW_PIC":
      self.onShowPic()

  def onPrev(self):
    self.CurrentQuestion-=1
    self.bt_prev.setDisabled(True)
    self.bt_next.setEnabled(True)
    #self.progressBar.setValue(self.CurrentQuestion)

  def onNext(self):
    self.CurrentQuestion+=1
    self.bt_next.setDisabled(True)
    self.bt_prev.setEnabled(True)
    #self.progressBar.setValue(self.CurrentQuestion)


  def onShowPic(self):
    self.image_dialog.init(self.image)

  def onAbout(self):
    help=HelpDialog()
    help.setHelpText(self.help_text)
    help.setAuthorsText(self.authors_text)
    help.setLicenseText(self.license_text)
    help.exec_()







if __name__ == "__main__":
  import sys
  app = QtGui.QApplication(sys.argv)
  window=BasicTestWindow()
  window.show()
  sys.exit(app.exec_())

