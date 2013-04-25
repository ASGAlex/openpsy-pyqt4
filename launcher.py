#!/usr/bin/python
# -*- coding: utf-8 -*- 
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from classes.launcher.LauncherDialog import *
import sys
import os

os.chdir(os.path.dirname(sys.argv[0]))
app = QtGui.QApplication(sys.argv)
window=LauncherDialog(os.path.dirname(sys.argv[0])+u'/tests')
window.show()
sys.exit(app.exec_())
