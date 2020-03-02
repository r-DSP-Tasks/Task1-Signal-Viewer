# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'playground.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1082, 831)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 550, 441, 211))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelMin = QtWidgets.QLabel(self.centralwidget)
        self.labelMin.setGeometry(QtCore.QRect(480, 740, 31, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelMin.setFont(font)
        self.labelMin.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.labelMin.setObjectName("labelMin")
        self.labelMax = QtWidgets.QLabel(self.centralwidget)
        self.labelMax.setGeometry(QtCore.QRect(490, 460, 11, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelMax.setFont(font)
        self.labelMax.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.labelMax.setObjectName("labelMax")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(570, 590, 112, 168))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.windowButton1 = QtWidgets.QRadioButton(self.groupBox)
        self.windowButton1.setChecked(True)
        self.windowButton1.setObjectName("windowButton1")
        self.verticalLayout_3.addWidget(self.windowButton1)
        self.windowButton2 = QtWidgets.QRadioButton(self.groupBox)
        self.windowButton2.setObjectName("windowButton2")
        self.verticalLayout_3.addWidget(self.windowButton2)
        self.windowButton3 = QtWidgets.QRadioButton(self.groupBox)
        self.windowButton3.setObjectName("windowButton3")
        self.verticalLayout_3.addWidget(self.windowButton3)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 1041, 381))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget1 = PlotWidget(self.horizontalLayoutWidget_2)
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2.addWidget(self.widget1)
        self.widget2 = PlotWidget(self.horizontalLayoutWidget_2)
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_2.addWidget(self.widget2)
        self.widget3 = PlotWidget(self.horizontalLayoutWidget_2)
        self.widget3.setObjectName("widget3")
        self.horizontalLayout_2.addWidget(self.widget3)
        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setGeometry(QtCore.QRect(760, 590, 93, 28))
        self.resetButton.setObjectName("resetButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1082, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelMin.setText(_translate("MainWindow", "-5"))
        self.labelMax.setText(_translate("MainWindow", "5"))
        self.groupBox.setTitle(_translate("MainWindow", "Window Mode"))
        self.windowButton1.setText(_translate("MainWindow", "Rectangle"))
        self.windowButton2.setText(_translate("MainWindow", "Hanning"))
        self.windowButton3.setText(_translate("MainWindow", "Hamming"))
        self.resetButton.setText(_translate("MainWindow", "Reset Bands"))

from pyqtgraph import PlotWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

