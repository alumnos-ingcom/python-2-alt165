"""Prueba de la funcion es_par() del ejercicio1
"""
from src.ejercicio4 import fibonacci

def test_fibo_cero():
    """Probar la funcion fibonacci para cero
    """
    resultado = fibonacci(0)
    assert isinstance(resultado, int), "el resultado debe ser int"
    assert resultado == 0, "No obtenemos el resultado esperado"


def test_fibo_mayor():
    """Probar la funcion fibonacci para un numero mayor
    """
    resultado = fibonacci(3)
    assert isinstance(resultado, int), "el resultado debe ser int"
    assert resultado == 5, "No obtenemos el resultado esperado"
