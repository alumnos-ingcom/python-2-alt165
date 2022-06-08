################
# José Lambrechts - @alt165
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
2. Estadísticas

Implementar una función que obtenga los máximos, mínimos y promedio
de una secuencia con números, retornando los valores como una tuple.

Sin utilizar lazos for o las funciones integradas del lenguaje que
procesan secuencias.
"""

import random


def obtiene_maximo(secuencia):
    """obtiene_secuencia(lista[int..int]) -> int
    """
    maximo = secuencia[0]
    i = 1
    while i < len(secuencia):
        if maximo < secuencia[i]:
            maximo = secuencia[i]
        i = i + 1
    return maximo


def obtiene_minimo(secuencia):
    """obtiene_secuencia(lista[int..int]) -> int
    """
    minimo = secuencia[0]
    i = 1
    while i < len(secuencia):
        if minimo > secuencia[i]:
            minimo = secuencia[i]
        i = i + 1
    return minimo


def obtiene_promedio(secuencia):
    """obtiene_secuencia(lista[int..int]) -> float
    """
    total = 0
    i = 0
    while i < len(secuencia):
        total = total + secuencia[i]
        i = i + 1
    return total / i


def obtiene_secuencia(rango_minimo, rango_maximo, tamano):
    """obtiene_secuencia(int, int, int) -> list
    esta funcion devuelve una secuencia de enteros
    """
    i = 0
    secuencia = []
    while i < tamano:
        numero = random.randint(rango_minimo, rango_maximo)
        secuencia.append(numero)
        i = i + 1
    return secuencia


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    lista = obtiene_secuencia(-10, 10, 5)
    maximo = obtiene_maximo(lista)
    minimo = obtiene_minimo(lista)
    promedio = obtiene_promedio(lista)
    print(f"En la lista {lista}")
    print(f"El máximo es: {maximo}")
    print(f"El mínimo es: {minimo}")
    print(f"El promedio es: {promedio:.2}")


if __name__ == "__main__":
    principal()
