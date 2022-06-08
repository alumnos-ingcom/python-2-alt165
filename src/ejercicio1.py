################
# José Lambrechts - @alt165
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
1. Pares e impares

Escribir una función que retorne True cuando un número entero es par
y False cuando no lo sea, sin utilizar módulo. (%)
"""
from funciones import limita_entrada as obtiene_numero


def es_par(numero):

    """es_par(int) -> boolean
    Esta funcion toma un valor entero y devuelve True cuando es par
    y False cuando no lo es. Observacion: El 0 se toma como valor par
    """
    comparar = numero // 2
    comparar = comparar * 2
    if comparar == numero:
        return True
    return False


def principal():

    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero = obtiene_numero("Ingrese un numero para saber si es par:")
    if es_par(numero):
        print(f"El número {numero} es par")
    else:
        print(f"El número {numero} no es par")


if __name__ == "__main__":

    principal()
