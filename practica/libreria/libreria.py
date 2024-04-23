from .libro import Libro

class Libreria:
    def __init__(self):
        self.__libros = []

    def agregar_final(self, libro:Libro):
        self.__libros.append(libro)

    def agregar_inicio(self, libro:Libro):
        self.__libros.insert(0, libro)

    def mostrar(self):
        for libro in self.__libros:
            print(libro)

    def __str__(self):
        return "".join(
            str(libro) for libro in self.__libros
        )

l01 = Libro("Programacion", "Deitel", 2020, "Algo")
l02 = Libro("Python", "Guido", 2010, "Planeta")

libreria = Libreria()
libreria.agregar_final(l01)
libreria.agregar_inicio(l02)
libreria.agregar_final(l01)
