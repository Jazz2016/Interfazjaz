import pymysql

def conexionDB():
    try:
        miConexion = pymysql.connect(
            host="localhost", user="root", passwd="vistaalegre", db="conexionDB"
        )
        cur = miConexion.cursor()
        print("Conexión exitosa a la base de datos")
        return miConexion, cur
    except pymysql.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None, None

def cerrarConexion(miConexion):
    if miConexion:
        miConexion.close()
        print("Conexión cerrada correctamente")
    else:
        print("No hay conexión activa para cerrar")



# Prueba
if __name__ == "__main__":
    conexion, cursor = conexionDB()
    
    if conexion and cursor:
        # Verifica la base de datos activa
        cursor.execute("SELECT DATABASE();")
        db_actual = cursor.fetchone()[0]
        print(f"📌 Base de datos actual: {db_actual}")

        # Lista las tablas como prueba
        cursor.execute("SHOW TABLES;")
        tablas = cursor.fetchall()
        print("📂 Tablas encontradas:")
        for tabla in tablas:
            print(f" - {tabla[0]}")

        cerrarConexion(conexion)