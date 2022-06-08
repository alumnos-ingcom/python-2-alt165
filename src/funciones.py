class Limite_numero_exception(Exception):
    """Excepcion para numeros no permitidos
    """


import sys
    
def limita_entrada(mensaje):
    """Esta funcion muestra el mensaje pasado como argumento
    y devuelve un entero
    utilizarla para limitar la entrada. Solo permite ingresar
    enteros.
    """
    seguir = True
    while seguir:
        try:
            numero = int(input(mensaje))
            seguir = False
        except ValueError:
            print("No es un valor válido")
    return numero


def limita_entrada_acotada(mensaje, limite_minimo = -sys.maxsize - 1, limite_maximo = sys.maxsize):
    """Esta funcion muestra el mensaje pasado como argumento
    y devuelve un entero
    utilizarla para limitar la entrada. Solo permite ingresar
    enteros dentro de un rango pasado como argumento.
    """
    seguir = True
    while seguir:
        try:
            numero = int(input(mensaje))
            if numero < limite_minimo or numero > limite_maximo:
                raise Limite_numero_exception
            seguir = False
        except ValueError:
            print("No es un valor válido")
        except Limite_numero_exception:
            print("No es un valor válido")
    return numero
