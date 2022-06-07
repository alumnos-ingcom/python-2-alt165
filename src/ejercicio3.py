################
# José Lambrechts - @alt165
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
3. Súper-puestos

Desarrollar una función que indique el grado de superposición
}entre dos listas. Siendo 0 sin superposición y uno para cada
elemento superpuesto.

['H', 'o', 'l', 'a', ' ', 'M', 'u', 'n', 'd', 'o']

y

['H', 'o', 'l', 'a']

Tienen una superposición de cuatro elementos.
"""


def superposicion(secuencia1, secuencia2):
    """superposicion(str, str) -> list[tuple()]
    esta funcion devuelve una lista con los indices y los caracteres
    que se superponen
    """

    # Obtenemos el largo de la cadena más corta
    largo_secuencia = len(secuencia1)
    if largo_secuencia > len(secuencia2):
        largo_secuencia = len(secuencia2)

    i = 0
    resultado = []
    while i < largo_secuencia:
        if secuencia1[i] == secuencia2[i]:
            tupla = (i, secuencia1[i])
            resultado.append(tupla)
        i = i + 1

    return resultado


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    secuencia1 = input("Ingrese el primer texto:")
    secuencia2 = input("Ingrese el segundo texto:")
    resultado = superposicion(secuencia1, secuencia2)
    print(resultado)
    cantidad_superpuesta = len(resultado)
    print(f"La cantidad de caracteres superpuestos es: {cantidad_superpuesta}")


if __name__ == "__main__":
    principal()