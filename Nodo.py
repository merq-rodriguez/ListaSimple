class Nodo:
#Constructor nodo
    def __init__(self, dato=None, siguiente=None):
        self.__siguiente = siguiente
        self.__dato = dato

    def __str__(self):
        return str(self.__dato)

    def getSiguiente(self):
        return self.__siguiente

    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente

    def getDato(self):
        return self.__dato

    def setDato(self, dato):
        self.__dato = dato
