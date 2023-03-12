# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(547, 568)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.GVCanvas = QtWidgets.QGraphicsView(parent=self.centralwidget)
        self.GVCanvas.setMinimumSize(QtCore.QSize(439, 314))
        self.GVCanvas.setMaximumSize(QtCore.QSize(439, 314))
        self.GVCanvas.setStyleSheet("background: white;")
        self.GVCanvas.setObjectName("GVCanvas")
        self.horizontalLayout_4.addWidget(self.GVCanvas)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_6.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.SPCanvasX = QtWidgets.QDoubleSpinBox(parent=self.frame)
        self.SPCanvasX.setDecimals(1)
        self.SPCanvasX.setMinimum(1.0)
        self.SPCanvasX.setMaximum(1000.0)
        self.SPCanvasX.setProperty("value", 42.0)
        self.SPCanvasX.setObjectName("SPCanvasX")
        self.verticalLayout_2.addWidget(self.SPCanvasX)
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.SPCanvasY = QtWidgets.QDoubleSpinBox(parent=self.frame)
        self.SPCanvasY.setDecimals(1)
        self.SPCanvasY.setMinimum(1.0)
        self.SPCanvasY.setMaximum(1000.0)
        self.SPCanvasY.setProperty("value", 29.7)
        self.SPCanvasY.setObjectName("SPCanvasY")
        self.verticalLayout_2.addWidget(self.SPCanvasY)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_3 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_8.addWidget(self.label_3)
        self.SPCopyX = QtWidgets.QDoubleSpinBox(parent=self.frame_2)
        self.SPCopyX.setDecimals(1)
        self.SPCopyX.setMaximum(1000.0)
        self.SPCopyX.setObjectName("SPCopyX")
        self.verticalLayout_8.addWidget(self.SPCopyX)
        self.label_4 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_8.addWidget(self.label_4)
        self.SPCopyY = QtWidgets.QDoubleSpinBox(parent=self.frame_2)
        self.SPCopyY.setDecimals(1)
        self.SPCopyY.setMaximum(1000.0)
        self.SPCopyY.setObjectName("SPCopyY")
        self.verticalLayout_8.addWidget(self.SPCopyY)
        self.horizontalLayout.addWidget(self.frame_2)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.SPNCopies = QtWidgets.QSpinBox(parent=self.frame_3)
        self.SPNCopies.setMinimum(1)
        self.SPNCopies.setMaximum(1000)
        self.SPNCopies.setProperty("value", 1)
        self.SPNCopies.setObjectName("SPNCopies")
        self.verticalLayout.addWidget(self.SPNCopies)
        self.horizontalLayout_3.addWidget(self.frame_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_4 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_6 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.SPOffset = QtWidgets.QDoubleSpinBox(parent=self.frame_4)
        self.SPOffset.setDecimals(1)
        self.SPOffset.setMinimum(0.1)
        self.SPOffset.setSingleStep(1.0)
        self.SPOffset.setStepType(QtWidgets.QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.SPOffset.setObjectName("SPOffset")
        self.verticalLayout_3.addWidget(self.SPOffset)
        self.verticalLayout_4.addWidget(self.frame_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.frame_5 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_7 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_9.addWidget(self.label_7)
        self.SPGap = QtWidgets.QDoubleSpinBox(parent=self.frame_5)
        self.SPGap.setDecimals(1)
        self.SPGap.setMinimum(0.1)
        self.SPGap.setStepType(QtWidgets.QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.SPGap.setObjectName("SPGap")
        self.verticalLayout_9.addWidget(self.SPGap)
        self.horizontalLayout_3.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_8 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.LBSheet = QtWidgets.QLabel(parent=self.frame_6)
        self.LBSheet.setObjectName("LBSheet")
        self.horizontalLayout_2.addWidget(self.LBSheet)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_10 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_6.addWidget(self.label_10)
        self.LBCopies = QtWidgets.QLabel(parent=self.frame_6)
        self.LBCopies.setObjectName("LBCopies")
        self.horizontalLayout_6.addWidget(self.LBCopies)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3.addWidget(self.frame_6)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Canvas v. Alfa"))
        self.label.setText(_translate("MainWindow", "Papel X:"))
        self.label_2.setText(_translate("MainWindow", "Papel Y:"))
        self.label_3.setText(_translate("MainWindow", "Ancho:"))
        self.label_4.setText(_translate("MainWindow", "Alto:"))
        self.label_5.setText(_translate("MainWindow", "N. Copias:"))
        self.label_6.setText(_translate("MainWindow", "Offset"))
        self.label_7.setText(_translate("MainWindow", "Gap"))
        self.label_8.setText(_translate("MainWindow", "Folios:"))
        self.LBSheet.setText(_translate("MainWindow", "0"))
        self.label_10.setText(_translate("MainWindow", "Copias:"))
        self.LBCopies.setText(_translate("MainWindow", "0"))
