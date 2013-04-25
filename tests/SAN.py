#!/usr/bin/python 
# -*- coding: utf-8 -*- 
from PyQt4.QtCore import * 
from PyQt4.QtGui import * 
from classes.tests.TestWindow import *
import sys 
import os 

def calculate(answers): 

  #самочуствие:
  S=float(-(answers[0]-4+answers[1]-4+answers[6]-4+answers[7]-4+answers[12]-4+answers[13]-4+answers[18]-4+answers[19]-4+answers[24]-4+answers[25]-4)/10.0)
  #активность:
  A=float((answers[2]+4+answers[3]+4+answers[8]+4+answers[9]+4+answers[14]+4+answers[15]+4+answers[20]+4+answers[21]+4+answers[26]+4+answers[27]+4)/10.0)
  #Настроение:
  N=float(-(answers[4]-4+answers[5]-4+answers[10]-4+answers[11]-4+answers[16]-4+answers[17]-4+answers[22]-4+answers[23]-4+answers[28]-4+answers[29]-4)/10.0)

  return [S,A,N]
  
def showResult(result): 
  S,A,N=result
  text=u'<b>Результаты:</b><br>'
  
  text+=u'Самочуствие: '+str(S)+'.'
  if S<4:
    text+=u'Плохое самочуствие'
  elif S>=4 and S<=5:
    text+=u'Нормальное самочуствие'
  elif S>5:
    text+=u'Хорошее самочуствие'
  text+='<br>'
  
  text+=u'Активность: '+str(A)+'.'
  if A<4:
    text+=u'Пониженная активность'
  elif A>=4 and A<=5:
    text+=u'Нормальная активность'
  elif A>5:
    text+=u'Повышенная активность'
  text+='<br>'
  
  text+=u'Настроение: '+str(N)+'.'
  if N<4:
    text+=u'Плохое настроение'
  elif N>=4 and N<=5:
    text+=u'Нормальное настроение'
  elif N>5:
    text+=u'Хорошее настроение'
  text+='<br>'
  
  return text
  
def drawImage(result): 
  text_x=[u'Самочуствие',u'Активность',u'Настроение']
  img=makeHistro(result,(480,320,12),text_x,4,True)
  return img
  
window=TestWindow() 
def init():
  WindowTitle=u"Самочуствие,Активность,Настроение"
  #Этот код вам не придётся изменять
  window.createTest("SAN") 
  window.setLogic(calculate,showResult,drawImage) 
  window.setWindowTitle(WindowTitle)
  window.show() 
