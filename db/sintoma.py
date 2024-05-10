from .conexion import conexionDB
class Sintoma():
    def __init__(self, id=None ,sintoma=""):
        self.sintoma = sintoma
        self.id = id
    
    def all():
        conexion_DB = conexionDB()
        cursor = conexion_DB.cursor()
        consulta = "select * from sintomas"
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        cursor.close()
        conexion_DB.close()
        return resultado   
    
    def create(sintoma:str):
        try:
            conexion_DB = conexionDB()
            cursor = conexion_DB.cursor()
            consulta = f"INSERT INTO sintomas(sintoma) VALUES ('{sintoma}')"
            cursor.execute(consulta)
            conexion_DB.commit()
            cursor.close()
            conexion_DB.close()
            return True
        except Exception as e:
            print(f"El error al ingresar el sintoma: {e}")
            return False
        
    def update(id:str, sintoma:str):
        try:
            conexion_db = conexionDB()
            cursor = conexion_db.cursor()
            consulta = f"UPDATE sintomas SET sintoma='{sintoma}' WHERE id='{id}'"
            cursor.execute(consulta)
            conexion_db.commit()
            cursor.close()
            conexion_db.close()

            return True
        except Exception as e:
            print(f"Error al actualizar el sintoma: {e}")

            return False

    def where(id):
        conexion_DB = conexionDB()
        cursor = conexion_DB.cursor()
        consulta = f"SELECT * FROM sintomas WHERE id={id}"
        cursor.execute(consulta)
        resultado = cursor.fetchone()
        cursor.close()
        conexion_DB.close()
        if resultado!=None:
            sintoma = Sintoma()
            sintoma.id = resultado[0]
            sintoma.sintoma = resultado[1]
        return sintoma 
    
    def delete(id):
        try:
            conexion_db = conexionDB()
            cursor = conexion_db.cursor()
            consulta = f"DELETE FROM sintomas WHERE id='{id}'"
            cursor.execute(consulta)
            conexion_db.commit()
            cursor.close()
            conexion_db.close()

            return True
        except Exception as e:
            print(f"Error al borrar sintoma: {e}")
            
            return False