import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QLabel,
)
from PyQt6.QtCore import Qt


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        #para cargar el UI en archivo .py
        #loadUi('ruta del archivo .ui', self)

        # Configuración de la ventana
        self.setWindowTitle("Inicio de Sesión")
        self.setGeometry(100, 100, 400, 400)

        # Diseño vertical
        layout = QVBoxLayout()

        # Etiqueta para el título
        self.title_label = QLabel("Login ERP", self)
        self.title_label.setStyleSheet("font-size: 25px; font-weight: bold;")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.title_label)

        # Campo de usuario con estilo
        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Usuario")
        self.username_input.setStyleSheet(
            """
            QLineEdit {
                border: 2px solid #cccccc;
                border-radius: 10px;
                padding: 5px;
                width: 200px; /* Limita el ancho */
                margin: 0 auto; /* Centra horizontalmente */
            }
        """
        )
        layout.addWidget(self.username_input, alignment=Qt.AlignmentFlag.AlignCenter)

        # Campo de contraseña con estilo
        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Contraseña")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setStyleSheet(
            """
            QLineEdit {
                border: 2px solid #cccccc;
                border-radius: 10px;
                padding: 5px;
                width: 200px;
                margin: 0 auto;
            }
        """
        )
        layout.addWidget(self.password_input, alignment=Qt.AlignmentFlag.AlignCenter)

        # Botón de inicio de sesión
        self.login_button = QPushButton("Iniciar Sesión", self)
        self.login_button.setStyleSheet(
            """
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 10px;
                padding: 5px;
                width: 100px;
                margin: 0 auto;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """
        )
        layout.addWidget(self.login_button, alignment=Qt.AlignmentFlag.AlignCenter)

        # Configurar el diseño
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
