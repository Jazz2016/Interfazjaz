from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QGraphicsDropShadowEffect
from PyQt6.QtGui import QColor
import sys

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Texto con sombra")

        # Crear etiqueta
        label = QLabel("Texto con sombra", self)
        label.setStyleSheet("font-size: 24px;")
        label.move(50, 50)

        # Crear sombra
        sombra = QGraphicsDropShadowEffect()
        sombra.setBlurRadius(10)
        sombra.setColor(QColor(0, 0, 0, 180))
        sombra.setOffset(4, 4)

        # Aplicar a la etiqueta
        label
