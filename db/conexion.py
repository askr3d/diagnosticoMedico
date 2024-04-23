import mysql.connector

def conexionDB():
    # Parámetros de conexión
    host = "localhost"
    usuario = "root"
    contraseña = "root"
    base_de_datos = "hospital"

    # Establecer la conexión
    conexion = mysql.connector.connect(
        host=host,
        user=usuario,
        password=contraseña,
        database=base_de_datos
    )

    return conexion
