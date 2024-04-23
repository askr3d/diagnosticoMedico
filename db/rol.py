from .conexion import conexionDB

class Rol:
    def __init__(self, id=None, rol=''):
        self.id = id
        self.rol = rol

    def all():
        conexion_db = conexionDB()
        cursor = conexion_db.cursor()
        consulta = "SELECT * FROM roles"
        cursor.execute(consulta)
        resultado = cursor.fetchall()

        return resultado