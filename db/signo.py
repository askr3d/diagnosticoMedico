from .conexion import conexionDB

class Signo():
    def __init__(self, id=None, signo=""):
        self.id = id
        self.signo = signo
        
    def all():
        conexion_DB = conexionDB()
        cursor = conexion_DB.cursor()
        consulta = "SELECT * FROM signos"
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        cursor.close()
        conexion_DB.close()
        return resultado   
    
    def create(signo:str):
        try:
            conexion_DB = conexionDB()
            cursor = conexion_DB.cursor()
            consulta = f"INSERT INTO signos(signo) VALUES ('{signo}')"
            cursor.execute(consulta)
            conexion_DB.commit()
            cursor.close()
            conexion_DB.close()
            return True
        except Exception as e:
            print(f"El error al ingresar el signo: {e}")
            return False
        
    def update(id:str, signo:str):
        try:
            conexion_db = conexionDB()
            cursor = conexion_db.cursor()
            consulta = f"UPDATE signos SET signo='{signo}' WHERE id='{id}'"
            cursor.execute(consulta)
            conexion_db.commit()
            cursor.close()
            conexion_db.close()
            return True
        except Exception as e:
            print(f"Error al actualizar el signo: {e}")
            return False


    def where(id):
        conexion_DB = conexionDB()
        cursor = conexion_DB.cursor()
        consulta = f"SELECT * FROM signos WHERE id={id}"
        cursor.execute(consulta)
        resultado = cursor.fetchone()
        cursor.close()
        conexion_DB.close()
        if resultado!=None:
            signo = Signo()
            signo.id = resultado[0]
            signo.signo = resultado[1]
        return signo 
    
    def delete(id):
        try:
            conexion_db = conexionDB()
            cursor = conexion_db.cursor()
            consulta = f"DELETE FROM signos WHERE id='{id}'"
            cursor.execute(consulta)
            conexion_db.commit()
            cursor.close()
            conexion_db.close()

            return True
        except Exception as e:
            print(f"Error al borrar signo: {e}")
            
            return False