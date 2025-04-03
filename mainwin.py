# mainwin.py
import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.uic import loadUi
from animaciones import agregar_animaciones  # Importar la función de animaciones

# Inicializar la app
app = QApplication(sys.argv)

# Cargar archivo .ui
ventana = loadUi("login3.ui")

# Restringir la redimensión de la ventana
ventana.setFixedSize(ventana.size())

# Cargar el archivo de estilos
with open("estilos.qss", "r") as file:
    app.setStyleSheet(file.read())

# Llamar a la función para agregar animaciones al botón
agregar_animaciones(ventana)

# Mostrar la ventana
ventana.show()

# Ejecutar la app
sys.exit(app.exec())



