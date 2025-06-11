import pytest
from fizzbuzz import fizzbuzz

@pytest.mark.parametrize("numero, resultado_esperado", [
    (1, "1"),
    (2, "2"),
    (3, "Fizz"),
    (4, "4"),
    (5, "Buzz"),
    (6, "Fizz"),
    (10, "Buzz"),
    (15, "FizzBuzz"),
    (30, "FizzBuzz"),
])
def test_fizzbuzz_geral(numero, resultado_esperado):
    assert fizzbuzz(numero) == resultado_esperado
