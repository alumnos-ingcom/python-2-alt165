"""Prueba de la funcion es_par() del ejercicio1
"""
from src.ejercicio5 import esta_balanceada

def test_balanceada_vacia():
    """Probar la funcion para cadenas vacias
    """
    cadena = ""
    resultado = esta_balanceada(cadena)
    assert isinstance(resultado, bool), "el resultado debe ser bool"
    assert resultado == True, "No obtenemos el resultado esperado"


def test_balanceada_true():
    """Probar la funcion para cadenas balanceadas
    """
    cadena = "[[]][][[[]]]"
    resultado = esta_balanceada(cadena)
    assert isinstance(resultado, bool), "el resultado debe ser bool"
    assert resultado == True, "No obtenemos el resultado esperado"


def test_balanceada_false():
    """Probar la funcion para cadenas desbalanceadas
    """
    cadena = "[[]][][[[]]"
    resultado = esta_balanceada(cadena)
    assert isinstance(resultado, bool), "el resultado debe ser bool"
    assert resultado == False, "No obtenemos el resultado esperado"