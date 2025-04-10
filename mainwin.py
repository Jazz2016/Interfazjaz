import sys
import pymysql
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi
from Conexion import conexionDB, cerrarConexion # type: ignore

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("login3.ui", self)  # Carga directamente en self
        self.btncrearcuenta.clicked.connect(self.abrir_nuevo_usuario)
        self.btnIniciarSesion.clicked.connect(self.iniciar_sesion)

    def abrir_nuevo_usuario(self):
        """Abrir la ventana de registro"""
        self.new_user_ventana = QMainWindow()
        loadUi("NewUser.ui", self.new_user_ventana)
        self.new_user_ventana.btnRegistrar.clicked.connect(self.registrar_usuario)
        self.new_user_ventana.show()

    def registrar_usuario(self):
        username = self.new_user_ventana.textEdit.toPlainText().strip()
        password = self.new_user_ventana.textEdit2.toPlainText().strip()

        if not username or not password:
            print("Deben ingresar un nombre y una contraseña válida.")
            return
        
        miConexion, cur = conexionDB()
        if miConexion and cur:
            try:
                cur.execute("INSERT INTO usuario(NameUsuario, Password) VALUES (%s, %s)", (username, password))
                miConexion.commit()
                print("Usuario registrado correctamente.")
                self.new_user_ventana.close()  # Cierra ventana luego del registro
            except pymysql.Error as e:
                print(f"Error al registrar usuario: {e}")
            finally:
                cerrarConexion(miConexion)
        else:
            print("No se pudo conectar a la base de datos.")
    
    def iniciar_sesion(self):
        username = self.textEdit.toPlainText().strip()
        password = self.textEdit2.toPlainText().strip()

        if not username or not password:
            print("Por favor, ingrese nombre de usuario y contraseña.")
            return

        miConexion, cur = conexionDB()
        if miConexion and cur:
            try:
                cur.execute("SELECT * FROM usuario WHERE NameUsuario = %s AND Password = %s", (username, password))
                usuario = cur.fetchone()
                if usuario:
                    print("Inicio de sesión exitoso.")
                    # Aquí puedes abrir otra ventana o seguir con la lógica principal
                else:
                    print("Usuario o contraseña incorrectos.")
            except pymysql.Error as e:
                print(f"Error al verificar usuario: {e}")
            finally:
                cerrarConexion(miConexion)
        else:
            print("No se pudo conectar a la base de datos.")

# Inicializar la aplicación
app = QApplication(sys.argv)

# Cargar estilos desde un archivo externo (opcional)
try:
    with open("estilos.qss", "r") as file:
        app.setStyleSheet(file.read())
except FileNotFoundError:
    print("Archivo de estilos no encontrado, se usará el estilo por defecto.")

ventana = LoginWindow()
ventana.show()

sys.exit(app.exec())
