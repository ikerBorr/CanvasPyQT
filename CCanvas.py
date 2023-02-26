from PyQt6.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsRectItem
from PyQt6.QtCore import Qt


#--- MACROS ---#

MAX_WIDTH = 425
MAX_HEIGHT = 300
CANVAS_OFFSET = 10

#--------------#


class CCanvas:
    def __init__(self, canvas: QGraphicsView, width: int = MAX_WIDTH, height: int = MAX_HEIGHT) -> None:
        super().__init__()
        self.m_width = width
        self.m_height = height
        self.m_canvas = canvas
        self.m_scene = QGraphicsScene(0, 0, width, height)
        self.m_canvas.setScene(self.m_scene)
        self.m_canvas.setFixedSize(width + CANVAS_OFFSET, height + CANVAS_OFFSET)

    def createLine(self, length=1) -> None:
        rect = QGraphicsRectItem(0, 0, length, 5)
        rect.setPos(0, 0)
        self.m_scene.addItem(rect)
        self.m_canvas.setScene(self.m_scene)

