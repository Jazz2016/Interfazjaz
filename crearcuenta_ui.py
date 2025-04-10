# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'crearcuenta.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 600)
        MainWindow.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(260, 60, 91, 20))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(250, 150, 101, 21))
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(160, 90, 281, 31))
        self.textEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.textEdit2 = QTextEdit(self.centralwidget)
        self.textEdit2.setObjectName(u"textEdit2")
        self.textEdit2.setGeometry(QRect(160, 180, 281, 31))
        self.textEdit2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(210, 240, 171, 21))
        self.textEdit3 = QTextEdit(self.centralwidget)
        self.textEdit3.setObjectName(u"textEdit3")
        self.textEdit3.setGeometry(QRect(160, 270, 281, 31))
        self.textEdit3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.btnRegistrar = QPushButton(self.centralwidget)
        self.btnRegistrar.setObjectName(u"btnRegistrar")
        self.btnRegistrar.setGeometry(QRect(240, 340, 131, 41))
        self.btnRegistrar.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 11pt \"Segoe UI\";\n"
"background-color: rgb(170, 170, 255);")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(140, 430, 311, 31))
        self.label_4.setStyleSheet(u"color: rgb(0, 0, 127);")
        self.label_4.setTextFormat(Qt.TextFormat.AutoText)
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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nombre Usuario", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Ingresa contrase\u00f1a", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Ingresa contrase\u00f1a nuevamente", None))
        self.btnRegistrar.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.label_4.setText("")
    # retranslateUi

