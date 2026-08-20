from arbol import Arbol


arbol = Arbol()

tablero_raiz = [
    ["X", "", ""],
    ["", "", ""],
    ["", "", ""]
]

raiz = arbol.insertar_raiz(tablero_raiz)


tablero_izquierdo = [
    ["X", "O", ""],
    ["", "", ""],
    ["", "", ""]
]

arbol.agregar_izquierdo(raiz, tablero_izquierdo)


tablero_derecho = [
    ["X", "", ""],
    ["", "O", ""],
    ["", "", ""]
]

arbol.agregar_derecho(raiz, tablero_derecho)


print("RECORRIDO PREORDEN DEL ARBOL")
print()

arbol.recorrido_preorden(arbol.get_raiz())