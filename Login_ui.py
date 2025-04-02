# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
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
        MainWindow.resize(443, 412)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        MainWindow.setStyleSheet(u"\n"
"background-color: rgb(147, 255, 215);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 20, 121, 41))
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 16pt \"Segoe UI\";\n"
"\n"
"")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setMargin(-1)
        self.password = QLineEdit(self.centralwidget)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(140, 150, 141, 22))
        sizePolicy.setHeightForWidth(self.password.sizePolicy().hasHeightForWidth())
        self.password.setSizePolicy(sizePolicy)
        self.password.setCursor(QCursor(Qt.CursorShape.UpArrowCursor))
        self.password.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"align: center;")
        self.Iniciar = QPushButton(self.centralwidget)
        self.Iniciar.setObjectName(u"Iniciar")
        self.Iniciar.setGeometry(QRect(160, 210, 111, 41))
        sizePolicy.setHeightForWidth(self.Iniciar.sizePolicy().hasHeightForWidth())
        self.Iniciar.setSizePolicy(sizePolicy)
        self.Iniciar.setCursor(QCursor(Qt.CursorShape.WhatsThisCursor))
        self.Iniciar.setStyleSheet(u"background-color: rgb(233, 215, 255);\n"
"color: rgb(0, 0, 0);")
        self.Iniciar.setCheckable(False)
        self.Iniciar.setAutoDefault(False)
        self.Iniciar.setFlat(False)
        self.Usuario = QLineEdit(self.centralwidget)
        self.Usuario.setObjectName(u"Usuario")
        self.Usuario.setGeometry(QRect(140, 100, 141, 22))
        sizePolicy.setHeightForWidth(self.Usuario.sizePolicy().hasHeightForWidth())
        self.Usuario.setSizePolicy(sizePolicy)
        self.Usuario.setSizeIncrement(QSize(2, 2))
        self.Usuario.setBaseSize(QSize(2, 2))
        self.Usuario.setCursor(QCursor(Qt.CursorShape.UpArrowCursor))
        self.Usuario.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"align: center;")
        self.Usuario.setDragEnabled(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 443, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.Iniciar.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Inicio de sesi\u00f3n", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Login ERP", None))
        self.password.setText(QCoreApplication.translate("MainWindow", u"CONTRASE\u00d1A", None))
        self.Iniciar.setText(QCoreApplication.translate("MainWindow", u"Iniciar sesi\u00f3n", None))
        self.Usuario.setText(QCoreApplication.translate("MainWindow", u"USUARIO", None))
        self.Usuario.setPlaceholderText("")
    # retranslateUi

