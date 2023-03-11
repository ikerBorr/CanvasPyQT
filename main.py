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
        self.PBTry.pressed.connect(self.reload)
    
    def reload(self):
        print("value:", self.SPCopyX.value())
        self.m_canvas.generatePrint(self.SPCopyX.value(), self.SPCopyY.value(), self.SPOffset.value(), self.SPGap.value())


app = QApplication(sys.argv)
w = MainWindow()
app.exec()