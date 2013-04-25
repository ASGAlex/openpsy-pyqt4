# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from copy import *
import visual 

class TestDescriptor:
  def __init__(self):
    self.cs=1
    self.rNames=[]
    self.rValues=[]
    self.rKeys=[]
    self.rDescr=''
    self.gDescr=''
    self.result=[]
    self.gNames=[]
    self.gRanges=[]
    self.gResult=[]
    self.iType=''
    self.img_wh=[640,480,10]
    self.h_max=0
    self.descr=[]
    self.image=QImage()
    self.r_to_use='primary'
    
  def setResultsDescription(self,descr):
    self.rDescr=descr
  
  def addResult(self,name,values,keys):
    self.rNames.append(name)#Добавляем имя в список имён
    self.rValues.append(values)#Добавляем список номеров в список
    self.rKeys.append(keys)#Добавляем список ключей в список
    self.result.append(0)#Добавляем 0 в список результатов
    self.gResult.append(0)
    self.descr.append([])
    
  def delResult(self,name):
    for i in range(0,len(self.rNames)):
      if name==self.rNames[i]:
        del(self.rNames[i])
        del(self.rValues[i])
        del(self.rKeys[i])
        del(self.result[i])
        del(self.gResult[i])
        del(self.descr[i])
        return
  
  def delResult(self,index):
    if index<len(self.rNames):
      del(self.rNames[index])
      del(self.rValues[index])
      del(self.rKeys[index])
      del(self.result[index])
      del(self.gResult[index])
      del(self.descr[index])
    
  def setGradeDescription(self,descr):
    self.gDescr=descr
  
  def addGradation(self,grade,g_range):
    self.gNames.append(grade)#Добавляем название градации в список
    self.gRanges.append(g_range)#Добавляем список диапазонов для каждого результата в список
    for i in range(0,len(self.descr)):
      self.descr[i].append(u'')
    #self.gResult.append(0)
    
  def delGradation(self,grade):
    for i in range(0,len(self.gNames)):
      if grade==self.gNames[i]:
        del(self.gNames[i])
        del(self.gRanges[i])
        for i in range(0,len(self.descr)):
          del(self.descr[i][-1])
        
        #del(self.gResult[i])
  
    
  def setImageType(self,i_type):
    if i_type=='graph': 
      self.iType=i_type
    elif i_type=='histro':
        self.iType=i_type
    else:
      self.iType='noimage'
  
  
  def setCalcSteps(self,steps):
    self.cs=steps
  
  def calculate(self,answers):
    """applying keys to answers and storing to results"""
    if len(self.rValues)==0 or len(answers)==0:
      return
    for ks in range(0,len(self.rKeys)):
      for k in range(0,len(self.rKeys[ks])):
        self.result[ks]=self.result[ks]+answers[self.rValues[ks][k]-1]*self.rKeys[ks][k]
    if self.cs==1:
      self.r_to_use='primary'
      return self.result
    elif self.cs==2:
      r=self.postprocess()
      return r
  
  
  def postprocess(self,data=[]):
    """Сравниваем каждый результат с его диапазонами, выбираем тот, в который он попадает и сохраняем его."""
    result=self.result
    if len(data)!=0:
      result=data
    self.gResult=[]
    for r in range(0,len(result)):
      for g in range(0,len(self.gRanges)):
        if result[r]>=self.gRanges[g][r][0] and  result[r]<=self.gRanges[g][r][1]:
          self.gResult.append(g+1)
          break
    self.r_to_use='secondary'
    return self.gResult
          
  def setImgSize(self,w,h,f=10):
    self.img_wh=[w,h,f]
  
  def setHistroMaximum(self,h_max):
    self.h_max=h_max
    
  def createImage(self,data=[]):
    result=[]
    if len(data)!=0:
      result=data
    elif self.r_to_use=='primary':
      result=self.result
    elif self.r_to_use=='secondary':
      result=self.gResult
    text_x=copy(self.rNames)
    text_x.append(self.rDescr)
    if self.iType=='graph':
      text_y=copy(self.gNames)
      text_y.append(self.gDescr)
      self.image=visual.makeGraph(result,self.img_wh,(text_x,text_y))
    elif self.iType=='histro':
      self.image=visual.makeHistro(result,self.img_wh,text_x,self.h_max,True)
    return self.image
      
  def createResultText(self,data1=[],data2=[]):
    result=self.result
    g_result=self.gResult
    if len(data1)!=0:
      result=data1
    if len(data2)!=0:
        g_result=data2
    text=u'<b>Результаты тестирования:</b><br><table border="1" cellpadding="0" cellspacing="0">'
    text+=u'<tr style="font-weight: bold; text-align: center;"><td>'+unicode(self.rDescr)+u'</td><td>Первичная оценка</td>'
    if self.cs==2:
      text+=u'<td>Вторичная оценка</td>'
    text+=u'<td colspan="2" rowspan="1">Интерпретация результатов</td></tr>'
    for i in range(0,len(result)):
      text+='<tr><td>'+self.rNames[i]+'</td>'
      text+='<td style="vertical-align: middle; text-align: center;">'+str(result[i])+'</td>'
      text+='<td style="vertical-align: middle; text-align: center;">'+str(g_result[i])+'</td>'
      text+='<td nowrap="true">'+self.gNames[g_result[i]-1]+'</td>'
      text+='<td>'+self.descr[i][g_result[i]-1]+'</td></tr>'
    
    text+='</table>'
    
    return text
  
  def addDescription(self,r_index,g_index,text):
    try:
      self.descr[r_index][g_index]=text
    except IndexError:
      print u'Указан некорректный индекс'
  