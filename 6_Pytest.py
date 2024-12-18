# import pytest

def dodawanie(a, b):
    return a + b

def test_dodawanie_1_2():
    assert dodawanie(1, 2) == 3

def test_dodawanie2():
    assert dodawanie(3, 6) == 8

def test_dodawanie3():
    assert dodawanie(0.1, 0.2) == 0.3

print('Koniec')