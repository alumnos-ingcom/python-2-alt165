"""Prueba de la funcion es_par() del ejercicio1
"""
from src.ejercicio3 import superposicion, grado_de_superposicion

def test_superposicion_sec1_mayor():
    """Probar la funcion superposicion secuencia1 > secuencia2
    """
    secuencia1 = "Asdf"
    secuencia2 = "Bcd"
    lista = superposicion(secuencia1, secuencia2)
    assert isinstance(lista, list), "el resultado debe ser una lista"
    assert lista == [(2, "d")], "No obtenemos el resultado esperado"


def test_superposicion_sec1_menor():
    """Probar la funcion superposicion secuencia1 < secuencia2
    """
    secuencia1 = "Asdf"
    secuencia2 = "Bsdeg"
    lista = superposicion(secuencia1, secuencia2)
    assert isinstance(lista, list), "el resultado debe ser una lista"
    assert lista == [(1, "s"), (2, "d")], "No obtenemos el resultado esperado"


def test_superposicion_iguales():
    """Probar la funcion superposicion con secuencias iguales
    """
    secuencia = "Asd"
    lista = superposicion(secuencia, secuencia)
    assert isinstance(lista, list), "el resultado debe ser una lista"
    assert lista == [(0, "A"), (1, "s"), (2, "d")], "No obtenemos el resultado esperado"


def test_superposicion_distintas():
    """Probar la funcion superposicion con secuencias sin caracteres en común
    """
    secuencia1 = "Asdf"
    secuencia2 = "Fdsa"
    lista = superposicion(secuencia1, secuencia2)
    assert isinstance(lista, list), "el resultado debe ser una lista"
    assert lista == [], "No obtenemos el resultado esperado"

def test_grado_iguales():
    """Probar la funcion grado_de_superposicion con secuencias iguales
    """
    secuencia = "AAA"
    resultado = grado_de_superposicion(secuencia, secuencia)
    assert isinstance(resultado, int), "El resultado debe ser un entero"
    assert resultado == 3, "No obtenemos el resultado esperado"


def test_grado_distintos():
    """Probar la funcion grado_de_superposicion con secuencias sin
    caracteres en comun
    """
    secuencia1 = "AAA"
    secuencia2 = "111"
    resultado = grado_de_superposicion(secuencia1, secuencia2)
    assert isinstance(resultado, int), "El resultado debe ser un entero"
    assert resultado == 0, "No obtenemos el resultado esperado"


def test_grado_similares():
    """Probar la funcion grado_de_superposicion con secuencias con
    algunos caracteres en comun
    """
    secuencia1 = "AAAA111"
    secuencia2 = "1A1A"
    resultado = grado_de_superposicion(secuencia1, secuencia2)
    assert isinstance(resultado, int), "El resultado debe ser un entero"
    assert resultado == 2, "No obtenemos el resultado esperado"