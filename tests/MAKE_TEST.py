#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import shutil
#new program name
if len(sys.argv)==1:
  print 'Не указано имя теста в качестве аргумента. Попробуйте ещё раз.'
  exit()
next_is_template=False
template_folder=""
for name in sys.argv[1:]:
  if name=='-t' or name=='--template':
    next_is_template=True
  elif next_is_template:
    print 'template dir is '+ name
    template_folder=name
    next_is_template=False
  else:
    print name
    #template
    code="""#!/usr/bin/python 
# -*- coding: utf-8 -*- 
from PyQt4.QtCore import * 
from PyQt4.QtGui import * 
from classes.tests.TestWindow import *
from classes.alg.visual import *
import sys
import os 

os.chdir(os.path.dirname(sys.argv[0]))
def calculate(answers): 
  #Вставьте сюда свой код вычисления результата 
  #Переменная answers содержит список ответов, данных пользователем 
  #Способы назначения ответа указаны в файле %s/Answer_role.txt 
  return #функция должна вернуть вычесленный результат/результаты 
  
def showResult(result): 
  #Вставьте сюда код создания текста, описывающего результат 
  #Данный текст будет выведен на экран после прохождения теста 
  #переменная result содержит результат тестирования 
  return #функция должна вернуть сформированный текст. Используйте функцию unicode() для кириллического текста 
  
def drawImage(result): 
  #Вставте код рисования графика, описывающего ваш результат
  #Используйте img=makeHistro(result,(РазмерХ,РазмерY,РазмерШрифта),НазванияКолонок,МаксимальноеЗначение,РазноцветныеКолонки) для построения гистрограммы
  #Используйте img=makeGraph(result,(РазмерХ,РазмерY,РазмерШрифта),((ПодписиОсиX),(ПодписиОсиY))) для построения графика
  return #Функция должна возвращать переменную типа QImage() 
  
#Укажите здесь заголовок окна программы
WindowTitle=u"Заголовок окна"

#Этот код вам не придётся изменять
def init():
  #Этот код вам не придётся изменять
  window.createTest(%s) 
  window.setLogic(calculate,showResult,drawImage) 
  window.setWindowTitle(WindowTitle)
  window.show() 
""" % (name,'"'+name+'"')


    os.makedirs(name)
    f=open(name+".py","w")
    f.write(code)
    f.close()

    name=name+'/'
    f_orig_list=('Answer_role.txt','Answers.txt','Authors.txt','Help.txt','Instruction.txt','Intro.txt','License.txt','Questions.txt')
    f_list=(name+'Answer_role.txt',name+'Answers.txt',name+'Authors.txt',name+'Help.txt',name+'Instruction.txt',name+'Intro.txt',name+'License.txt',name+'Questions.txt',name+'Shortcuts.txt')

    t_list=('''Укажите, какое значение записывать в массив ответов при выборе одного из вариантов.
Формат записи: [Ответ-1][Ответ-2][Ответ-3]...[Ответ N].
Содержимое файла может выглядеть, например, так: [-2][-1][0][1][2]. Это означает, что при выборе первого варианта ответа будет записано число "-2", при выборе второго - "-1", третьего - "0" и так далее''','''Укажите список ответов.
Если на все вопросы предполагается один шаблон ответов (к примеру - либо "да", либо "нет"), то файл должен содержать одну строку.
Если для каждого вопроса предполагается свой шаблон ответов (к примеру, для первого вопроса либо "да" либо "нет", а для второго вопроса - "согласен" или "несогласен"), то каждый шаблон должен быть указан в отдельной строке.
Шаблон имеет следующий формат: [Ответ-1][Ответ-2][Ответ-3]...[Ответ N]. ''', '''Укажите сведения об авторах методики или программы.
Эта информация будет доступна пользователю в разделе помощи.
Можно использовать html-тэги.''','''Здесь должна содержаться помощь по программе или представляемой ею методике.
Можно использовать html-тэги.''','''Укажите инструкцию к тесту (опроснику).
Инструкция будет предъявлена пользователю перед прохождением тестирования.
Можно использовать html-тэги.''','''Краткое описание программы, вводные указания пользователю.
Будет отображаться один раз при запуске программы.
Можно использовать html-тэги.''','''Текст лицензионного соглашения с пользователем.
Минздрав CCCP рекомендует GPL.''','''Укажите список вопросов, задаваемых пользователю.
Каждый вопрос указывается в отдельной строке. Не оставляйте пустых строк.''','''Укажите быструю клавишу для каждой кнопки ответа.''')
    if len(template_folder)!=0:
      for f in f_orig_list:
	if os.path.exists(template_folder+'/'+f):
	  shutil.copyfile(template_folder+'/'+f,name+'/'+f)
    try:
      for i in range(0,len(f_list)):
	if os.path.exists(f_list[i])!=True:
	  f=open(f_list[i],"w")
	  f.write(t_list[i])
	  f.close()
    except:
      print 'Произошла какая-то ошибка, извините. Операция не завершена.'
	  



