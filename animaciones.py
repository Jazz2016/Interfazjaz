# animaciones.py
from PyQt6.QtCore import QPropertyAnimation, QRect

def agregar_animaciones(ventana):
    # Crear dos animaciones para el botón: una de entrada y otra de salida
    ventana.animEnter = QPropertyAnimation(ventana.pushButton, b"geometry")
    ventana.animEnter.setDuration(300)
    ventana.animEnter.setStartValue(ventana.pushButton.geometry())
    ventana.animEnter.setEndValue(QRect(ventana.pushButton.x()-5, ventana.pushButton.y()-5,
                                        ventana.pushButton.width()+10, ventana.pushButton.height()+10))

    ventana.animLeave = QPropertyAnimation(ventana.pushButton, b"geometry")
    ventana.animLeave.setDuration(300)
    ventana.animLeave.setStartValue(QRect(ventana.pushButton.x()-5, ventana.pushButton.y()-5,
                                         ventana.pushButton.width()+10, ventana.pushButton.height()+10))
    ventana.animLeave.setEndValue(ventana.pushButton.geometry())  # Restaurar tamaño original

    # Vincular las animaciones a los eventos de entrada y salida del cursor
    ventana.pushButton.enterEvent = lambda event: ventana.animEnter.start()
    ventana.pushButton.leaveEvent = lambda event: ventana.animLeave.start()

