
"""Modul for Fraction-klassen (Oppgave 2)."""

from math import gcd


class Fraction:
    """Brøk med heltallig teller og strengt positiv nevner."""

    def __init__(self, numerator, denominator=1):
        if isinstance(numerator, bool) or isinstance(denominator, bool) \
                or not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Numerator and denominator must be integers.")

        if denominator <= 0:
            raise ValueError("Denominator must be strictly positive (> 0).")

        g = gcd(numerator, denominator)  # forkorter brøken

        self._numerator = numerator // g
        self._denominator = denominator // g

    @property
    def numerator(self):
        return self._numerator

    @property
    def denominator(self):
        return self._denominator

    # --- strengrepresentasjoner ---

    def __repr__(self):
        return f"Fraction({self._numerator}, {self._denominator})"

    def __str__(self):
        if self._denominator == 1:
            return str(self._numerator)

        return f"{self._numerator}/{self._denominator}"
