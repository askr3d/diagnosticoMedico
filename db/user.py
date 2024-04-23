from .conexion import conexionDB

class User:
    def __init__(self, id=None, nickname='', password='', rol_id=0):
        self.id = id
        self.nickname = nickname
        self.password = password
        self.rol_id = rol_id

    def all():
        conexion_db = conexionDB()
        cursor = conexion_db.cursor()
        consulta = """SELECT users.id, users.nickname, roles.rol
                        FROM users
                        JOIN roles ON roles.id = users.rol_id
                    """
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        cursor.close()
        conexion_db.close()

        return resultado
    
    def count():
        conexion_db = conexionDB()
        cursor = conexion_db.cursor()
        consulta = "SELECT COUNT(*) FROM users"
        cursor.execute(consulta)
        resultado = cursor.fetchone()
        cursor.close()
        conexion_db.close()

        return resultado[0]

    def create(nickname:str, password:str, rol_id:str):
        try:
            conexion_db = conexionDB()
            cursor = conexion_db.cursor()
            consulta = f"INSERT INTO users (nickname, password, rol_id) VALUES ('{nickname}', '{password}', '{rol_id}')"
            cursor.execute(consulta)
            conexion_db.commit()
            cursor.close()
            conexion_db.close()

            return True
        except Exception as e:
            print(f"Error al insertar usuario: {e}")

            return False

    def update(id:str, nickname:str, password:str, rol_id:str):
        try:
            conexion_db = conexionDB()
            cursor = conexion_db.cursor()
            consulta = f"UPDATE users SET nickname='{nickname}', password='{password}', rol_id='{rol_id}' WHERE id='{id}'"
            cursor.execute(consulta)
            conexion_db.commit()
            cursor.close()
            conexion_db.close()

            return True
        
        except Exception as e:
            print(f"Error al actualizar usuario: {e}")

            return False

    def delete(id):
        try:
            conexion_db = conexionDB()
            cursor = conexion_db.cursor()
            consulta = f"DELETE FROM users WHERE id='{id}'"
            cursor.execute(consulta)
            conexion_db.commit()
            cursor.close()
            conexion_db.close()

            return True
        
        except Exception as e:
            print(f"Error al borrar usuario: {e}")

            return False

    def find(nickname, password):
        conexion_db = conexionDB()
        cursor = conexion_db.cursor()
        consulta = f"SELECT * FROM users WHERE nickname='{nickname}' AND password='{password}'"
        cursor.execute(consulta)
        resultado = cursor.fetchone()
        cursor.close()
        conexion_db.close()
        if resultado != None:
            user = User()
            user.id = resultado[0]
            user.nickname = resultado[1]
            user.password = resultado[2]
            user.rol_id = resultado[3]

            return user
        else:
            return None
    
    def where(id):
        conexion_db = conexionDB()
        cursor = conexion_db.cursor()
        consulta = f"SELECT * FROM users WHERE id={id}"
        cursor.execute(consulta)
        resultado = cursor.fetchone()
        cursor.close()
        conexion_db.close()
        if resultado != None:
            user = User()
            user.id = resultado[0]
            user.nickname = resultado[1]
            user.password = resultado[2]
            user.rol_id = resultado[3]

            return user
        else:
            return None

    def whereAll(palabra):
        conexion_db = conexionDB()
        cursor = conexion_db.cursor()
        consulta = f"select users.id, users.nickname, roles.rol from users JOIN roles ON roles.id = users.rol_id WHERE users.id LIKE '%{palabra}%' OR users.nickname LIKE '%{palabra}%' OR roles.rol LIKE '%{palabra}%'"
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        cursor.close()
        conexion_db.close()

        return resultado

    def getByRol(rol_id: str):
        conexion_db = conexionDB()
        cursor = conexion_db.cursor()
        consulta = f"""SELECT users.id, users.nickname
                        FROM users
                        WHERE users.rol_id = {rol_id}
                    """
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        cursor.close()
        conexion_db.close()

        return resultado

    def __str__(self):
        return (
            'ID: ' + str(self.id) + '\n' +
            'Nickname: ' + self.nickname + '\n' +
            'Password: ' + self.password + '\n'
        )