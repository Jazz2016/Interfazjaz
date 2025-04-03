# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login3.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        MainWindow.setMouseTracking(True)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: rgb(222, 255, 103);\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 20, 181, 41))
        self.label.setTabletTracking(False)
        self.label.setStyleSheet(u"background-color: rgb(255, 85, 0);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(180, 130, 221, 31))
        self.lineEdit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.lineEdit.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 255, 0);\n"
"aling center;")
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(180, 190, 221, 31))
        self.lineEdit_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.lineEdit_2.setStyleSheet(u"color: rgb(85, 255, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"aling center;")
        self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)
        self.lineEdit_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(180, 260, 191, 41))
        self.pushButton.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 170, 0);\n"
"font: 700 14pt \"Segoe UI\";\n"
"aling center;")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(190, 100, 71, 16))
        self.label_2.setStyleSheet(u"background-color: rgb(222, 255, 103);\n"
"font: 700 9pt \"Segoe UI\";\n"
"\n"
"color: rgb(0, 0, 0);")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(180, 170, 71, 16))
        self.label_3.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";\n"
"background-color: rgb(222, 255, 103);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 600, 33))
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
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Usuario:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a:", None))
    # retranslateUi

