from .conexion import conexionDB

class Cita():
    
    def __init__(self, id=None, paciente_id='', medico_id='', fecha=''):
        self.id = id
        self.paciente_id = paciente_id
        self.medico_id = medico_id
        self.fecha = fecha

    def count():
        conexion_db = conexionDB()
        cursor = conexion_db.cursor()
        consulta = "SELECT COUNT(*) FROM citas"
        cursor.execute(consulta)
        resultado = cursor.fetchone()

        return resultado[0]
    
    def all():
        conexion_db = conexionDB()
        cursor = conexion_db.cursor()
        consulta = """SELECT citas.id, pacientes.nombre, users.nickname, citas.fecha
                        FROM citas
                        JOIN pacientes ON pacientes.id = citas.paciente_id
                        JOIN users ON users.id = citas.medico_id
                """
        cursor.execute(consulta)
        resultado = cursor.fetchall()

        return resultado

    def create(paciente_id:str, medico_id:str, fecha:str):
        try:
            conexion_db = conexionDB()
            cursor = conexion_db.cursor()
            consulta = f"INSERT INTO citas (paciente_id, medico_id, fecha) VALUES ('{paciente_id}', '{medico_id}', '{fecha}')"
            cursor.execute(consulta)
            conexion_db.commit()
            cursor.close()
            conexion_db.close()

            return True
        except Exception as e:
            print(f"Error al ingresar la cita: {e}")

            return False

    def update(id:str, paciente_id:str, medico_id:str, fecha:str):
        try:
            conexion_db = conexionDB()
            cursor = conexion_db.cursor()
            consulta = f"UPDATE citas SET paciente_id='{paciente_id}', medico_id='{medico_id}', fecha='{fecha}' WHERE id='{id}'"
            cursor.execute(consulta)
            conexion_db.commit()
            cursor.close()
            conexion_db.close()

            return True
        except Exception as e:
            print(f"Error al actualizar cita: {e}")

            return False

    def delete(id:str):
        try:
            conexion_db = conexionDB()
            cursor = conexion_db.cursor()
            consulta = f"DELETE FROM citas WHERE id='{id}'"
            cursor.execute(consulta)
            conexion_db.commit()
            cursor.close()
            conexion_db.close()

            return True
        
        except Exception as e:
            print(f"Error al borrar cita: {e}")

            return False

    def whereAll(palabra):
        conexion_db = conexionDB()
        cursor = conexion_db.cursor()
        consulta = f"""select citas.id, pacientes.nombre, users.nickname, citas.fecha
                        from citas
                        JOIN users ON users.id = citas.medico_id
                        JOIN pacientes ON pacientes.id = citas.paciente_id
                        WHERE citas.id LIKE '%{palabra}%' OR pacientes.nombre LIKE '%{palabra}%' OR users.nickname LIKE '%{palabra}%' OR citas.fecha LIKE '%{palabra}%'
                    """
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        cursor.close()
        conexion_db.close()

        return resultado

    def where(id):
        conexion_db = conexionDB()
        cursor = conexion_db.cursor()
        consulta = f"SELECT * FROM citas WHERE id={id}"
        cursor.execute(consulta)
        resultado = cursor.fetchone()
        cursor.close()
        conexion_db.close()
        if resultado != None:
            cita = Cita()
            cita.id = resultado[0]
            cita.paciente_id = resultado[1]
            cita.medico_id = resultado[2]
            cita.fecha = resultado[3]

            return cita
        else:
            return None