from PyQt6.QtCore import QPropertyAnimation

def setupAnimations(ventana):
    # Ejemplo: Crear animación para un botón
    ventana.animEnter = QPropertyAnimation(ventana.pushButton, b"geometry")
    ventana.animEnter.setDuration(1000)  # Duración de la animación en ms
    return ventana.animEnter

