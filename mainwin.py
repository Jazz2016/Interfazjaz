import sys
import pymysql
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi
from connectionSQL import conexionDB, cerrarConexion

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ventana = loadUi("login.ui", self)
        self.ventana.btncrearcuenta.clicked.connect(self.abrir_nuevo_usuario)  # Botón para crear cuenta
        self.ventana.btnIniciarSesion.clicked.connect(self.iniciar_sesion) # Botón para iniciar
    
    def abrir_nuevo_usuario(self):
        """Abrir la ventana de registro"""
        self.new_user_ventana = loadUi("NewUser.ui", self)
        self.new_user_ventana.btnRegistrar.clicked.connect(self.registrar_usuario)  # Conectar el botón al método
        self.new_user_ventana.show()

        #FUNCION PARA REGISTRAR USUARIO
    def registrar_usuario(self):
        username = self.new_user_ventana.textEdit.toPlainText().strip()  # Obtener el texto de Nombre
        password = self.new_user_ventana.textEdit2.toPlainText().strip()  # Obtener el texto de Contraseña

        if not username or not password:
            print("Deben ingresar un nombre y una contraseña válida.")
            return
        
        # Conectar con la base de datos e insertar los datos
        miConexion, cur = conexionDB()
        if miConexion and cur:
            try:
                cur.execute("INSERT INTO usuario(NameUsuario, Password) VALUES (%s, %s)", (username, password))
                miConexion.commit()
                print("Usuario registrado correctamente.")
            except pymysql.Error as e:
                print(f"Error al registrar usuario: {e}")
            finally:
                cerrarConexion(miConexion)
        else:
            print("No se pudo conectar a la base de datos.")
    
    def iniciar_sesion(self):
        username = self.ventana.textEdit.toPlainText().strip()
        password = self.ventana.textEdit2.toPlainText().strip()
        if not username or not password:
            print("Por favor, ingrese nombre de usuario y contraseña.")
            return

        # Conectar con la base de datos
        miConexion, cur = conexionDB()
        if miConexion and cur:
            try:
                cur.execute("SELECT * FROM usuario WHERE NameUsuario = %s AND Password = %s", (username, password))
                usuario = cur.fetchone()  # Obtener el primer resultado

                if usuario:
                    print("Inicio de sesión exitoso.")
                    # Aquí puedes redirigir a la ventana principal
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

# Cargar estilos desde un archivo externo
with open("styles.qss", "r") as file:
    app.setStyleSheet(file.read())

ventana = LoginWindow()
ventana.show()

sys.exit(app.exec())


