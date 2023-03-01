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
        self.__scene = QGraphicsScene(0, 0, width + CANVAS_OFFSET, height + CANVAS_OFFSET)
        self.__brushGeometry = QBrush(Qt.GlobalColor.gray)
        self.__penGeometry = QPen(Qt.GlobalColor.black)
        self.__penGeometry.setWidth(GEOMETRY_BORDER_SIZE)
        self.__penLine = QPen(Qt.GlobalColor.white)
        self.__penLine.setWidth(1)
        margin = CANVAS_OFFSET + 2 * GEOMETRY_BORDER_SIZE
        self.__canvas.setMaximumSize(QtCore.QSize(MAX_WIDTH + margin , MAX_HEIGHT + margin))


    def __printLine(self, x1: int, y1: int, x2: int, y2: int, pen: QPen = None) -> None:
        
        assert(x1 >= 0 and x2 <= self.__width and y1 >= 0 and y2 <= self.__height)
       
        off = int((GEOMETRY_BORDER_SIZE + CANVAS_OFFSET) / 2)

        tempLine = QGraphicsLineItem(off + x1, off + y1, off + x2, off + y2)
        tempLine.setPen(pen or self.__penLine)
        self.__scene.addItem(tempLine)


    def __printRect(self, x1: int, y1: int, x2: int, y2: int, pen: QPen = None, brush: QBrush = None) -> None:
        
        assert(x1 >= 0 and x2 <= self.__width and y1 >= 0 and y2 <= self.__height)

        offset  = int((GEOMETRY_BORDER_SIZE + CANVAS_OFFSET) / 2)

        geometry = QGraphicsRectItem( offset + x1, offset + y1, x2, y2)
        geometry.setPen(pen or self.__penGeometry)
        geometry.setBrush(brush or self.__brushGeometry)
        self.__scene.addItem(geometry)

        
    def resize(self, width: int, height: int) -> None:
        
        self.__scene = QGraphicsScene(0, 0, width, height)


    def generatePrint(self, width: int = 1, height: int = 1, offset: int = 1, gap: int = 0) -> None:
        
        assert(width >= 0 and height >= 0 and offset >= 0 and gap >= 0)

        nLinesH1 = int((self.__width - width - 2 * offset) / (width + gap))
        nLinesV1 = int((self.__height - height - 2 * offset) / (height + gap))
        nLinesH2 = int((self.__width - width - 2 * offset) / (height + gap))
        nLinesV2 = int((self.__height - height - 2 * offset) / (width+ gap))

        if ((nLinesH1 * nLinesV1) < (nLinesH2 * nLinesV2)):
            tempWidth = height
            tempHeight = width
            nLinesH = nLinesH2
            nLinesV = nLinesV2
        else:
            tempWidth = width
            tempHeight = height
            nLinesH = nLinesH1
            nLinesV = nLinesV1

        self.__printRect(0, 0, self.__width, self.__height)
        
        totalWidth = (nLinesH + 1) * tempWidth + nLinesH * gap + 2 * offset
        totalHeight = (nLinesV + 1) * tempHeight + nLinesV * gap + 2 * offset

        orgX = int((self.__width - totalWidth) / 2) + offset
        orgY = int((self.__height - totalHeight) / 2) + offset

        print("orgX: ", orgX)
        print("orgY: ", orgY)

        off = 0
        self.__penLine.setWidth(gap)

        for i in range(nLinesH + 2):
            off = i * (tempWidth + gap)
            self.__printLine(orgX + off, orgY, orgX + off, totalHeight + orgY - 2 * offset)

        self.__canvas.setScene(self.__scene) 