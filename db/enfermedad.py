from .conexion import conexionDB

class Enfermedad():
    def __init__(self, id=None, enfermedad="", signo="", sintoma=""):
        self.id = id
        self.enfermedad = enfermedad
        self.signo = signo
        self.sintoma = sintoma
        
    def all():
        conexion_DB = conexionDB()
        cursor = conexion_DB.cursor()
        consulta = "SELECT * FROM enfermedades"
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        cursor.close()
        conexion_DB.close()

        return resultado   
    
    def create(enfermedad:str, signo:str, sintoma:str):
        try:
            conexion_DB = conexionDB()
            cursor = conexion_DB.cursor()
            consulta = f"INSERT INTO enfermedades(enfermedad, signo, sintoma) VALUES ('{enfermedad}', '{signo}', '{sintoma}')"
            cursor.execute(consulta)
            conexion_DB.commit()
            cursor.close()
            conexion_DB.close()
            return True
        except Exception as e:
            print(f"El error al ingresar la enfermedad: {e}")
            return False
        
    def update(id:str, enfermedad:str, signo:str, sintoma:str):
        try:
            conexion_db = conexionDB()
            cursor = conexion_db.cursor()
            consulta = f"UPDATE enfermedades SET enfermedad='{enfermedad}', signo='{signo}', sintoma='{sintoma}' WHERE id='{id}'"
            cursor.execute(consulta)
            conexion_db.commit()
            cursor.close()
            conexion_db.close()
            return True
        except Exception as e:
            print(f"Error al actualizar enfermedad: {e}")
            return False

    def where(id):
        conexion_db = conexionDB()
        cursor = conexion_db.cursor()
        consulta = f"SELECT * FROM enfermedades WHERE id={id}"
        cursor.execute(consulta)
        resultado = cursor.fetchone()
        cursor.close()
        conexion_db.close()
        if resultado != None:
            enfermedad = Enfermedad()
            enfermedad.id = resultado[0]
            enfermedad.enfermedad = resultado[1]
            enfermedad.signo = resultado[2]
            enfermedad.sintoma = resultado[3]

            return enfermedad
        else:
            return None
        
    def delete(id):
        try:
            conexion_db = conexionDB()
            cursor = conexion_db.cursor()
            consulta = f"DELETE FROM enfermedades WHERE id='{id}'"
            cursor.execute(consulta)
            conexion_db.commit()
            cursor.close()
            conexion_db.close()

            return True
        
        except Exception as e:
            print(f"Error al borrar enfermedad: {e}")

            return False