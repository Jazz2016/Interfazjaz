import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.uic import loadUi
import animaciones  # Importa animaciones.py después de definir ventana

# Inicializar la app
app = QApplication(sys.argv)

# Cargar archivo .ui
ventana = loadUi("login3.ui")  # Ahora la ventana está disponible

# Cargar el archivo de estilos
with open("estilos.qss", "r") as file:
    app.setStyleSheet(file.read())

# Llamar a las funciones de animaciones y pasarle la ventana
animaciones.setupAnimations(ventana)  # Cambia "mi_funcion" por "setupAnimations"

# Mostrar la ventana
ventana.show()

sys.exit(app.exec())
