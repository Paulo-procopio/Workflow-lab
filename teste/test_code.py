# teste/code_teste.py

import pytest
import sys
import os

# Adiciona o diretório src ao path para importar
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.code import somar, subtrair, multiplicar, dividir

def test_somar():
    assert somar(2, 3) == 5
    assert somar(-1, 1) == 0
    assert somar(0, 0) == 0

def test_subtrair():
    assert subtrair(5, 3) == 2
    assert subtrair(0, 5) == -5

def test_multiplicar():
    assert multiplicar(3, 4) == 12
    assert multiplicar(0, 100) == 0

def test_dividir():
    assert dividir(10, 2) == 5
    assert dividir(9, 3) == 3

def test_dividir_por_zero():
    with pytest.raises(ValueError):
        dividir(10, 0)