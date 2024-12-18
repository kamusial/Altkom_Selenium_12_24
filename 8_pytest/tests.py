from kod import *
def test_fizzbuzz_basic():
    assert fizzbuzz(1) == 1
    assert fizzbuzz(2) == 2
    assert fizzbuzz(3) == 'Fizz'
    assert fizzbuzz(5) == 'Buzz'
    assert fizzbuzz(15) == 'FizzBuzz'

def test_fizzbuzz_advanced():
    assert fizzbuzz(0) == None
    assert fizzbuzz(-1) == None
    assert fizzbuzz('Piesek') == None
    assert fizzbuzz(5.9) == 'Buzz'
