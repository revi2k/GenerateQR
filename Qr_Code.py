# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Qr_Code.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import qrcode
from PyQt5.QtGui import QPixmap

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.InsertData = QtWidgets.QLineEdit(self.centralwidget)
        self.InsertData.setGeometry(QtCore.QRect(10, 50, 771, 21))
        self.InsertData.setObjectName("InsertData")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 761, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.QR_CodeShow = QtWidgets.QLabel(self.centralwidget)
        self.QR_CodeShow.setObjectName("QR_CodeShow")
        self.QR_CodeShow.setGeometry(QtCore.QRect(126, 140, 531, 411))
        self.QR_CodeShow.setAlignment(QtCore.Qt.AlignCenter)
        self.GenerateQR = QtWidgets.QPushButton(self.centralwidget)
        self.GenerateQR.setGeometry(QtCore.QRect(200, 90, 381, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.GenerateQR.setFont(font)
        self.GenerateQR.setObjectName("GenerateQR")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def encode_qr():
            data_to_encode = self.InsertData.text()
            img = qrcode.make(data_to_encode)
            img.save("generated_qr.png")
            pixmap = QPixmap("generated_qr.png")
            self.QR_CodeShow.setPixmap(pixmap)

        self.GenerateQR.clicked.connect(encode_qr)




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Insert data to encode</span></p></body></html>"))
        self.GenerateQR.setText(_translate("MainWindow", "GENERATE"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    app.setStyle('Fusion')
    MainWindow.show()
    sys.exit(app.exec_())