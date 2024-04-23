from .user import User

class Sesion:
    def __init__(self, sesion=False):
        self.sesion = sesion

    def login(nickname, password):
        return User.find(nickname, password)
    