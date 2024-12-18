from kod import mnozenie

def test_mnozenie_basic():
    assert mnozenie(2, 5) == 10
    assert mnozenie(6, 5) == 30
    assert mnozenie(2, 1) == 2

def test_mnozenie_small_numbers():
    assert mnozenie(0.1, 0.2 ) == 0.02

def test_mnozenie_floats():
    assert mnozenie(10, 1.1) == 11
    assert mnozenie(1.1, 100) == 110
