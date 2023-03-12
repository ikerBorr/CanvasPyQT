from PyQt6.QtWidgets import QGraphicsView, QGraphicsScene
from PyQt6.QtCore import Qt, QRectF, QLineF
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
        self.__penLine = QPen(Qt.GlobalColor.white)
        self.__penLine.setWidth(1)

        scene_max_w = const.MAX_WIDTH + 2 * const.GEOMETRY_BORDER + const.CANVAS_OFFSET
        scene_max_h = const.MAX_HEIGHT + 2 * const.GEOMETRY_BORDER + const.CANVAS_OFFSET
        self.__scene = QGraphicsScene(0, 0, scene_max_w, scene_max_h)
        self.__canvas.setMaximumSize(QtCore.QSize(scene_max_w + 2, scene_max_h + 2))

    def __print_line(self, x1: int, y1: int, x2: int, y2: int, gap: int = 1) -> None:
        
        assert(x1 >= 0 and x2 <= self.__width and y1 >= 0 and y2 <= self.__height)

        self.__penLine.setWidth(gap)
        line = QLineF(x1 + const.LINE_ORG, y1 + const.LINE_ORG, x2 + const.LINE_ORG, y2 + const.LINE_ORG)
        self.__scene.addLine(line, self.__penLine)

    def __print_rect(self, x1: int, y1: int, x2: int, y2: int, brush: QBrush = None, pen: QPen = None,) -> None:
        
        assert(x1 >= 0 and x2 <= self.__width and y1 >= 0 and y2 <= self.__height)

        rect = QRectF(x1 + const.RECT_ORG, y1 + const.RECT_ORG, x2, y2)
        self.__scene.addRect(rect, pen or self.__penGeometry, brush or self.__brushGeometry)

    def __optime_place(self, w: int, h: int, gap: int = 1, offset: int = 1) -> [int, int, int, int]:

        aux = gap - 2 * offset
        nw1 = int((self.__width + aux) / (w + gap))
        nh1 = int((self.__height + aux) / (h + gap))
        nw2 = int((self.__height + aux) / (w + gap))
        nh2 = int((self.__width + aux) / (h + gap))

        if nw1 * nh1 > nw2 * nh2:
            return w, h, nw1, nh1
        else:
            return h, w, nh2, nw2

    def resize(self, width, height) -> None:

        if height > width:
            width, height = height, width

        a1 = const.MAX_WIDTH / width
        a2 = const.MAX_HEIGHT / height
        if a1 > a2:
            width, height = width * a2, height * a2
        else:
            width, height = width * a1, height * a1

        self.__width = int(width)
        self.__height = int(height)
        scene_max_w = width+ 2 * const.GEOMETRY_BORDER + const.CANVAS_OFFSET
        scene_max_h = height + 2 * const.GEOMETRY_BORDER + const.CANVAS_OFFSET
        self.__scene = QGraphicsScene(0, 0, scene_max_w, scene_max_h)

        scene_max_w = width + 2 * const.GEOMETRY_BORDER + const.CANVAS_OFFSET
        scene_max_h = height + 2 * const.GEOMETRY_BORDER + const.CANVAS_OFFSET
        self.__scene = QGraphicsScene(0, 0, scene_max_w, scene_max_h)
        self.__canvas.setScene(self.__scene)
        # self.__canvas.setMaximumSize(QtCore.QSize(scene_max_w + 2, scene_max_h + 2))

    def generate_print(self, width: int = 1, height: int = 1, offset: int = 1, gap: int = 1) -> None:
        
        assert(width >= 0 and height >= 0 and offset > 0 and gap > 0)

        self.__print_rect(0, 0, self.__width, self.__height, QBrush(Qt.GlobalColor.white))

        width, height, n_vert, n_hort = self.__optime_place(width, height, gap, offset)

        offset_v = int((self.__width - int(width * n_vert + gap * (n_vert - 1))) / 2)
        offset_h = int((self.__height - int(height * n_hort + gap * (n_hort - 1))) / 2)

        org_x = int(offset_v + width + gap / 2)
        end_x = self.__width - offset_v
        orgy = int(offset_h + height + gap / 2)
        end_y = self.__height - offset_h

        self.__print_rect(offset_v, offset_h, end_x - offset_v, end_y - offset_h)

        self.__print_line(offset_v, offset_h, offset_v, end_y, 2)
        for i in range(n_vert - 1):
            self.__print_line(org_x, int(offset_h + gap / 2), org_x, int(end_y - gap / 2), gap)
            org_x = org_x + width + gap
        self.__print_line(end_x, offset_h, end_x, end_y, 2)

        self.__print_line(offset_v, offset_h, end_x, offset_h, 2)
        for i in range(n_hort - 1):
            self.__print_line(int(offset_v + gap / 2), orgy, int(end_x - gap / 2), orgy, gap)
            orgy = orgy + height + gap
        self.__print_line(offset_v, end_y, end_x, end_y, 2)

        self.__canvas.setScene(self.__scene)
