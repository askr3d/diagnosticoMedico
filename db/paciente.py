from .conexion import conexionDB

class Paciente():
    
    def __init__(self, id=None, nombre='', apellidos='', edad=-1):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    def all():
        conexion_db = conexionDB()
        cursor = conexion_db.cursor()
        consulta = "SELECT * FROM pacientes"
        cursor.execute(consulta)
        resultado = cursor.fetchall()

        return resultado

    def create(nombre:str, apellidos:str, edad:str):
        try:
            conexion_db = conexionDB()
            cursor = conexion_db.cursor()
            consulta = f"INSERT INTO pacientes (nombre, apellidos, edad) VALUES ('{nombre}', '{apellidos}', '{edad}')"
            cursor.execute(consulta)
            conexion_db.commit()
            cursor.close()
            conexion_db.close()

            return True
        except Exception as e:
            print(f"Error al ingresar paciente: {e}")

            return False
        
    def update(id:str, nombre:str, apellidos:str, edad:str):
        try:
            conexion_db = conexionDB()
            cursor = conexion_db.cursor()
            consulta = f"UPDATE pacientes SET nombre='{nombre}', apellidos='{apellidos}', edad='{edad}' WHERE id='{id}'"
            cursor.execute(consulta)
            conexion_db.commit()
            cursor.close()
            conexion_db.close()

            return True
        except Exception as e:
            print(f"Error al actualizar paciente: {e}")

            return False

    def where(id):
        conexion_db = conexionDB()
        cursor = conexion_db.cursor()
        consulta = f"SELECT * FROM pacientes WHERE id={id}"
        cursor.execute(consulta)
        resultado = cursor.fetchone()
        cursor.close()
        conexion_db.close()
        if resultado != None:
            paciente = Paciente()
            paciente.id = resultado[0]
            paciente.nombre = resultado[1]
            paciente.apellidos = resultado[2]
            paciente.edad = resultado[3]

            return paciente
        else:
            return None

    def whereAll(palabra):
        conexion_db = conexionDB()
        cursor = conexion_db.cursor()
        consulta = f"select * from pacientes WHERE id LIKE '%{palabra}%' OR nombre LIKE '%{palabra}%' OR apellidos LIKE '%{palabra}%' OR edad LIKE '%{palabra}%'"
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        cursor.close()
        conexion_db.close()

        return resultado

    def delete(id):
        try:
            conexion_db = conexionDB()
            cursor = conexion_db.cursor()
            consulta = f"DELETE FROM pacientes WHERE id='{id}'"
            cursor.execute(consulta)
            conexion_db.commit()
            cursor.close()
            conexion_db.close()

            return True
        
        except Exception as e:
            print(f"Error al borrar usuario: {e}")

            return False

    def count():
        conexion_db = conexionDB()
        cursor = conexion_db.cursor()
        consulta = "SELECT COUNT(*) FROM pacientes"
        cursor.execute(consulta)
        resultado = cursor.fetchone()

        return resultado[0]
