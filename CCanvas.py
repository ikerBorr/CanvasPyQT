from PyQt6.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsRectItem, QGraphicsLineItem
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QBrush, QPen

from PyQt6 import QtCore


#--- MACROS ---#

MAX_WIDTH = 425
MAX_HEIGHT = 300

CANVAS_OFFSET = 10

GEOMETRY_BACKGROUND_COLOR = QBrush(Qt.GlobalColor.gray)
GEOMETRY_BORDER_COLOR = QPen(Qt.GlobalColor.black)
GEOMETRY_BORDER_SIZE = 2

#--------------#


class CCanvas:
    def __init__(self, canvas: QGraphicsView, width: int = MAX_WIDTH, height: int = MAX_HEIGHT) -> None:

        super().__init__()
        self.m_width = width
        self.m_height = height
        self.m_canvas = canvas
        self.m_scene = QGraphicsScene(0, 0, width + CANVAS_OFFSET, height + CANVAS_OFFSET)

        margin = CANVAS_OFFSET + GEOMETRY_BORDER_SIZE
        self.m_canvas.setMaximumSize(QtCore.QSize(MAX_WIDTH + margin , MAX_HEIGHT + margin))
        
        # geometry = QGraphicsRectItem(CANVAS_OFFSET/2, CANVAS_OFFSET/2, width, height)
        # geometry.setBrush(GEOMETRY_BACKGROUND_COLOR)
        # pen = GEOMETRY_BORDER_COLOR
        # pen.setWidth(GEOMETRY_BORDER_SIZE)
        # geometry.setPen(pen)
        # self.m_scene.addItem(geometry)
        # self.m_canvas.setScene(self.m_scene)


    def resize(self, width: int, height: int) -> None:
        
        self.m_scene = QGraphicScene(0, 0, width, height)


    def generatePrint(self, width: int = 1, height: int = 1, offset: int = 1, gap: int = 1) -> None:
        
        nLinesH1 = (self.m_width + gap - offset) / (width + gap)
        nLinesV1 = (self.m_height + gap - offset) / (height + gap)
        nLinesH2 = (self.m_width + gap - offset) / (height + gap)
        nLinesV2 = (self.m_height + gap - offset) / (width + gap)

        if ((nLinesH1 * nLinesV1) < (nLinesH2 * nLinesV2)):
            tempWidth = height
            tempHeight = width
            nLinesH = int(nLinesH2 - 1)
            nLinesV = int(nLinesV2 - 1)
        else:
            tempWidth = width
            tempHeight = height
            nLinesH = int(nLinesH1 - 1) 
            nLinesV = int(nLinesV1 - 1)
        
        print("H: " + str(nLinesH))
        print("V: " + str(nLinesV))

        totalWidth = (nLinesH + 1) * tempWidth + nLinesH * gap + offset
        totalHeight = (nLinesV + 1) * tempHeight + nLinesV * gap + offset

        print("tW: " + str(totalWidth))
        print("tH: " + str(totalHeight))
        
        geometry = QGraphicsRectItem(CANVAS_OFFSET/2, CANVAS_OFFSET/2, self.m_width, self.m_height)
        geometry.setBrush(GEOMETRY_BACKGROUND_COLOR)
        pen = GEOMETRY_BORDER_COLOR
        pen.setWidth(GEOMETRY_BORDER_SIZE)
        geometry.setPen(pen)
        self.m_scene.addItem(geometry)

        orgX = (self.m_width - totalWidth) / 2
        orgY = (self.m_height - totalHeight) / 2

        off = 0
        border = QPen(Qt.GlobalColor.white)
        border.setWidth(gap)

        for i in range(nLinesH):
            off = (i+1) * tempWidth
            tempLine = QGraphicsLineItem(orgX + off, orgY, orgX + off, totalHeight + orgY)
            print("orgX: " + str(orgX) + "; off: " + str(off) + "; orgY: " + str(orgY) + "; totalHeight: " + str(totalHeight))
            print("X1: " + str(orgX + off) + "; Y1: " + str(orgY) + "; X2: " + str(orgX + off) + "; Y2: " + str(totalHeight + orgY)) 
            tempLine.setPen(border)
            self.m_scene.addItem(tempLine)
            print(i)

        self.m_canvas.setScene(self.m_scene) 