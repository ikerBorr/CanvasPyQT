import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsScene
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QFont

from view.v_MainWindow import Ui_MainWindow
from controller.c_canvas import CCanvas
from model import m_constants as const

import math


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.show()

        self.__canvas = CCanvas()
        self.__copies = 0
        self.__cv_width = 420
        self.__cv_height = 297

        scene_max_w = const.MAX_WIDTH + 2 * const.GEOMETRY_BORDER + const.CANVAS_OFFSET
        scene_max_h = const.MAX_HEIGHT + 2 * const.GEOMETRY_BORDER + const.CANVAS_OFFSET
        self.GVCanvas.setMaximumSize(QSize(scene_max_w + 2, scene_max_h + 2))
        self.GVCanvas.setMinimumSize(QSize(scene_max_w + 2, scene_max_h + 2))

        self.SPOffset.setValue(0.5)
        self.SPGap.setValue(0.5)
        self.GVCanvas.setScene(CCanvas.create_scene())

        self.__events()

    def __events(self) -> None:
        self.SPCanvasX.valueChanged.connect(self.__resize_canvas)
        self.SPCanvasY.valueChanged.connect(self.__resize_canvas)
        self.SPCopyX.valueChanged.connect(self.__reload)
        self.SPCopyY.valueChanged.connect(self.__reload)
        self.SPGap.valueChanged.connect(self.__reload)
        self.SPOffset.valueChanged.connect(self.__reload)
        self.SPNCopies.valueChanged.connect(self.__calculate_copies)

    def __reload(self) -> None:
        cp_width, cp_height = self.SPCopyX.value(), self.SPCopyY.value()
        offset, gap = self.SPOffset.value(), self.SPGap.value()

        scene = self.GVCanvas.scene()
        scene.clear()
        scene, self.__copies = self.__canvas.generate_print(scene, cp_width, cp_height, self.__cv_width, 
                                                            self.__cv_height, offset, gap)
        self.__calculate_copies()
        if self.__copies > 0:
            self.GVCanvas.setScene(scene)
        else:
            scene.clear()
            scene.addSimpleText("ERROR TAMAÑO INCORRECTO", QFont("Times", 22))
            self.GVCanvas.setScene(scene)

    def __calculate_copies(self):
        if self.__copies > 0:
            num_sheet = math.ceil(self.SPNCopies.value() / self.__copies)
            self.LBSheet.setText(str(num_sheet))
            self.LBCopies.setText(str(num_sheet * self.__copies))
            self.LBCopies.setStyleSheet("color:")
            self.LBSheet.setStyleSheet("color:")

            area_util = (self.SPCopyX.value() * self.SPCopyY.value() * self.__copies) / \
                        (self.SPCanvasX.value() * self.SPCanvasY.value())
            self.LBUtil.setText(str("{:.1f}".format(area_util * 100)) + "%")
        else:
            self.LBSheet.setText("err")
            self.LBCopies.setText("err")
            self.LBCopies.setStyleSheet("color: red")
            self.LBSheet.setStyleSheet("color: red")
            self.LBUtil.setText(str(0))

    def __resize_canvas(self) -> None:
        scene, cv_width, cv_height = self.__canvas.resize(self.SPCanvasX.value(), self.SPCanvasY.value())
        self.GVCanvas.setScene(scene)
        self.__cv_width = cv_width
        self.__cv_height = cv_height
        self.__reload()


# ---- MAIN -----

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    app.exec()
