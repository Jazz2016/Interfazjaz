from PyQt5.QtWidgets import QLabel, QGraphicsDropShadowEffect, QApplication, QMainWindow
from PyQt5.QtGui import QColor
from PyQt5 import uic
import sys

class mainwindow(Qmainwindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Login6.ui", self)  # tu archivo .ui

        # Acceder al QLabel
        label = self.findChild(QLabel, "labelTitulo")

        # Crear efecto de sombra
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setColor(QColor(0, 0, 0, 160))  # negro semi-transparente
        shadow.setOffset(2, 2)

        # Aplicar al QLabel
        label.setGraphicsEffect(shadow)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
