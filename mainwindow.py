from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QGraphicsDropShadowEffect
from PyQt6.QtGui import QColor
from PyQt6 import uic
import sys

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Cargar el archivo .ui
        uic.loadUi("login.ui", self)

        # Acceder al QLabel que tiene el texto (asegúrate que se llama así en el .ui)
        label = self.findChild(QLabel, "labelTitulo")

        # Crear sombra
        sombra = QGraphicsDropShadowEffect(self)
        sombra.setBlurRadius(10)
        sombra.setColor(QColor(0, 0, 0, 160))
        sombra.setOffset(3, 3)

        # Aplicar sombra
        label.setGraphicsEffect(sombra)

app = QApplication(sys.argv)
ventana = LoginWindow()
ventana.show()
sys.exit(app.exec())
