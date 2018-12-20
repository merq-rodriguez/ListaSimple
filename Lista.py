from ListaSimple import  Nodo

class Lista:
    #Constructor Lista
    def __init__(self):
        self.__inicio = None
        self.__fin = None
        self.__cantidad_actual = 0
    
    def setInicio(self, inicio):
        self.__inicio = inicio

    def setFinal(self, fin):
        self.__fin = fin

    def inicioAdd(self, dato):
        nuevo = Nodo(dato)
        if (self.estaVacia()):
            self.__inicio = self.__fin = nuevo
            self.__cantidad_actual += 1
        else:
            nuevo.setSiguiente(self.__inicio)
            self.setInicio(nuevo)  
            self.__cantidad_actual +=  1

    def finalAdd(self, dato):
        nuevo = Nodo(dato)
        if(self.estaVacia()):
            self.__inicio = self.__fin = nuevo
            self.__cantidad_actual += 1
        else:
            self.__fin.setSiguiente(nuevo)
            self.setFinal(self.__fin.getSiguiente())
            self.__cantidad_actual += 1
            
    def imprimir(self):
        if (self.estaVacia()):
            print("La lista esta vacia.")
        else:
            indice = self.__inicio
            while indice: 
                print(indice)
                indice = indice.getSiguiente()
            
    def buscar(self, dato):
        if(self.estaVacia()):
            return None
        else:
            indice = self.__inicio
            while indice:
                if(indice.getDato() is dato):
                    return True
                else: 
                    indice = indice.getSiguiente()  
        return False    

    def estaVacia(self):
        return (self.__inicio == None)

    def longitud(self):
        return self.__cantidad_actual
