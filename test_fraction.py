
"""pytest-tester for Fraction."""

import pytest
from fraction import Fraction


# Initialiser

def test_init_and_simplification():
    f = Fraction(2, 4)
    assert (f.numerator, f.denominator) == (1, 2)


def test_default_denominator():
    assert Fraction(3) == Fraction(3, 1)


def test_negative_numerator_allowed():
    assert Fraction(-1, 2).numerator == -1


@pytest.mark.parametrize("den", [0, -1, -5])
def test_non_positive_denominator(den):
    with pytest.raises(ValueError):
        Fraction(1, den)


@pytest.mark.parametrize("num, den", [(1.5, 2), (1, 2.0), ("1", 2), (True, 2)])
def test_non_integer_arguments(num, den):
    with pytest.raises(TypeError):
        Fraction(num, den)