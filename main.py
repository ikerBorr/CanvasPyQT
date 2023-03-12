import sys

from PyQt6.QtWidgets import QApplication, QMainWindow

from MainWindow import Ui_MainWindow
from CCanvas import CCanvas


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.show()

        self.__canvas = CCanvas(self.GVCanvas)
        self.PBTry.pressed.connect(self.reload)
        self.SPCanvasX.valueChanged.connect(self.resize_canvas)
        self.SPCanvasY.valueChanged.connect(self.resize_canvas)
    
    def reload(self) -> None:
        self.__canvas.generate_print(self.SPCopyX.value(), self.SPCopyY.value(),
                                     self.SPOffset.value(), self.SPGap.value())

    def resize_canvas(self) -> None:
        self.__canvas.resize(self.SPCanvasX.value(), self.SPCanvasY.value())


app = QApplication(sys.argv)
w = MainWindow()
app.exec()
