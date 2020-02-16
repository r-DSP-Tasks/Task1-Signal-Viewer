# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'startstop.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(646, 464)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget = PlotWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(500, 300))
        self.widget.setObjectName("widget")
        self.verticalLayout_5.addWidget(self.widget)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.load_bt = QtWidgets.QToolButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.load_bt.sizePolicy().hasHeightForWidth())
        self.load_bt.setSizePolicy(sizePolicy)
        self.load_bt.setObjectName("load_bt")
        self.verticalLayout_3.addWidget(self.load_bt)
        self.start_bt = QtWidgets.QToolButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_bt.sizePolicy().hasHeightForWidth())
        self.start_bt.setSizePolicy(sizePolicy)
        self.start_bt.setObjectName("start_bt")
        self.verticalLayout_3.addWidget(self.start_bt)
        self.pause_bt = QtWidgets.QToolButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pause_bt.sizePolicy().hasHeightForWidth())
        self.pause_bt.setSizePolicy(sizePolicy)
        self.pause_bt.setObjectName("pause_bt")
        self.verticalLayout_3.addWidget(self.pause_bt)
        self.reset_bt = QtWidgets.QToolButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reset_bt.sizePolicy().hasHeightForWidth())
        self.reset_bt.setSizePolicy(sizePolicy)
        self.reset_bt.setObjectName("reset_bt")
        self.verticalLayout_3.addWidget(self.reset_bt)
        self.channel1_chk = QtWidgets.QCheckBox(self.groupBox)
        self.channel1_chk.setObjectName("channel1_chk")
        self.verticalLayout_3.addWidget(self.channel1_chk)
        self.channel2_chk = QtWidgets.QCheckBox(self.groupBox)
        self.channel2_chk.setObjectName("channel2_chk")
        self.verticalLayout_3.addWidget(self.channel2_chk)
        self.channel3_chk = QtWidgets.QCheckBox(self.groupBox)
        self.channel3_chk.setObjectName("channel3_chk")
        self.verticalLayout_3.addWidget(self.channel3_chk)
        self.channel4_chk = QtWidgets.QCheckBox(self.groupBox)
        self.channel4_chk.setObjectName("channel4_chk")
        self.verticalLayout_3.addWidget(self.channel4_chk)
        self.channel5_chk = QtWidgets.QCheckBox(self.groupBox)
        self.channel5_chk.setObjectName("channel5_chk")
        self.verticalLayout_3.addWidget(self.channel5_chk)
        self.horizontalLayout_5.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 646, 22))
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
        self.groupBox.setTitle(_translate("MainWindow", "Tools"))
        self.load_bt.setText(_translate("MainWindow", "Load"))
        self.start_bt.setText(_translate("MainWindow", "Start"))
        self.pause_bt.setText(_translate("MainWindow", "Pause"))
        self.reset_bt.setText(_translate("MainWindow", "Reset"))
        self.channel1_chk.setText(_translate("MainWindow", "Channel 1"))
        self.channel2_chk.setText(_translate("MainWindow", "Channel 2 "))
        self.channel3_chk.setText(_translate("MainWindow", "Channel 3"))
        self.channel4_chk.setText(_translate("MainWindow", "Channel 4"))
        self.channel5_chk.setText(_translate("MainWindow", "Channel 5 "))

from pyqtgraph import PlotWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

