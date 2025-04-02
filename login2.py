from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 600))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.OpenHandCursor))
        MainWindow.setMouseTracking(True)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(222, 255, 103);\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 20, 181, 41))
        self.label.setTabletTracking(False)
        self.label.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(220, 120, 221, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 255, 0);\n"
"aling center;")
        self.lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 190, 221, 31))
        self.lineEdit_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.OpenHandCursor))
        self.lineEdit_2.setStyleSheet("color: rgb(85, 255, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"aling center;")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 260, 191, 41))
        self.pushButton.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"font: 700 14pt \"Segoe UI\";\n"
"aling center;")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 100, 71, 16))
        self.label_2.setStyleSheet("background-color: rgb(222, 255, 103);\n"
"font: 700 9pt \"Segoe UI\";\n"
"\n"
"color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 170, 71, 16))
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";\n"
"background-color: rgb(222, 255, 103);")
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 33))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Inicio de sesión"))
        self.label.setText(_translate("MainWindow", "Login ERP"))
        self.lineEdit.setText(_translate("MainWindow", "usuario:"))
        self.lineEdit_2.setText(_translate("MainWindow", "contraseña:"))
        self.pushButton.setText(_translate("MainWindow", "Aceptar"))
        self.label_2.setText(_translate("MainWindow", "Usuario:"))
        self.label_3.setText(_translate("MainWindow", "Contraseña:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
