# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login3.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(400, 400))
        MainWindow.setMaximumSize(QSize(600, 600))
        MainWindow.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        MainWindow.setMouseTracking(True)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: rgb(170, 170, 255);\n"
"alternate-background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 10, 181, 41))
        self.label.setTabletTracking(False)
        self.label.setStyleSheet(u"background-color: rgb(85, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit1 = QLineEdit(self.centralwidget)
        self.lineEdit1.setObjectName(u"lineEdit1")
        self.lineEdit1.setGeometry(QRect(150, 120, 221, 31))
        self.lineEdit1.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.lineEdit1.setAutoFillBackground(False)
        self.lineEdit1.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0)\n"
"aling center;")
        self.lineEdit1.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit2 = QLineEdit(self.centralwidget)
        self.lineEdit2.setObjectName(u"lineEdit2")
        self.lineEdit2.setGeometry(QRect(150, 200, 221, 31))
        self.lineEdit2.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.lineEdit2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"aling center;")
        self.lineEdit2.setEchoMode(QLineEdit.EchoMode.Password)
        self.lineEdit2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.btnIniciarSesion = QPushButton(self.centralwidget)
        self.btnIniciarSesion.setObjectName(u"btnIniciarSesion")
        self.btnIniciarSesion.setGeometry(QRect(190, 270, 141, 41))
        self.btnIniciarSesion.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnIniciarSesion.setStyleSheet(u"background-color: rgb(0, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 8pt \"Segoe UI\";\n"
"aling center;")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(150, 90, 71, 16))
        self.label_2.setStyleSheet(u"background-color: rgb(170, 170, 255);\n"
"font: 700 9pt \"Segoe UI\";\n"
"\n"
"color: rgb(0, 0, 0);")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(150, 180, 71, 16))
        self.label_3.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";\n"
"background-color: rgb(170, 170, 255)")
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(150, 240, 181, 20))
        self.checkBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.checkBox.setStyleSheet(u"font: 700 9pt \"Segoe UI\";\n"
"background-color: rgb(170, 170, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.btncrearcuenta = QPushButton(self.centralwidget)
        self.btncrearcuenta.setObjectName(u"btncrearcuenta")
        self.btncrearcuenta.setGeometry(QRect(190, 360, 141, 41))
        self.btncrearcuenta.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btncrearcuenta.setStyleSheet(u"background-color: rgb(0, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 8pt \"Segoe UI\";\n"
"aling center;")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(170, 330, 191, 20))
        self.label_4.setStyleSheet(u"color: rgb(0, 0, 127);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 500, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Inicio de sesi\u00f3n", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Login ERP", None))
        self.lineEdit1.setText("")
        self.lineEdit2.setText("")
        self.btnIniciarSesion.setText(QCoreApplication.translate("MainWindow", u"INICIAR SESI\u00d3N", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Usuario:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a:", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Recordarme", None))
        self.btncrearcuenta.setText(QCoreApplication.translate("MainWindow", u"Crear cuenta", None))
        self.label_4.setText("")
    # retranslateUi

