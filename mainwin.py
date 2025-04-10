import sys
import pymysql
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi
from Conexion import conexionDB, cerrarConexion  # type: ignore

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("login3.ui", self)
        self.btncrearcuenta.clicked.connect(self.abrir_nuevo_usuario)
        self.btnIniciarSesion.clicked.connect(self.iniciar_sesion)

    def abrir_nuevo_usuario(self):
        """Abrir la ventana de registro"""
        self.new_user_ventana = QMainWindow()
        loadUi("crearcuenta.ui", self.new_user_ventana)
        self.new_user_ventana.btnRegistrar.clicked.connect(self.registrar_usuario)
        self.new_user_ventana.show()

    def registrar_usuario(self):
        """Registrar un nuevo usuario"""
        username = self.new_user_ventana.textEdit.toPlainText().strip()
        password = self.new_user_ventana.textEdit2.toPlainText().strip()
        password2 = self.new_user_ventana.textEdit3.toPlainText().strip()

        if not username or not password or not password2:
            self.new_user_ventana.label_4.setText("Debe ingresar un nombre y las contraseñas.")
            self.new_user_ventana.label_4.setStyleSheet("color: red;")
            return

        if password != password2:
            self.new_user_ventana.label_4.setText("Las contraseñas no coinciden.")
            self.new_user_ventana.label_4.setStyleSheet("color: red;")
            return

        miConexion, cur = conexionDB()
        if miConexion and cur:
            try:
                cur.execute("INSERT INTO usuario(NameUsuario, Password) VALUES (%s, %s)", (username, password))
                miConexion.commit()
                self.new_user_ventana.label_4.setText("Usuario registrado correctamente.")
                self.new_user_ventana.label_4.setStyleSheet("color: green;")

                # Limpiar campos
                self.new_user_ventana.textEdit.clear()
                self.new_user_ventana.textEdit2.clear()
                self.new_user_ventana.textEdit3.clear()

            except pymysql.IntegrityError:
                # Mostrar mensaje si el usuario ya está registrado
                self.new_user_ventana.label_4.setText("Este usuario ya está registrado.")
                self.new_user_ventana.label_4.setStyleSheet("color: red;")
            except pymysql.Error as e:
                self.new_user_ventana.label_4.setText(f"Error al registrar usuario: {e}")
                self.new_user_ventana.label_4.setStyleSheet("color: red;")
            finally:
                cerrarConexion(miConexion)
        else:
            self.new_user_ventana.label_4.setText("No se pudo conectar a la base de datos.")
            self.new_user_ventana.label_4.setStyleSheet("color: red;")

    def iniciar_sesion(self):
        """Iniciar sesión del usuario"""
        username = self.lineEdit1.text().strip()
        password = self.lineEdit2.text().strip()

        if not username or not password:
            self.label_4.setText("Por favor, ingrese nombre de usuario y contraseña.")
            self.label_4.setStyleSheet("color: red;")
            return

        miConexion, cur = conexionDB()
        if miConexion and cur:
            try:
                cur.execute("SELECT * FROM usuario WHERE NameUsuario = %s AND Password = %s", (username, password))
                usuario = cur.fetchone()
                if usuario:
                    self.label_4.setText("Inicio de sesión exitoso.")
                    self.label_4.setStyleSheet("color: green;")
                    self.lineEdit1.clear()
                    self.lineEdit2.clear()
                else:
                    self.label_4.setText("Usuario o contraseña incorrectos.")
                    self.label_4.setStyleSheet("color: red;")
            except pymysql.Error as e:
                self.label_4.setText(f"Error al verificar usuario: {e}")
                self.label_4.setStyleSheet("color: red;")
            finally:
                cerrarConexion(miConexion)
        else:
            self.label_4.setText("No se pudo conectar a la base de datos.")
            self.label_4.setStyleSheet("color: red;")

# Inicializar la aplicación
app = QApplication(sys.argv)

try:
    with open("estilos.qss", "r") as file:
        app.setStyleSheet(file.read())
except FileNotFoundError:
    print("Archivo de estilos no encontrado, se usará el estilo por defecto.")

ventana = LoginWindow()
ventana.show()

sys.exit(app.exec())
