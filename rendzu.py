#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import random
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import pyqtSignal, Qt

class Game(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.IsGameOverFlag = False
        self.tboard = Board(self)
        self.setCentralWidget(self.tboard)

        self.statusbar = self.statusBar()

#       Задать размеры окна
#        self.setFixedSize(450, 450)
        self.resize(450, 450)
#       Задать положение окна
        self.center()
#       Задать текст в заголовке окна
        self.setWindowTitle('5 в ряд')
        self.show()
      
    def center(self):

        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2,
            (screen.height()-size.height())/2)

    def mouseReleaseEvent(self, e):
        if not(self.IsGameOverFlag):
#           Определить, внутри какой ячейки щелкнули мышкой
            CellX = int(e.x() / self.tboard.CellWidth)
            CellY = int(e.y() / self.tboard.CellHeight)
#           Записать, в какую ячейку поставили крестик
            if self.tboard.Cell[CellX][CellY] == Figure.NoFigure:
                self.tboard.Cell[CellX][CellY] = Figure.XFigure
                self.IsGameOver(Figure.XFigure)
#               Перерисовать доску с поставленными крестиками и ноликами
                self.tboard.update()
#               Сделать ответный ход
                if not(self.IsGameOverFlag):
                    self.MachineMove()

    def IsGameOver(self, fig):
        for x in range(self.tboard.CellCountX):
            for y in range(self.tboard.CellCountY):
                if x < self.tboard.CellCountX-4 and self.tboard.Cell[x][y] == fig and \
                   self.tboard.Cell[x+1][y] == fig and \
                   self.tboard.Cell[x+2][y] == fig and \
                   self.tboard.Cell[x+3][y] == fig and \
                   self.tboard.Cell[x+4][y] == fig: 
                       self.IsGameOverFlag = True
                       self.tboard.Cell[x][y] = fig + 2
                       self.tboard.Cell[x+1][y] = fig + 2
                       self.tboard.Cell[x+2][y] = fig + 2
                       self.tboard.Cell[x+3][y] = fig + 2
                       self.tboard.Cell[x+4][y] = fig + 2
                if x < self.tboard.CellCountX-4 and y < self.tboard.CellCountY-4 and self.tboard.Cell[x][y] == fig and \
                   self.tboard.Cell[x+1][y+1] == fig and \
                   self.tboard.Cell[x+2][y+2] == fig and \
                   self.tboard.Cell[x+3][y+3] == fig and \
                   self.tboard.Cell[x+4][y+4] == fig: 
                       self.IsGameOverFlag = True
                       self.tboard.Cell[x][y] = fig + 2
                       self.tboard.Cell[x+1][y+1] = fig + 2
                       self.tboard.Cell[x+2][y+2] = fig + 2
                       self.tboard.Cell[x+3][y+3] = fig + 2
                       self.tboard.Cell[x+4][y+4] = fig + 2
                if y < self.tboard.CellCountY-4 and self.tboard.Cell[x][y] == fig and \
                   self.tboard.Cell[x][y+1] == fig and \
                   self.tboard.Cell[x][y+2] == fig and \
                   self.tboard.Cell[x][y+3] == fig and \
                   self.tboard.Cell[x][y+4] == fig: 
                       self.IsGameOverFlag = True
                       self.tboard.Cell[x][y] = fig + 2
                       self.tboard.Cell[x][y+1] = fig + 2
                       self.tboard.Cell[x][y+2] = fig + 2
                       self.tboard.Cell[x][y+3] = fig + 2
                       self.tboard.Cell[x][y+4] = fig + 2
                if x < self.tboard.CellCountX-4 and y > 4 and self.tboard.Cell[x][y] == fig and \
                   self.tboard.Cell[x+1][y-1] == fig and \
                   self.tboard.Cell[x+2][y-2] == fig and \
                   self.tboard.Cell[x+3][y-3] == fig and \
                   self.tboard.Cell[x+4][y-4] == fig: 
                       self.IsGameOverFlag = True
                       self.tboard.Cell[x][y] = fig + 2
                       self.tboard.Cell[x+1][y-1] = fig + 2
                       self.tboard.Cell[x+2][y-2] = fig + 2
                       self.tboard.Cell[x+3][y-3] = fig + 2
                       self.tboard.Cell[x+4][y-4] = fig + 2
                   

    def MachineMove(self):

#       Для временной матрицы перебираем все ячейки, чтобы определить, куда ставить следующий нолик
#       Раз уж перебираем все поле, проверяем только следующие направления: -, \, |, /. 
        self.MaxWeight = 0
        for i in range(self.tboard.CellCountX):
            for j in range(self.tboard.CellCountY):
                self.CurrWeight = 0
#       Проверить, не является ли данная ячейка четвертым крестиком
#       по диагонали вверх-влево и при этом свободной
                if i > 3 and j > 3 and self.tboard.Cell[i][j] == Figure.NoFigure:
                    if self.tboard.Cell[i-1][j-1] == Figure.XFigure and \
                       self.tboard.Cell[i-2][j-2] == Figure.XFigure and \
                       self.tboard.Cell[i-3][j-3] == Figure.XFigure and \
                       self.tboard.Cell[i-4][j-4] != Figure.OFigure:
                           self.CurrWeight = 1000
                           if self.CurrWeight > self.MaxWeight:
                               self.MaxWeight = self.CurrWeight
                               CellX = i
                               CellY = j
#       Проверить, не является ли данная ячейка четвертым крестиком
#       по диагонали вверх-вправо и при этом свободной
                if i < (self.tboard.CellCountX - 4) and j > 3 and self.tboard.Cell[i][j] == Figure.NoFigure:
                    if self.tboard.Cell[i+1][j-1] == Figure.XFigure and \
                       self.tboard.Cell[i+2][j-2] == Figure.XFigure and \
                       self.tboard.Cell[i+3][j-3] == Figure.XFigure and \
                       self.tboard.Cell[i+4][j-4] != Figure.OFigure:
                           self.CurrWeight = 1000 + self.CurrWeight
                           if self.CurrWeight > self.MaxWeight:
                               self.MaxWeight = self.CurrWeight
                               CellX = i
                               CellY = j
#       Проверить, не является ли данная ячейка четвертым крестиком
#       по диагонали вниз-влево и при этом свободной
                if i > 3 and j < (self.tboard.CellCountY - 4) and self.tboard.Cell[i][j] == Figure.NoFigure:
                    if self.tboard.Cell[i-1][j+1] == Figure.XFigure and \
                       self.tboard.Cell[i-2][j+2] == Figure.XFigure and \
                       self.tboard.Cell[i-3][j+3] == Figure.XFigure and \
                       self.tboard.Cell[i-4][j+4] != Figure.OFigure:
                           self.CurrWeight = 1000 + self.CurrWeight
                           if self.CurrWeight > self.MaxWeight:
                               self.MaxWeight = self.CurrWeight
                               CellX = i
                               CellY = j
#       Проверить, не является ли данная ячейка четвертым крестиком
#       по диагонали вниз-вправо и при этом свободной
                if i < (self.tboard.CellCountX - 4) and j < (self.tboard.CellCountY - 4) and self.tboard.Cell[i][j] == Figure.NoFigure:
                    if self.tboard.Cell[i+1][j+1] == Figure.XFigure and \
                       self.tboard.Cell[i+2][j+2] == Figure.XFigure and \
                       self.tboard.Cell[i+3][j+3] == Figure.XFigure and \
                       self.tboard.Cell[i+4][j+4] != Figure.OFigure:
                           self.CurrWeight = 1000 + self.CurrWeight
                           if self.CurrWeight > self.MaxWeight:
                               self.MaxWeight = self.CurrWeight
                               CellX = i
                               CellY = j                               
                            

#        Если комбинации нет, ставим случайным образом                    
        if self.MaxWeight == 0:            
            CellX = random.randint(0, self.tboard.CellCountX-1)
            CellY = random.randint(0, self.tboard.CellCountY-1)
            while self.tboard.Cell[CellX][CellY] != Figure.NoFigure:
                CellX = random.randint(0, self.tboard.CellCountX-1)
                CellY = random.randint(0, self.tboard.CellCountY-1)
        self.tboard.Cell[CellX][CellY] = Figure.OFigure
        self.IsGameOver(Figure.OFigure)
#       Перерисовать доску с поставленными крестиками и ноликами
        self.tboard.update()            

        
class Board(QFrame):

#   Задать количество ячеек игрового поля по горизонтали и вертикали
    CellCountX = 15
    CellCountY = 15
    CellWidth = 0
    CellHeight = 0
    Cell = []
        
    def __init__(self, parent):
        super().__init__(parent)

        self.initBoard()

    def initBoard(self):

        self.clearBoard()

    def clearBoard(self):

#       Инициализировать массив ячеек игрового поля
        self.Cell = []
#       Заполнить игровую матрицу пустыми значениями
        for i in range(self.CellCountX):
            self.Cell.append([])
            for j in range(self.CellCountY):
                self.Cell[i].append(Figure.NoFigure)
        

    def paintEvent(self, e):

        self.paintboard()

    def paintboard(self):

#       Получить размеры игрового окна        
        width = self.width()
        height = self.height()
#       Вычислить размеры ячейки по размеру игрового окна и количеству ячеек
        self.CellWidth = width /self.CellCountX
        self.CellHeight = height / self.CellCountY

#       Нарисовать сетку игрового поля        
        Color = QColor(0xCCCCCC)
        pen = QPen(Color, 1, Qt.SolidLine)
        qp = QPainter()
        qp.begin(self)
        qp.setPen(pen)
        for i in range(self.CellCountX-1):
            qp.drawLine((i+1)*self.CellWidth, 0, (i+1)*self.CellWidth, height)
        for i in range(self.CellCountY):
            qp.drawLine(0, (i+1)*self.CellHeight, width, (i+1)*self.CellHeight)
        qp.end()
        
#       Перерисовать все фигуры на доске
        for i in range(self.CellCountX):
            for j in range(self.CellCountY):
               self.drawFigure(i+1,j+1, self.Cell[i][j])

        
#       Нарисовать крестик или нолик
    def drawFigure(self, x, y, shape):
        if shape == Figure.NoFigure:
            return
#       Задать масштаб фигуры по отношению к ячейке
        k = 0.5

#       Задать цвет фигуры в зависимости от фигуры        
        if shape == Figure.XFigure:
            Color = QColor(0x0000CC)
        elif shape == Figure.OFigure:
            Color = QColor(0xCC0000)
        elif shape == Figure.WinX or shape == Figure.WinO:
            Color = QColor(0x00CC00)

#       Нарисовать объект
        pen = QPen(Color, 3, Qt.SolidLine)
        qp = QPainter()
        qp.begin(self)
        qp.setPen(pen)
        if shape == Figure.OFigure or shape == Figure.WinO:
            qp.drawEllipse((x-1)*self.CellWidth + (1-k)/2*self.CellWidth, (y-1)*self.CellHeight + (1-k)/2*self.CellHeight, self.CellWidth*k, self.CellHeight*k)
        elif shape == Figure.XFigure or shape == Figure.WinX:
            qp.drawLine((x-1)*self.CellWidth + (1-k)/2*self.CellWidth, (y-1)*self.CellHeight + (1-k)/2*self.CellHeight, x*self.CellWidth - (1-k)/2*self.CellWidth, (y)*self.CellHeight - (1-k)/2*self.CellHeight)
            qp.drawLine(x*self.CellWidth - (1-k)/2*self.CellWidth, (y-1)*self.CellHeight + (1-k)/2*self.CellHeight, (x-1)*self.CellWidth + (1-k)/2*self.CellWidth,  (y)*self.CellHeight - (1-k)/2*self.CellHeight)
        qp.end()

        
class Figure(object):

        NoFigure = 0
        XFigure = 1
        OFigure = 2
        WinX = 3
        WinO = 4


if __name__ == '__main__':

    app = QApplication([])
    game = Game()
    sys.exit(app.exec_())
