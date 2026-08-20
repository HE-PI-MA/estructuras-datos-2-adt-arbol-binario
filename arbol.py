from nodo import Nodo


class Arbol:
    def __init__(self):
        self.__raiz = None

    def get_raiz(self):
        return self.__raiz

    def set_raiz(self, nodo):
        self.__raiz = nodo

    def insertar_raiz(self, tablero):
        self.__raiz = Nodo(tablero)
        return self.__raiz

    def agregar_izquierdo(self, nodo_padre, tablero):
        nuevo_nodo = Nodo(tablero)
        nodo_padre.set_izquierdo(nuevo_nodo)
        return nuevo_nodo

    def agregar_derecho(self, nodo_padre, tablero):
        nuevo_nodo = Nodo(tablero)
        nodo_padre.set_derecho(nuevo_nodo)
        return nuevo_nodo

    def recorrido_preorden(self, nodo):
        if nodo is not None:
            nodo.mostrar_tablero()
            print()

            self.recorrido_preorden(nodo.get_izquierdo())
            self.recorrido_preorden(nodo.get_derecho())