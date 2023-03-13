import sys

from PyQt6.QtWidgets import QApplication, QMainWindow

from view.v_MainWindow import Ui_MainWindow
from controller.c_canvas import CCanvas

import math


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.show()

        self.__canvas = CCanvas(self.GVCanvas)
        self.__copies = 0
        self.SPOffset.setValue(0.5)
        self.SPGap.setValue(0.5)

        self.events()

    def events(self) -> None:
        self.SPCanvasX.valueChanged.connect(self.resize_canvas)
        self.SPCanvasY.valueChanged.connect(self.resize_canvas)
        self.SPCopyX.valueChanged.connect(self.reload)
        self.SPCopyY.valueChanged.connect(self.reload)
        self.SPGap.valueChanged.connect(self.reload)
        self.SPOffset.valueChanged.connect(self.reload)
        self.SPNCopies.valueChanged.connect(self.calculate_copies)

    def reload(self) -> None:
        self.__copies = self.__canvas.generate_print(self.SPCopyX.value(), self.SPCopyY.value(),
                                                     self.SPOffset.value(), self.SPGap.value())
        self.calculate_copies()

    def calculate_copies(self):
        if self.__copies > 0:
            num_sheet = math.ceil(self.SPNCopies.value() / self.__copies)
            self.LBSheet.setText(str(num_sheet))
            self.LBCopies.setText(str(num_sheet * self.__copies))
            self.LBCopies.setStyleSheet("color:")
            self.LBSheet.setStyleSheet("color:")
        else:
            self.LBSheet.setText("err")
            self.LBCopies.setText("err")
            self.LBCopies.setStyleSheet("color: red")
            self.LBSheet.setStyleSheet("color: red")

    def resize_canvas(self) -> None:
        self.__canvas.resize(self.SPCanvasX.value(), self.SPCanvasY.value())
        self.reload()


# ---- MAIN -----

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    app.exec()
