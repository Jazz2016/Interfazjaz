import sys
import pymysql
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel
from PyQt6.uic import loadUi
from Conexion import conexionDB, cerrarConexion  # type: ignore

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
        """Registrar un nuevo usuario"""
        # Obtener los datos de los campos
        username = self.new_user_ventana.textEdit.toPlainText().strip()  # Usa .toPlainText() si es un QTextEdit
        password = self.new_user_ventana.textEdit2.toPlainText().strip()  # También .toPlainText() para el otro campo

        # Verificar que los campos no estén vacíos
        if not username or not password:
            self.new_user_ventana.label_4.setText("Debe ingresar un nombre y una contraseña.")
            self.new_user_ventana.label_4.setStyleSheet("color: red;")
            return

        # Conectar con la base de datos
        miConexion, cur = conexionDB()
        if miConexion and cur:
            try:
                # Intentamos registrar el usuario
                cur.execute("INSERT INTO usuario(NameUsuario, Password) VALUES (%s, %s)", (username, password))
                miConexion.commit()

                # Mostrar mensaje de éxito en el QLabel de la ventana de registro
                self.new_user_ventana.label_4.setText("Usuario registrado correctamente.")
                self.new_user_ventana.label_4.setStyleSheet("color: green;")
                self.new_user_ventana.close()  # Cerrar ventana después del registro

            except pymysql.IntegrityError:
                # Si hay un error de integridad, es porque el usuario ya existe
                self.new_user_ventana.label_4.setText("Este usuario ya está registrado.")
                self.new_user_ventana.label_4.setStyleSheet("color: red;")
            
            except pymysql.Error as e:
                # Cualquier otro error relacionado con la base de datos
                self.new_user_ventana.label_4.setText(f"Error al registrar usuario: {e}")
                self.new_user_ventana.label_4.setStyleSheet("color: red;")
            
            finally:
                cerrarConexion(miConexion)
        else:
            # Si no se pudo conectar a la base de datos
            self.new_user_ventana.label_4.setText("No se pudo conectar a la base de datos.")
            self.new_user_ventana.label_4.setStyleSheet("color: red;")
    
    def iniciar_sesion(self):
        """Iniciar sesión del usuario"""
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
