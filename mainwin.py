import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi

class LoginWindow(QMainWindow):
    def __init__(self): 
        super().__init__()
        # Cargar la interfaz desde el archivo UI y asignarla a la instancia de la clase
        loadUi("login3.ui", self)
        
        # Asegurarse de que el botón existe en la UI cargada
        self.btncrearcuenta.clicked.connect(self.abrir_nuevo_usuario)  # Botón Crear Cuenta

    def abrir_nuevo_usuario(self):
        # Cargar la ventana de crear cuenta y mostrarla
        self.new_user_window = loadUi("crearcuenta.ui")
        self.new_user_window.show()  # Muestra la nueva ventana

app = QApplication(sys.argv)

# Cargar estilos
with open("estilos.qss", "r") as file:
    app.setStyleSheet(file.read())

# Crear la ventana principal y mostrarla
ventana = LoginWindow()
ventana.show()

# Ejecutar la aplicación
sys.exit(app.exec())
