import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.uic import loadUi

#inicializar la app
app = QApplication(sys.argv)

#cargar archivo .ui
ventana =loadUi("Login.ui")

#cargar el archivo de estilos
with open ("estilos.qss", "r") as file:
    app.setStyleSheet(file.read())

#Mostrar la ventana
ventana.show()

sys.exit(app.exec())
