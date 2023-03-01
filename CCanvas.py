from PyQt6.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsRectItem, QGraphicsLineItem
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QBrush, QPen

from PyQt6 import QtCore


#--- MACROS ---#

MAX_WIDTH = 425
MAX_HEIGHT = 300
CANVAS_OFFSET = 10
GEOMETRY_BORDER_SIZE = 2

#--------------#


class CCanvas:
    def __init__(self, canvas: QGraphicsView, width: int = MAX_WIDTH, height: int = MAX_HEIGHT) -> None:

        super().__init__()
        self.__width = width
        self.__height = height
        self.__canvas = canvas
        #self.__scene = QGraphicsScene(0, 0, width + CANVAS_OFFSET, height + CANVAS_OFFSET)
        self.__scene = QGraphicsScene(0, 0, 439, 314)
        self.__brushGeometry = QBrush(Qt.GlobalColor.gray)
        self.__penGeometry = QPen(Qt.GlobalColor.black)
        self.__penGeometry.setWidth(GEOMETRY_BORDER_SIZE)
        self.__penLine = QPen(Qt.GlobalColor.white)
        self.__penLine.setWidth(1)
        margin = CANVAS_OFFSET + 2 * GEOMETRY_BORDER_SIZE
        #self.__canvas.setMaximumSize(QtCore.QSize(MAX_WIDTH + margin , MAX_HEIGHT + margin))
        self.__canvas.setMaximumSize(QtCore.QSize(MAX_WIDTH + margin + 10, MAX_HEIGHT + margin + 10))


    def __printLine(self, x1: int, y1: int, x2: int, y2: int, pen: QPen = None) -> None:
        
        assert(x1 >= 0 and x2 <= self.__width and y1 >= 0 and y2 <= self.__height)
       
        offset = int(GEOMETRY_BORDER_SIZE + CANVAS_OFFSET / 2)

        tempLine = QGraphicsLineItem(x1 + offset, y1 + offset, x2 + offset, y2 + offset)
        tempLine.setPen(pen or self.__penLine)
        self.__scene.addItem(tempLine)


    def __printRect(self, x1: int, y1: int, x2: int, y2: int, pen: QPen = None, brush: QBrush = None) -> None:
        
        assert(x1 >= 0 and x2 <= self.__width and y1 >= 0 and y2 <= self.__height)

        offset = int(CANVAS_OFFSET / 2)

        #geometry = QGraphicsRectItem(x1 + offset, y1 + offset, x2 + offset + 2 * GEOMETRY_BORDER_SIZE , y2 + offset + 2 * GEOMETRY_BORDER_SIZE)
        geometry = QGraphicsRectItem(5, 5, 434 , 309)
        print("offset: ", offset)
        print("x1: ", x1 + offset, " y1: ", y1 + offset, " x2: ", x2 + offset + 2 * GEOMETRY_BORDER_SIZE, " y2: ", y2 + offset + 2 * GEOMETRY_BORDER_SIZE)
        geometry.setPen(pen or self.__penGeometry)
        geometry.setBrush(brush or self.__brushGeometry)
        self.__scene.addItem(geometry)
        #offset  = int(GEOMETRY_BORDER_SIZE + CANVAS_OFFSET / 2)

        #geometry = QGraphicsRectItem( offset + x1, offset + y1, x2, y2)
        #geometry.setPen(pen or self.__penGeometry)
        #geometry.setBrush(brush or self.__brushGeometry)
        #self.__scene.addItem(geometry)

        
    def resize(self, width: int, height: int) -> None:
        
        self.__scene = QGraphicsScene(0, 0, width, height)


    def generatePrint(self, width: int = 1, height: int = 1, offset: int = 1, gap: int = 0) -> None:
        
        assert(width >= 0 and height >= 0 and offset >= 0 and gap >= 0)

        self.__printRect(0,0,425,300)

        tempPen = QPen(Qt.GlobalColor.red)
        self.__printLine(0, 0, 0, 300, tempPen)
        self.__printLine(425, 0, 425, 300, tempPen)

        self.__canvas.setScene(self.__scene) 