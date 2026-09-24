class Editorial:
    def __init__(self, idEd: int, nombre: str, pais: str):
        self.__idEd = idEd
        self.__nombre = nombre
        self.__pais = pais

    @property
    def idEd(self):
        return self.__idEd
    @idEd.setter
    def idEd(self, value):
        self.__idEd = value

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def pais(self):
        return self.__pais
    @pais.setter
    def pais(self, value):
        self.__pais = value


class Libro:
    def __init__(self, ISBN: str, titulo: str, autor: str, precio: float, editorial: Editorial):
        self.__ISBN = ISBN
        self.__titulo = titulo
        self.__autor = autor
        self.__precio = precio
        self.__editorial = editorial

    @property
    def ISBN(self):
        return self.__ISBN
    @ISBN.setter
    def ISBN(self, value):
        self.__ISBN = value

    @property
    def titulo(self):
        return self.__titulo
    @titulo.setter
    def titulo(self, value):
        self.__titulo = value

    @property
    def autor(self):
        return self.__autor
    @autor.setter
    def autor(self, value):
        self.__autor = value

    @property
    def precio(self):
        return self.__precio
    @precio.setter
    def precio(self, value):
        self.__precio = value

    @property
    def editorial(self):
        return self.__editorial
    @editorial.setter
    def editorial(self, value):
        self.__editorial = value