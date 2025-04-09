import pymysql

def conexionDB():
    try:
        miConexion = pymysql.connect(
            host = "localhost", user="root", passwd="", db="login"
        )

        cur = miConexion.cursor()
        print("Conexión exitosa a la base de datos")
        return miConexion, cur
   except pymysql.error as e:
        print(f"Error al conectar a la base de daros: {e}")
        return None, None

 def cerrarConexion(miConexion):

    if miConexion:
        miConexion.close()
        print("Conexión cerrada correctamente")
    else:
        print("No hay conexión activa para cerrar") 