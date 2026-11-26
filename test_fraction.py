
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

# Sammenligninger

def test_equal_and_not_equal():
    assert Fraction(1, 2) == Fraction(2, 4)
    assert Fraction(1, 2) != Fraction(1, 3)


def test_ordering():
    a, b = Fraction(1, 3), Fraction(1, 2)

    assert a < b and a <= b and b > a and b >= a
    assert Fraction(1, 2) <= Fraction(2, 4)
    assert Fraction(1, 2) >= Fraction(2, 4)
    assert not (b < a) and not (a > b)
    assert Fraction(-1, 2) < Fraction(1, 3)


def test_comparison_with_other_types():
    assert Fraction(1, 2).__eq__(0.5) is NotImplemented
    assert Fraction(1, 2).__lt__(1) is NotImplemented

    with pytest.raises(TypeError):
        Fraction(1, 2) < 1

# Aritmetikk

def test_add():
    assert Fraction(1, 2) + Fraction(1, 3) == Fraction(5, 6)


def test_sub():
    assert Fraction(1, 2) - Fraction(1, 3) == Fraction(1, 6)
    assert Fraction(1, 3) - Fraction(1, 2) == Fraction(-1, 6)


def test_mul():
    assert Fraction(2, 3) * Fraction(3, 4) == Fraction(1, 2)


def test_div():
    assert Fraction(1, 2) / Fraction(1, 4) == Fraction(2)
    assert Fraction(1, 2) / Fraction(-1, 4) == Fraction(-2)


def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        Fraction(1, 2) / Fraction(0, 5)


def test_arithmetic_with_other_types():
    with pytest.raises(TypeError):
        Fraction(1, 2) + 1