#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui.imageui import *

class ImageDialog(QWidget,Ui_Form):
  """Окно отображения картинки"""
  def __init__(self):
    QWidget.__init__(self,None)
    self.setupUi(self)
    self.connect(self.bt_save,SIGNAL("clicked()"),self.onSaveAs)

  def init(self,img):
    self.lbl_image.setPixmap(QPixmap.fromImage(img))
    self.show()
    self.resize(img.width(),img.height())

  def onSaveAs(self):
    filename=QFileDialog.getSaveFileName(None,QString.fromUtf8("Выберите путь для сохранения файла"),"","Images (*.png *.xpm *.jpg *bmp)")
    if filename.isNull()!=0:
      lbl_image.pixmap().save(filename);

if __name__ == "__main__":
  import sys
  app = QtGui.QApplication(sys.argv)
  window=ImageDialog()
  window.init(QImage())
  sys.exit(app.exec_())

