#!/usr/bin/python
# -*- coding: utf-8 -*-


from string import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from BasicTestWindow import *
from .. alg.TestDescriptor import *
from .. alg.visual import *



class TestWindow(BasicTestWindow):
  """Базовый класс окна тестов с обработкой вопросов"""
  def __init__(self):
    #creating UI and basic connections
    BasicTestWindow.__init__(self)

    #buttons
    self.connect(self.bt_multi,SIGNAL("clicked()"),self.onMulti)
    self.connect(self.bt_prev,SIGNAL("clicked()"),self.onPrev)
    self.connect(self.bt_next,SIGNAL("clicked()"),self.onNext)
    self.created=False

    self.questions=[]
    self.answers=[]
    self.answer_text=[]
    self.answer_role=[]
    self.shortcuts=''
    
    self.descr=TestDescriptor()

  def loadData(self,folder):
    """loading all needed data for test from folder"""
    files_to_load=("Questions.txt","Answers.txt","Answer_role.txt","Shortcuts.txt","Intro.txt","Instruction.txt","Help.txt","Authors.txt","License.txt")

    containers=[self.questions,self.answer_text,self.answer_role,self.shortcuts,self.hello_text,self.instruction_text,self.help_text,self.authors_text,self.license_text]

    #loading all text data into string or string list - depending on container type
    for i in range(0,len(containers)):
      qfile=QFile(folder+'/'+files_to_load[i])
      if qfile.open(QIODevice.ReadOnly)==True:
        stream=QTextStream(qfile)
        stream.setCodec("UTF-8");
        if type(containers[i])==type([]):
          while stream.atEnd()!=True:
            containers[i].append(stream.readLine())
        elif type(containers[i])==type(''):
          containers[i]=stream.readAll()
      qfile.close()

    #unpacking
    self.questions,self.answer_text,self.answer_role,self.shortcuts,self.hello_text,self.instruction_text,self.help_text,self.authors_text,self.license_text=containers


    self.QuestionsCount=len(self.questions)

  def prepareButtons(self):
    """Подготовка кнопок-ответов

    Подготавливает кнопки ответов: выясняем, один шаблон для ответов, или для каждого ответа свой шаблон. Далее в список шаблонов добавляем список ответов. """
    answers=[]
    answer_role=[]
    if len(self.answer_text)<self.QuestionsCount:
      #Один шаблон ответов для всех вопросов
      answers.append(self.createAnswers(self.answer_text[0]))
      answer_role.append(self.createAnswers(self.answer_role[0]))
    else:
      #для каждого вопроса разные варианты ответа
      for l in self.answer_text:
        answers.append(self.createAnswers(l))
      for l in self.answer_role:
        answer_role.append(self.createAnswers(l))
    
    
    shortcuts=self.createAnswers(self.shortcuts)
    #Имеем список списков ответов ^_^

    #создаём кнопки: добавляем в окно, соединяем со слотом, настраиваем внешний вид, присваиваем имя объекта.
    self.buttons=[]
    for answ in answers[0]:
      self.buttons.append(QPushButton(answ,self))
      self.connect(self.buttons[-1],SIGNAL("clicked()"),self.hasAnswer)
      self.button_layout.addWidget(self.buttons[-1])
      self.buttons[-1].setDisabled(True)
      self.buttons[-1].hide()
      #номер объекта - его имя
      self.buttons[-1].setObjectName(str(len(self.buttons)-1))

    self.base_point_size=self.buttons[-1].font().pointSizeF()
    self.answer_role=answer_role
    self.answer_text=answers
    self.shortcuts=shortcuts
    
  def createAnswers(self,line):
    """Создаёт список ответов из строки

    Строка закодирована следующим образом:
    [ответ-1][ответ-2][ответ-3]...[ответ-n]
    Таким образом, сначала удаляем промежуточные скобки ][, затем - открывающиеся и закрывающиеся. Что осталось кидаем в список строк."""
    line=unicode(line)
    answers=splitfields(line,"][")
    pos=answers[0].find('[',0,len(answers[0]))+1
    answers[0]=answers[0][pos:len(answers[0])]

    pos=answers[-1].find(']',0,len(answers[-1]))
    answers[-1]=answers[-1][0:pos]
    
    
    #по идее, должен получиться список ответов без разделителей
    return answers

  def createTest(self,name,directory=""):
    """Creating test using config files from directory"""
    if self.created==True:
      return
      
    qdir=QDir()
    if len(directory.strip())!=0:
      directory+'/'
    directory='tests/'+directory
    if qdir.exists(directory+name)==False:
      return
    self.loadData(directory+name)
    self.setHelloText()
    self.prepareButtons()
    self.my_name=name
    self.created=True


  #when testing is in progress:
  def hasAnswer(self):
    """We has a new answer - let's save it!"""
    if self.CurrentQuestion>=len(self.answers):
      self.answers.append(0)
    button=int(self.sender().objectName())
    role=0
    if len(self.answer_role)<self.QuestionsCount:
      role=self.answer_role[0][button]
    else:
      role=self.answer_role[self.CurrentQuestion][button]

    self.answers[self.CurrentQuestion]=int(role)

    #Проверка конца тестирования
    if self.CurrentQuestion<self.QuestionsCount-1:
      self.CurrentQuestion+=1
    else:
      #checking button instead pressing
      for b in self.buttons:
        b.setChecked(False)
        b.setCheckable(False)
      self.buttons[button].setCheckable(True)
      self.buttons[button].setChecked(True)
      #multi-button apperance
      self.bt_multi.setText(QString.fromUtf8("Завершить тестирование"))
      self.bt_multi.show()
      self.bt_multi.setEnabled(True)
      #let's finish the test
      self.state="TEST_FINISHED"

    #Настройка кнопок "вперед-назад"
    if self.bt_prev.isEnabled()==False:
      self.bt_next.setDisabled(True)
    if self.CurrentQuestion>0:
      self.bt_prev.setEnabled(True)
    
    #Настройка горячих клавиш
    if len(self.shortcuts)!=0:
      for i in range(0,len(self.shortcuts)):
        self.buttons[i].setShortcut(QKeySequence(self.shortcuts[i]))

    self.displayQuestion()

  def displayQuestion(self):
    """displaying current question"""
    self.main_text.setHtml(self.questions[self.CurrentQuestion])

    #Если в каждом случае ответы разные - присваиваем кнопкам новые имена
    if len(self.answer_role)<self.QuestionsCount==False:
      for b in self.buttons:
        b.setText(self.answer_text[self.CurrentQuestion][int(b.objectName())])

    #индикатор прогресса
    self.progressBar.setValue(self.CurrentQuestion+1)


  #reimplementing inherited functions:
  def onNext(self):
    BasicTestWindow.onNext(self)
    self.displayQuestion()

  def onPrev(self):
    BasicTestWindow.onPrev(self)
    self.displayQuestion()

  def onNewTest(self):
    for b in self.buttons:
      b.show()
    BasicTestWindow.onNewTest(self)

  def onMulti(self):
    if self.state=="NEW_STARTED":
      #displayind answer buttons
      for b in self.buttons:
        b.show()
        b.setEnabled(True)
      #Настройка горячих клавиш
      if len(self.shortcuts)!=0:
        for i in range(0,len(self.shortcuts)):
          self.buttons[i].setShortcut(QKeySequence(self.shortcuts[i]))
      self.displayQuestion()
    if self.state=="TEST_FINISHED":
      for b in self.buttons:
        b.setChecked(False)
        b.setCheckable(False)
        b.setDisabled(True)
      result=self.calculate(self.answers)
      result_text=u''
      result_text+=self.showResult(result)
      self.main_text.setHtml(result_text)
      self.image=self.drawImage(result)
    BasicTestWindow.onMulti(self)
  #done


  def keyReleaseEvent(self,event):
    if event.matches(QKeySequence.ZoomIn):
      self.zoom+=0.1
    elif event.matches(QKeySequence.ZoomOut):
      self.zoom-=0.1
    self.main_text.setZoomFactor(self.zoom)

    all_buttons=self.buttons
    all_buttons+=self.bt_prev,self.bt_next,self.bt_multi

    for b in all_buttons:
      font=b.font()
      font.setPointSizeF(self.base_point_size*self.zoom)
      b.setFont(font)
  
  def setDescriptor(self,descr):
    self.descr=descr
    self.calculate=descr.calculate
    self.showResult=descr.createResultText
    self.drawImage=descr.createImage
    
  def setLogic(self,calc,shres,drimg):
    self.calculate=calc
    self.showResult=shres
    self.drawImage=drimg
    


if __name__ == "__main__":
  import sys
  app = QtGui.QApplication(sys.argv)
  window=TestWindow()
  window.createTest("test")
  window.show()
  sys.exit(app.exec_())

