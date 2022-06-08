################
# José Lambrechts - @alt165
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
6. El Cifrado del Cesar

El cifrado César o cifrado de rotación usa una encriptación de sustitución
simple. Esto significa que cada caracter se sustituye por otro caracter
de acuerdo con un sistema especifico.

La codificación debe ser tal que la palabra codificada contenga unicamente
caracteres del tipo AZaz y 0 a 9, de manera que al codificar las ultimas
letras del abecedario se vuelva a las primeras letras.

Por ejemplo, el método conocido y muy utilizado ROT13 rota el alfabeto con
13 posiciones, resultando en A->N, B->O... Y->L y Z->M.

    Implementar una funcion que codifique un texto rotandolo una cantidad
    de posiciones ajustable.

    Implementar la funcion que decodifique el texto rotado una cantidad
    de posiciones ajustable.

Una buena forma para verificar este ejercicio es codificar y decodificar
un texto y compararlo con lo que fué ingresado originalmente.

Tip: Implementar las funciones utilizando las funciones ord y chr.
"""


def crea_mapa():
    """Esta función sirve para tener la lista de caracteres disponibles
    lo implementé de esta forma para poder utilizar acentos, ñ y espacios
    """
    mapa = " 0123456789abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZáéíóúÁÉÍÓÚ"
    return mapa


def obtiene_posicion(caracter, mapa):
    """Esta funcion toma un caracter y un string y devuelve el indice en el que
    se encuentra el caracter en el mapa elegido
    """
    i = 0
    while i < len(mapa):
        if caracter == mapa[i]:
            return i
        i = i + 1


def incrementa_caracter(caracter, incremento):
    """incrementa_caracter(caracter, int) -> int
    Esta funcion toma un caracter y lo incrementa.
    si se pasa de rango vuelve a empezar.
    Devuelve un int que se usa como indice para
    encontrar el caracter codificado
    """
    mapa = crea_mapa()
    posicion = obtiene_posicion(caracter, mapa)
    posicion = posicion + incremento
    if posicion > len(mapa):
        posicion = posicion % len(mapa)
    return posicion


def codifica_string(string, incremento):
    """codifica_string(string, int) -> string
    esta funcion toma un string y un numero y devuelve un string
    codificado desplazando los caracteres una cantidad indicada
    en un mapa generado
    """
    codificado = ""
    mapa = crea_mapa()
    i = 0
    while i < len(string):
        caracter_codificado = incrementa_caracter(string[i], incremento)
        codificado = codificado + mapa[caracter_codificado]
        i = i + 1
    return codificado


def decodifica_string(string, incremento):
    """toma el string codificado y lo devuelve decodificado
    """
    incremento = -1 * incremento
    decodificado = codifica_string(string, incremento)
    return decodificado


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    cadena = input("Ingrese el caracter a codificar ")
    desplazar = int(input("Cantidad a deplazar "))
    codificada = codifica_string(cadena, desplazar)
    print(codificada)
    print(decodifica_string(codificada, desplazar))


if __name__ == "__main__":
    principal()
