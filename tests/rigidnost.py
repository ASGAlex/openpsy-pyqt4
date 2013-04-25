#!/usr/bin/python 
# -*- coding: utf-8 -*- 
from PyQt4.QtCore import * 
from PyQt4.QtGui import * 
from classes.tests.TestWindow import *
import sys 
import os 

def calculate(answers): 
  #Вставьте сюда свой код вычисления результата 
  #Переменная answers содержит список ответов, данных пользователем 
  #Способы назначения ответа указаны в файле rigidnost/Answer_role.txt 
  index=[[2, 3, 5, 7, 10, 12, 15, 16, 17, 19, 21, 22, 24, 25, 28, 29, 32, 35, 36, 37, 41, 42, 45, 47, 49],[1, 4, 6, 8, 9, 11, 13, 14, 18, 20, 23, 26, 27, 30, 31, 33, 34, 38, 39, 40, 43, 44, 46, 48, 50]]
  result=0
  #Уменяшаем индексы на 1  и складываем
  for i in range(0,len(index[0])):
    index[0][i]-=1;#Уменьшаем значение индекса на 1, тем самым делая его рабочим
    index[1][i]-=1;
    if answers[index[0][i]]==1:
      result+=1;
    if answers[index[1][i]]==2:
      result+=1;
    print 'result=',result
    print 'answers[index[0][i]]=',answers[index[0][i]]
  return result#функция должна вернуть вычесленный результат/результаты 
  
def showResult(result): 
  #Вставьте сюда код создания текста, описывающего результат 
  #Данный текст будет выведен на экран после прохождения теста 
  #переменная result содержит результат тестирования 
  text=u'<b>Результат:</b> <br>'+unicode(result)
  if result>=0 and result<=13:
    text=text+u' - мобильный;'
  elif result>=14 and result<=27:
    text=text+u' - проявляет черты ригидности и мобильности;'
  elif result>=28 and result<=40:
    text=text+u' - ригидный;'
  
  return unicode(text)#функция должна вернуть сформированный текст. Используйте функцию unicode() для кириллического текста 
  
def drawImage(result): 
  #Вставте код рисования графика, описывающего ваш результат 
  #переменная result содержит результат тестирования 
  return #Функция должна возвращать переменную типа QImage() 
  
window=TestWindow() 
def init():
  WindowTitle=u"Методика измерения ригидности"
  #Этот код вам не придётся изменять
  window.createTest("rigidnost") 
  window.setLogic(calculate,showResult,drawImage) 
  window.setWindowTitle(WindowTitle)
  window.show() 
