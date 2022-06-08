"""Prueba de la funcion es_par() del ejercicio1
"""
from src.ejercicio2 import obtiene_secuencia, obtiene_promedio, obtiene_minimo, obtiene_maximo

def test_secuencia():
    """Probar la funcion obtiene_secuencia
    solo verifica el tipo de datos obtenido
    """
    lista = obtiene_secuencia(-10, 10, 5)
    assert isinstance(lista, list), "el resultado debe ser una lista"


def test_promedio():
    """Probar la funcion promedio
    """
    lista = [-10, 40, 0]
    resultado = obtiene_promedio(lista)
    assert isinstance(resultado, float), "el resultado debe ser una lista"
    assert resultado == 10, "No obtenemos el resultado esperado"


def test_promedio_cero():
    """Probar la funcion promedio con valores iguales a cero
    """
    lista = [0, 0, 0]
    resultado = obtiene_promedio(lista)
    assert isinstance(resultado, float), "el resultado debe ser una lista"
    assert resultado == 0, "No obtenemos el resultado esperado"


def test_minimo():
    """Probar la funcion obtiene_minimo
    """
    lista = [-10, 40, 0]
    resultado = obtiene_minimo(lista)
    assert isinstance(resultado, int), "el resultado debe ser una lista"
    assert resultado == -10, "No obtenemos el resultado esperado"


def test_minimo_iguales():
    """Probar la funcion obtiene_minimo con valores iguales
    """
    lista = [10, 10, 10]
    resultado = obtiene_minimo(lista)
    assert isinstance(resultado, int), "el resultado debe ser una lista"
    assert resultado == 10, "No obtenemos el resultado esperado"


def test_maximo():
    """Probar la funcion obtiene_maximo
    """
    lista = [-10, 40, 0]
    resultado = obtiene_maximo(lista)
    assert isinstance(resultado, int), "el resultado debe ser una lista"
    assert resultado == 40, "No obtenemos el resultado esperado"


def test_maximo():
    """Probar la funcion obtiene_maximo con valores iguales
    """
    lista = [10, 10, 10]
    resultado = obtiene_maximo(lista)
    assert isinstance(resultado, int), "el resultado debe ser una lista"
    assert resultado == 10, "No obtenemos el resultado esperado"