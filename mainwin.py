import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi

class LoginWindow(QMainWindow):
    def init(self):
        super().init()
        self.ventana = loadUi("login.ui", self)
        self.ventana.btnCrearCuenta.clicked.connect(self.abrir_nuevo_usuario) #boton crear cuenta

    def abrir_nuevo_usuario(self):
        self.new_user_window = loadUi("NewUser.ui")
        self.new_user_window.show()  # Muestra la nueva ventana

Inicializar la aplicación
app = QApplication(sys.argv)

#cargar estilos
with open("styles.qss", "r") as file:
    app.setStyleSheet(file.read())

ventana = LoginWindow()
ventana.show()

sys.exit(app.exec())



