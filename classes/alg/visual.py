#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *

#size[0] - Ширина (X)
#size[1] - Высота (Y)
#size[2] - Размер шрифта
#
#text[0] - Подписи X
#text[1] - Подписи Y
#
#
def makeGraph(result,size,text):
  """Создание графика"""
  width=size[0]
  height=size[1]
  font=size[2]
  text_x=text[0]
  text_y=text[1]

  img=QImage(width,height,QImage.Format_RGB32)
  img.fill(0xffffff)
  painter=QPainter(img)
  painter.setFont(QFont(painter.font().family(),font))
  #Отступы
  metrics=QFontMetrics(painter.font())
  lens=[]
  for l in text_y:
    lens.append(len(l))

  for i in range(0,len(lens)):
    if lens[i]==max(lens):
      ident_left=metrics.width(text_y[i])+metrics.width(text_y[i])/5

  ident_right=metrics.width(text_x[-1])+metrics.width(text_x[-1])/5

  #Шаги и отступы снизу и сверху
  step_x=(width-ident_right-ident_left)/len(text_x)
  step_y=height/(len(text_y)+1)
  ident_bottom=step_y+font
  ident_top=step_y+font
  step_y=(height-ident_top-ident_bottom)/(len(text_y))
  #Оси
  axis_x=QLine(ident_left,height-ident_bottom,width-ident_right,height-ident_bottom)
  axis_y=QLine(ident_left,height-ident_bottom,ident_left,ident_top)

  #Черточки и подписи
  x_hyphen=[]
  hx_size=step_x/10
  hy_size=step_y/10
  text_x_pos=[]
  for i in range(0,len(text_x)):
    if i<len(text_x)-1:
      x_hyphen.append(QLine(ident_left+(i+1)*step_x,height-ident_bottom-hx_size,ident_left+(i+1)*step_x,height-ident_bottom))
    metrics=QFontMetrics(painter.font())
    if i==len(text_x)-1:
      text_x_pos.append(QPoint(ident_left+(i+1)*step_x,height-ident_bottom+font+hy_size*2))
      #text_x_pos.append(QRect(x,y,w,h))
    else:
      #text_x_pos.append(QPoint(ident_left+(i+1)*step_x-metrics.width(text_x[i])/2,height-ident_bottom+font+hy_size*2))
      text_x_pos.append(QRect(ident_left+(i+1)*step_x-step_x/2,height-ident_bottom+font+hy_size*2,step_x,ident_bottom-font-hy_size*2))


  y_hyphen=[]
  text_y_pos=[]
  for i in range(0,len(text_y)):
    if i<len(text_y)-1:
      y_hyphen.append(QLine(ident_left,height-ident_bottom-(i+1)*step_y,ident_left+hy_size,height-ident_bottom-(i+1)*step_y))
    metrics=QFontMetrics(painter.font())
    if i==len(text_y)-1:
      text_y_pos.append(QPoint(ident_left-metrics.width(text_y[i])/2,ident_top/2+font/2))
    else:
      text_y_pos.append(QPoint(ident_left-metrics.width(text_y[i])-hy_size,height-ident_bottom-(i+1)*step_y+font/2))

  #Точки графика
  graph_points=[]
  dot_line_x=[]
  dot_line_y=[]
  for i in range(0,len(result)):
    graph_points.append(QPoint(ident_left+step_x*(i+1),height-(ident_bottom+result[i]*step_y)))
    dot_line_x.append(QLine(QPoint(ident_left,graph_points[-1].y()),graph_points[-1]))
    dot_line_y.append(QLine(QPoint(graph_points[-1].x(),height-ident_bottom),graph_points[-1]))

  #Перья для рисования
  axis_pen=QPen(Qt.black)
  axis_pen.setWidth(4)

  dot_pen=QPen(Qt.black)
  dot_pen.setWidth(1)
  dot_pen.setStyle(Qt.DotLine)

  main_pen=QPen(Qt.black)
  main_pen.setWidth(2)

  point_pen=QPen(Qt.red)
  point_pen.setWidth(4)

  #Рисуем
  #Оси
  painter.setRenderHint(QPainter.Antialiasing)
  painter.setPen(axis_pen)
  painter.drawLine(axis_x)
  painter.drawLine(axis_y)
  #Черточки и подписи
  painter.setPen(main_pen)
  painter.drawLines(x_hyphen)
  painter.drawLines(y_hyphen)
  for i in range(0,len(text_x_pos)):
    if i==len(text_x_pos)-1:
      nf=QFont(painter.font())
      nf.setWeight(QFont.Bold)#bold
      painter.setFont(nf)
      painter.drawText(text_x_pos[i],text_x[i])
      nf.setWeight(QFont.Normal)#normal
      painter.setFont(nf)
    else:
      painter.drawText(text_x_pos[i],Qt.TextWordWrap,text_x[i])
  for i in range(0,len(text_y_pos)):
    if i==len(text_y_pos)-1:
      nf=QFont(painter.font())
      nf.setWeight(QFont.Bold)#bold
      painter.setFont(nf)
      painter.drawText(text_y_pos[i],text_y[i])
      nf.setWeight(QFont.Normal)#normal
      painter.setFont(nf)
    else:
      painter.drawText(text_y_pos[i],text_y[i])
  #График
  p=QPolygon(graph_points)
  painter.drawPolyline(p)
  #Пунктирные линии
  painter.setRenderHint(QPainter.Antialiasing,False)
  painter.setPen(dot_pen)
  painter.drawLines(dot_line_x)
  painter.drawLines(dot_line_y)
  #Точки графика
  painter.setRenderHint(QPainter.Antialiasing)
  painter.setPen(point_pen)
  painter.drawPoints(p)
  return img

def makeHistro(result,size,text,maximum=0,difcol=True):
  """Создание гистрограммы"""
  width=size[0]
  height=size[1]
  font=size[2]
  text_x=text

  img=QImage(width,height,QImage.Format_RGB32)
  img.fill(0xffffff)
  painter=QPainter(img)
  painter.setFont(QFont(painter.font().family(),font))

  step_x=(width)/(len(text_x)+1)
  step_y=height/(max(result))

  ident_left=ident_right=step_x/2
  ident_top=step_y+font*2
  ident_bottom=step_y+font*2

  step_x=(width-ident_left-ident_right)/(len(result))
  step_y=(height-ident_bottom-ident_top)/(max(result))
  rects=[]
  text_up=[]
  text_up_pos=[]
  text_down_pos=[]
  metrics=QFontMetrics(painter.font())
  for i in range(0,len(result)):
    rects.append(QRect(ident_left+i*step_x,height-(ident_bottom+result[i]*step_y),step_x,result[i]*step_y))
    text_up_pos.append(QPoint(ident_left+i*step_x+step_x/2-metrics.width(str(result[i]))/2,height-(ident_bottom+result[i]*step_y-font-font/2)))
    text_down_pos.append(QPoint(ident_left+i*step_x+step_x/2-metrics.width(text_x[i])/2,height-ident_bottom+1.5*font))
    text_up.append(str(result[i]))

  max_line=QLine()
  max_text=u'Максимум: '
  max_text_pos=QPoint()
  if maximum!=0:
    if maximum<max(result):
      maximum=max(result)
    max_line=QLine(ident_left,height-maximum*step_y-ident_bottom,width-ident_right,height-maximum*step_y-ident_bottom)
    max_text+=str(maximum)
    max_text_pos=QPoint(width/2-metrics.width(max_text)/2,height-maximum*step_y-font/2-ident_bottom)

  pen=QPen(Qt.black,2)
  brush1=QBrush(Qt.lightGray)
  brush2=QBrush(Qt.lightGray)
  if difcol==True:
    brush2=QBrush(Qt.gray)

  painter.setPen(pen)
  painter.setBrush(brush1)

  for i in range(0,len(rects)):
    if difcol==True:
      if i%2==0:#если чётное
        painter.setBrush(brush1)
      elif i%2!=0:
        painter.setBrush(brush2)
      painter.drawRect(rects[i])
    painter.drawText(text_down_pos[i],text_x[i])
    painter.drawText(text_up_pos[i],text_up[i])

  if difcol==False:
    painter.drawRects(rects)

  if maximum!=0:
    painter.drawLine(max_line)
    painter.drawText(max_text_pos,max_text)

  return img













