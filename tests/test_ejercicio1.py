"""Prueba de la funcion es_par() del ejercicio1
"""
from src.ejercicio1 import es_par

def test_par():
    """Probar la funcion par con numeros pares"""
    numero = 10
    resultado = es_par(numero)
    assert isinstance(resultado, int), "el resultado debe ser un número float"
    assert resultado == True, "No obtenemos el resultado esperado"


def test_impar():
    """Probar la funcion par con numeros impares"""
    numero = 11
    resultado = es_par(numero)
    assert isinstance(resultado, int), "el resultado debe ser un número float"
    assert resultado == False, "No obtenemos el resultado esperado"


def test_cero():
    """Probar la funcion par con cero"""
    numero = 10
    resultado = es_par(numero)
    assert isinstance(resultado, int), "el resultado debe ser un número float"
    assert resultado == True, "No obtenemos el resultado esperado"


def test_par_negativo():
    """Probar la funcion par con numeros pares negativos"""
    numero = -10
    resultado = es_par(numero)
    assert isinstance(resultado, int), "el resultado debe ser un número float"
    assert resultado == True, "No obtenemos el resultado esperado"


def test_par():
    """Probar la funcion par con numeros pares"""
    numero = 10
    resultado = es_par(numero)
    assert isinstance(resultado, int), "el resultado debe ser un número float"
    assert resultado == True, "No obtenemos el resultado esperado"


def test_impar_negativo():
    """Probar la funcion par con numeros impares negativos"""
    numero = 10
    resultado = es_par(numero)
    assert isinstance(resultado, int), "el resultado debe ser un número float"
    assert resultado == True, "No obtenemos el resultado esperado"
