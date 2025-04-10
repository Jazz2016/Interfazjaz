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
        loadUi("crearcuenta.ui", self.new_user_ventana)
        self.new_user_ventana.btnRegistrar.clicked.connect(self.registrar_usuario)
        self.new_user_ventana.show()

   

def registrar_usuario(self):
    # Obtener los datos de los campos
    username = self.new_user_ventana.textEdit.text().strip()  # Usa .text() si es un QLineEdit
    password = self.new_user_ventana.textEdit2.text().strip()  # También .text() para el otro campo

    # Verificar que los campos no estén vacíos
    if not username or not password:
        QMessageBox.warning(self.new_user_ventana, "Campos vacíos", "Debe ingresar un nombre y una contraseña.")
        return

    # Conectar con la base de datos
    miConexion, cur = conexionDB()
    if miConexion and cur:
        try:
            # Intentamos registrar el usuario
            cur.execute("INSERT INTO usuario(NameUsuario, Password) VALUES (%s, %s)", (username, password))
            miConexion.commit()

            # Mostrar mensaje de éxito
            QMessageBox.information(self.new_user_ventana, "Registro exitoso", "Usuario registrado correctamente.")
            self.new_user_ventana.close()  # Cerrar ventana después del registro

        except pymysql.IntegrityError:
            # Si hay un error de integridad, es porque el usuario ya existe
            QMessageBox.warning(self.new_user_ventana, "Usuario duplicado", "Este usuario ya está registrado.")
        
        except pymysql.Error as e:
            # Cualquier otro error relacionado con la base de datos
            QMessageBox.critical(self.new_user_ventana, "Error", f"Error al registrar usuario: {e}")
        
        finally:
            cerrarConexion(miConexion)
    else:
        # Si no se pudo conectar a la base de datos
        QMessageBox.critical(self.new_user_ventana, "Conexión fallida", "No se pudo conectar a la base de datos.")

    
    def iniciar_sesion(self):
        username = self.lineEdit1.text().strip()
        password = self.lineEdit2.text().strip()


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
