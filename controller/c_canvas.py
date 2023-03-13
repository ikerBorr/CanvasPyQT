import math

from PyQt6.QtWidgets import QGraphicsScene
from PyQt6.QtCore import Qt, QRectF, QLineF
from PyQt6.QtGui import QBrush, QPen

from model import m_constants as const


class CCanvas:

    def __init__(self) -> None:

        super().__init__()

        self.__constSize = const.MM_PX_CONSTANT
        self.__brushGeometry = QBrush(Qt.GlobalColor.gray)
        self.__penGeometry = QPen(Qt.GlobalColor.black)
        self.__penGeometry.setWidth(const.GEOMETRY_BORDER)
        self.__penLine = QPen(Qt.GlobalColor.white)
        self.__penLine.setWidth(1)

    def __print_line(self, scene: QGraphicsScene, x1: int, y1: int, x2: int, y2: int, gap: float = 1) -> None:

        self.__penLine.setWidth(int(gap))
        line = QLineF(x1 + const.LINE_ORG, y1 + const.LINE_ORG, x2 + const.LINE_ORG, y2 + const.LINE_ORG)
        scene.addLine(line, self.__penLine)

    def __print_rect(self, scene: QGraphicsScene, x1: int, y1: int, x2: int, y2: int,
                     brush: QBrush = None, pen: QPen = None) -> None:

        rect = QRectF(x1 + const.RECT_ORG, y1 + const.RECT_ORG, x2, y2)
        scene.addRect(rect, pen or self.__penGeometry, brush or self.__brushGeometry)

    @staticmethod
    def __optimise_place(cv_w: float, cv_h: float, w: float, h: float, gap: int = 1,
                         offset: int = 1) -> [int, int, int, int]:

        aux = gap - 2 * offset
        nw1 = int((cv_w + aux) / (w + gap))
        nh1 = int((cv_h + aux) / (h + gap))
        nw2 = int((cv_h + aux) / (w + gap))
        nh2 = int((cv_w + aux) / (h + gap))

        if (nw1 * nh1) > (nw2 * nh2):
            return w, h, nw1, nh1
        else:
            return h, w, nh2, nw2

    @staticmethod
    def create_scene():
        return QGraphicsScene(0, 0, const.SCENE_MAX_WIDTH, const.SCENE_MAX_HEIGHT)

    def cm_to_px(self, x: float) -> float:
        ret = int(x * self.__constSize)
        if ret == 0:
            return 1
        else:
            return x * self.__constSize

    def resize(self, width: float, height: float) -> [QGraphicsScene, int, int]:

        if height > width:
            width, height = height, width

        c1 = const.MAX_WIDTH / width
        c2 = const.MAX_HEIGHT / height
        if c1 > c2:
            width, height = width * c2, height * c2
            self.__constSize = c2
        else:
            width, height = width * c1, height * c1
            self.__constSize = c1

        scene_max_w = width + 2 * const.GEOMETRY_BORDER + const.CANVAS_OFFSET
        scene_max_h = height + 2 * const.GEOMETRY_BORDER + const.CANVAS_OFFSET
        scene = QGraphicsScene(0, 0, scene_max_w, scene_max_h)

        return scene, width, height

    def generate_print(self, scene: QGraphicsScene, cp_width: float, cp_height: float, cv_width: float,
                       cv_height: float, offset: float, gap: float) -> [QGraphicsScene, int]:

        gap, offset = self.cm_to_px(gap), self.cm_to_px(offset)

        self.__print_rect(scene, 0, 0, math.ceil(cv_width), math.ceil(cv_height), QBrush(Qt.GlobalColor.white))

        width, height, n_vert, n_hort = self.__optimise_place(cv_width, cv_height, self.cm_to_px(cp_width),
                                                              self.cm_to_px(cp_height), int(gap), int(offset))

        offset_v = int((cv_width - int(width * n_vert + gap * (n_vert - 1))) / 2)
        offset_h = int((cv_height - int(height * n_hort + gap * (n_hort - 1))) / 2)

        org_x = int(offset_v + width + gap / 2)
        end_x = int(cv_width) - offset_v
        orgy = int(offset_h + height + gap / 2)
        end_y = int(cv_height) - offset_h

        self.__print_rect(scene, offset_v, offset_h, end_x - offset_v, end_y - offset_h)

        self.__print_line(scene, offset_v, offset_h, offset_v, end_y, 2)
        for i in range(n_vert - 1):
            self.__print_line(scene, org_x, int(offset_h + gap / 2), org_x, int(end_y - gap / 2), gap)
            org_x = org_x + width + gap
        self.__print_line(scene, end_x, offset_h, end_x, end_y, 2)

        self.__print_line(scene, offset_v, offset_h, end_x, offset_h, 2)
        for i in range(n_hort - 1):
            self.__print_line(scene, int(offset_v + gap / 2), orgy, int(end_x - gap / 2), orgy, gap)
            orgy = orgy + height + gap
        self.__print_line(scene, offset_v, end_y, end_x, end_y, 2)

        return scene, n_vert * n_hort
