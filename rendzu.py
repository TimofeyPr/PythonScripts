#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import pyqtSignal, Qt

class Game(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

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
#       Определить, внутри какой ячейки щелкнули мышкой
        CellX = int(e.x() / self.tboard.CellWidth)
        CellY = int(e.y() / self.tboard.CellHeight)
#       Записать, в какую ячейку поставили крестик
        self.tboard.Cell[CellX][CellY] = Figure.XFigure
#       Нарисовать крестик на доске
#        self.tboard.drawFigure(CellX, CellY, Figure.XFigure)
#        print(CellX, CellY, Figure.XFigure)
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

#        mainWindow = QMainWindow()

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

#       Нарисовать объект
        pen = QPen(Color, 3, Qt.SolidLine)
        qp = QPainter()
        qp.begin(self)
        
        qp.setPen(pen)
        if shape == Figure.OFigure:
            qp.drawEllipse((x-1)*self.CellWidth + (1-k)/2*self.CellWidth, (y-1)*self.CellHeight + (1-k)/2*self.CellHeight, self.CellWidth*k, self.CellHeight*k)
        elif shape == Figure.XFigure:
            qp.drawLine((x-1)*self.CellWidth + (1-k)/2*self.CellWidth, (y-1)*self.CellHeight + (1-k)/2*self.CellHeight, x*self.CellWidth - (1-k)/2*self.CellWidth, (y)*self.CellHeight - (1-k)/2*self.CellHeight)
            qp.drawLine(x*self.CellWidth - (1-k)/2*self.CellWidth, (y-1)*self.CellHeight + (1-k)/2*self.CellHeight, (x-1)*self.CellWidth + (1-k)/2*self.CellWidth,  (y)*self.CellHeight - (1-k)/2*self.CellHeight)
        qp.end()

        
class Figure(object):

        NoFigure = 0
        XFigure = 2
        OFigure = 1


if __name__ == '__main__':

    app = QApplication([])
    game = Game()
    sys.exit(app.exec_())
