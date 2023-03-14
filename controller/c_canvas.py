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

    def __print_line(self, scene: QGraphicsScene, p1: list, p2: list, gap: float = 1) -> None:

        assert(len(p1) == 2 and len(p2) == 2)

        self.__penLine.setWidth(int(gap))
        line = QLineF(p1[0] + const.LINE_ORG, p1[1] + const.LINE_ORG, p2[0] + const.LINE_ORG, p2[1] + const.LINE_ORG)
        scene.addLine(line, self.__penLine)

    def __print_rect(self, scene: QGraphicsScene, p1: list, p2: list, brush: QBrush = None, pen: QPen = None) -> None:

        rect = QRectF(p1[0] + const.RECT_ORG, p1[1] + const.RECT_ORG, p2[0], p2[1])
        scene.addRect(rect, pen or self.__penGeometry, brush or self.__brushGeometry)

    @staticmethod
    def __optimise_place(sheet: list, copy: list, gap: int = 1, offset: int = 1) -> (int, int, int, int):

        assert(len(sheet) == 2 and len(copy) == 2)

        aux = gap - 2 * offset
        nw1 = int((sheet[0] + aux) / (copy[0] + gap))
        nh1 = int((sheet[1] + aux) / (copy[1] + gap))
        nw2 = int((sheet[1] + aux) / (copy[0] + gap))
        nh2 = int((sheet[0] + aux) / (copy[1] + gap))

        if (nw1 * nh1) < (nw2 * nh2):
            copy = copy[1], copy[0]
            nw1, nh1 = nh2, nw2

        return copy[0], copy[1], nw1, nh1

    @staticmethod
    def create_scene() -> QGraphicsScene:
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

    def generate_print(self, scene: QGraphicsScene, copy: list, sheet: list, offset: float, gap: float) -> tuple:

        assert(len(copy) == 2 and len(sheet) == 2)

        self.__print_rect(scene, [0, 0], [math.ceil(sheet[0]), math.ceil(sheet[1])], QBrush(Qt.GlobalColor.white))

        gap, offset = self.cm_to_px(gap), int(self.cm_to_px(offset))
        copy = [self.cm_to_px(copy[0]), self.cm_to_px(copy[1])]
        width, height, n_vert, n_hort = self.__optimise_place(sheet, copy, int(gap), offset)

        offset_v = int((sheet[0] - int(width * n_vert + gap * (n_vert - 1))) / 2)
        offset_h = int((sheet[1] - int(height * n_hort + gap * (n_hort - 1))) / 2)

        org_x = int(offset_v + width + gap / 2)
        end_x = int(sheet[0]) - offset_v
        orgy = int(offset_h + height + gap / 2)
        end_y = int(sheet[1]) - offset_h

        self.__print_rect(scene, [offset_v, offset_h], [end_x - offset_v, end_y - offset_h])

        self.__print_line(scene, [offset_v, offset_h], [offset_v, end_y], 2)
        for i in range(n_vert - 1):
            self.__print_line(scene, [org_x, int(offset_h + gap / 2)], [org_x, int(end_y - gap / 2)], gap)
            org_x = org_x + width + gap
        self.__print_line(scene, [end_x, offset_h], [end_x, end_y], 2)

        self.__print_line(scene, [offset_v, offset_h], [end_x, offset_h], 2)
        for i in range(n_hort - 1):
            self.__print_line(scene, [int(offset_v + gap / 2), orgy], [int(end_x - gap / 2), orgy], gap)
            orgy = orgy + height + gap
        self.__print_line(scene, [offset_v, end_y], [end_x, end_y], 2)

        return scene, n_vert * n_hort
