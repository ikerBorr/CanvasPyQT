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
        self.SPCanvasX.valueChanged.connect(self.resize_canvas)
        self.SPCanvasY.valueChanged.connect(self.resize_canvas)
        self.SPCopyX.valueChanged.connect(self.reload)
        self.SPCopyY.valueChanged.connect(self.reload)
        self.SPGap.valueChanged.connect(self.reload)
        self.SPOffset.valueChanged.connect(self.reload)
    
    def reload(self) -> None:
        self.__canvas.generate_print(self.SPCopyX.value(), self.SPCopyY.value(),
                                     self.SPOffset.value(), self.SPGap.value())

    def resize_canvas(self) -> None:
        self.__canvas.resize(self.SPCanvasX.value(), self.SPCanvasY.value())
        self.reload()


app = QApplication(sys.argv)
w = MainWindow()
app.exec()
