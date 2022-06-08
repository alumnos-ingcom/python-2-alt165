"""Prueba de la funcion es_par() del ejercicio1
"""
from src.ejercicio6 import crea_mapa, obtiene_posicion, incrementa_caracter, codifica_string, decodifica_string


def test_obtiene_posicion():
    """Probar la funcion , solo verifico el tipo de datos devuelto y el resultado
    """
    mapa = crea_mapa()
    caracter = " "
    resultado = obtiene_posicion(caracter, mapa)
    assert isinstance(resultado, int), "el resultado debe ser int"
    assert resultado == 0, "No obtenemos el resultado esperado"


def test_incrementa_en_rango():
    """Probar la funcion dentro del rango del mapa
    """
    caracter = " "
    desplazar = 10
    resultado = incrementa_caracter(caracter, desplazar)
    assert isinstance(resultado, int), "el resultado debe ser int"
    assert resultado == 10, "No obtenemos el resultado esperado"


def test_incrementa_fuera_de_rango():
    """Probar la funcion cuando el incremento
    excede el rango del mapa
    """
    caracter = "Ú"
    desplazar = 10
    resultado = incrementa_caracter(caracter, desplazar)
    assert isinstance(resultado, int), "el resultado debe ser int"
    assert resultado == 9, "No obtenemos el resultado esperado"


def test_codifica_y_decodifica():
    """Probar las dos funciones juntas
    """
    cadena = "Cadena de prueba de codificación"
    incremento = 10
    codificado = codifica_string(cadena, incremento)
    decodificado = decodifica_string(codificado, incremento)
    assert isinstance(codificado, str), "El resultado debe ser un str"
    assert isinstance(decodificado, str), "El resultado debe ser un str"
    assert cadena == decodificado, "No obtenemos el resultado esperado"