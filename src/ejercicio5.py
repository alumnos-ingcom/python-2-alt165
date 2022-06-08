################
# José Lambrechts - @alt165
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
5. Corchetes balanceados

Implementar una función que determine si una cadena con corchetes está
balanceada.

Es decir, si cada corchete que abre, tiene su par que cierra. El resultado
debe ser un valor lógico indicando si esta o no balanceado.

Ejemplos

   (vacio)      True
   []           True
   [][]         True
   [[][]]       True
   ][           False
   ][][         False
   []][[]       False

La funcion deberia de ignorar todo lo que no sean corchetes.
Extra #1

Hacer que la funcion reciba que par de simbolos buscar si esta balanceado.
(como para pasar parentesis, llaves o cualquier otro)
Extra #2

Hacer que la función verifique el balanceo simultaneo de parentesis,
llaves y corchetes.
"""


def esta_balanceada(cadena):
    """esta_balanceada(str) -> boolean
    la funcion agrega los corchetes de apertura a una pila
    y si encuentra corchetes de cierre elimina el ultimo elemento
    si al final la pila está vacía el string está balanceado. Tambien se
    verifica que el primer corchete no sea de cierre.
    """
    i = 0
    pila = []
    while i < len(cadena):
        if cadena[i] == "[":
            pila.append(cadena[i])
        elif cadena[i] == "]":
            if len(pila) == 0:
                return False
            pila = pila[:-1]
        i = i + 1
    if len(pila) == 0:
        return True
    return False


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    cadena = input("Ingrese la cadena para evaluar: ")
    if esta_balanceada(cadena):
        print("La cadena está balanceada")
    else:
        print("La cadena no está balanceada")


if __name__ == "__main__":
    principal()
