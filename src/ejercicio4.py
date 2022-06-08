################
# José Lambrechts - @alt165
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
4. Fibonacci

La sucesión de Fibonacci es una sucesión infinita donde cada elemento
es la suma de los dos anteriores. En la misma, los dos primeros términos
son 1. (En algunos lugares se toma el primer término en 0 y el segundo en
1) Implementar una función que permita obtener el n-esimo termino de la
sucesión de Fibonacci. Siendo este número un entero positivo mayor a 2.
"""


from funciones import limita_entrada_acotada as obtiene_numero


def fibonacci(posicion):
    variable1 = 1
    variable2 = 1
    resultado = 0
    i = 0
    while i < posicion:
        resultado = variable1 + variable2
        variable1 = variable2
        variable2 = resultado
        i = i + 1
    return resultado


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero = obtiene_numero("Ingrese numero para calcular Fibonacci: ", 2)
    # obtiene numero como está utilizada acá solo permite ingresar valores
    #enteros mayores a 2
    resultado = fibonacci(numero)
    print(resultado)


if __name__ == "__main__":
    principal()
