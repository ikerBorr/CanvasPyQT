import sys

from PyQt6.QtCore import Qt 
from PyQt6.QtWidgets import QApplication, QMainWindow

from MainWindow import Ui_MainWindow
from CCanvas import CCanvas

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.show()

        self.m_canvas = CCanvas(self.GVCanvas)
        self.m_canvas.createLine(100)


app = QApplication(sys.argv)
w = MainWindow()
app.exec()