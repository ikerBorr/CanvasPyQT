from PyQt6.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsRectItem, QGraphicsLineItem
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QBrush, QPen

from PyQt6 import QtCore

import constants as const

class CCanvas:
    def __init__(self, canvas: QGraphicsView, width: int = const.MAX_WIDTH, height: int = const.MAX_HEIGHT) -> None:

        super().__init__()
        self.__width = width
        self.__height = height
        self.__canvas = canvas
        self.__brushGeometry = QBrush(Qt.GlobalColor.gray)
        self.__penGeometry = QPen(Qt.GlobalColor.black)
        self.__penGeometry.setWidth(const.GEOMETRY_BORDER)
        self.__penLine = QPen(Qt.GlobalColor.red)
        self.__penLine.setWidth(1)

        sceneMaxW = const.MAX_WIDTH + 2 * const.GEOMETRY_BORDER + const.CANVAS_OFFSET
        sceneMaxH = const.MAX_HEIGHT + 2 * const.GEOMETRY_BORDER + const.CANVAS_OFFSET
        self.__scene = QGraphicsScene(0, 0, sceneMaxW, sceneMaxH)
        self.__canvas.setMaximumSize(QtCore.QSize(sceneMaxW + 2, sceneMaxH + 2))

    def __printLine(self, x1: int, y1: int, x2: int, y2: int, pen: QPen = None) -> None:
        
        assert(x1 >= 0 and x2 <= self.__width and y1 >= 0 and y2 <= self.__height)

        tempLine = QGraphicsLineItem(x1 + const.LINE_ORG, y1 + const.LINE_ORG, x2 + const.LINE_ORG, y2 + const.LINE_ORG)
        tempLine.setPen(pen or self.__penLine)
        self.__scene.addItem(tempLine)


    def __printRect(self, x1: int, y1: int, x2: int, y2: int, pen: QPen = None, brush: QBrush = None) -> None:
        
        assert(x1 >= 0 and x2 <= self.__width and y1 >= 0 and y2 <= self.__height)

        geometry = QGraphicsRectItem(const.RECT_ORG, const.RECT_ORG, x2 + 2 * const.GEOMETRY_BORDER, y2 + 2 * const.GEOMETRY_BORDER)
        geometry.setPen(pen or self.__penGeometry)
        geometry.setBrush(brush or self.__brushGeometry)
        self.__scene.addItem(geometry)

        
    def resize(self, width: int, height: int) -> None:
        
        self.__scene = QGraphicsScene(0, 0, width, height)


    def generatePrint(self, width: int = 1, height: int = 1, offset: int = 1, gap: int = 0) -> None:
        
        assert(width >= 0 and height >= 0 and offset >= 0 and gap >= 0)

        self.__printRect(0, 0, 425, 300)
        self.__printLine(0, 0, 0, 300, self.__penLine)
        self.__printLine(425, 0, 425, 300, self.__penLine)
        self.__canvas.setScene(self.__scene)
