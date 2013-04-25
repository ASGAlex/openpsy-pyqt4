#!/usr/bin/python 
# -*- coding: utf-8 -*- 
from PyQt4.QtCore import * 
from PyQt4.QtGui import * 
from classes.tests.TestWindow import *
from classes.alg.visual import *
from classes.alg.TestDescriptor import *
import sys
import os 

def calculate(answers): 
  #Ключ к тесту
  internality=(1,-5,9,-13,-17,-21,25,29,33,37)
  trevoga=(2,-6,10,14,-18,22,-26,30,-34,-38)
  nozg=(-3,7,11,-15,-19,-23,27,31,35,39)
  activity_ctrl=(4,-8,-12,16,-20,24,-28,-32,-36,-40)
  
  keys=(internality,trevoga,nozg,activity_ctrl)
  
  results=[0,0,0,0,0]
  print results
  #считаем всё
	
  for i in range(0,len(keys)):
    for val in keys[i]:
      if (val>0 and answers[abs(val)-1]>0) or (val<0 and answers[abs(val)-1]<0):
	results[i]+=answers[abs(val)-1]
      else:
	results[i]-=answers[abs(val)-1]
  
  all_napr=0
  for r in results:
    all_napr+=r
  all_napr=all_napr/4
  results.append(all_napr)
  
  return results
  
def showResult(result): 
  text=u'Результаты тестирования:<br>'
  
  text+=u'<b>Интеринальность: </b>'+str(result[0])+'.   '
  if result[0]>0:
    text+=u'Причины болезни воспринимаются как нечто, не зависящее от родителей, что они не могут контролировать и чем не могут управлять.'
  elif result[0]<0:
    text+=u'Родители воспринимают себя как ответственных за болезнь ребенка.'
  text+='<br>'
  
  
  text+=u'<b>Тревога: </b>'+str(result[1])+'.   '
  if result[1]>15:
    text+=u'Выраженная тревога'
  elif result[1]<0 and result[1]>-15:
    text+=u'Относительно нейтральное отношение к болезни ребенка.'
  elif result[1]<-15:
    text+=u'Крайняя степень отрицания тревоги. Возможно, тревога вытесняется.'
  else:
    text+=u'Уровень тревоги в норме'
  text+='<br>'
  
  text+=u'<b>Нозогнозия: </b>'+str(result[2])+'.   '
  if result[2]>15:
    text+=u'Преувеличение родителями тяжести болезни ребенка.'
  elif result[2]<-10:
    text+=u'Преуменьшение родителями тяжести болезни ребенка '
  else:
    text+=u'Тяжесть болезни сильно не преувеличивается и не преуменьшается.'
  text+='<br>'
  
  text+=u'<b>Контроль активности: </b>'+str(result[3])+'.   '
  if result[3]>15:
    text+=u'Тенденция родителей устанавливать на время болезни максимальные ограничения активности ребенка («покой лечит»).'
  elif result[3]<-15:
    text+=u'Тенденция недооценки соблюдения необходимых ограничений активности.'
  else:
    text+=u'Ограничения активности больного ребёнка в разумных пределах'
  text+='<br>'
  
  
  text+=u'<b>Общая напряженность: </b>'+str(result[4])+'.   '
  if result[4]>15:
    text+=u'Напряженное отношение к заболеванию ребенка.'
  text+='<br>'
  
  return text#функция должна вернуть сформированный текст. Используйте функцию unicode() для кириллического текста 
  
def drawImage(result): 
  #Вставте код рисования графика, описывающего ваш результат 
  #переменная result содержит результат тестирования 
  return #Функция должна возвращать переменную типа QImage() 

window=TestWindow() 
def init():
  WindowTitle=u"Заголовок окна"
  #Этот код вам не придётся изменять
  window.createTest("DOBR") 
  window.setLogic(calculate,showResult,drawImage) 
  window.setWindowTitle(WindowTitle)
  window.show() 
