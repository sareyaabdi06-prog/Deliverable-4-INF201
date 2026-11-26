
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

    # --- sammenligninger ---

    def _key(self, other):
        """Returnerer (a, b) som kan sammenlignes ved kryssmultiplikasjon."""
        return (self._numerator * other._denominator,
                other._numerator * self._denominator)

    def __eq__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented

        return (self._numerator == other._numerator
                and self._denominator == other._denominator)

    def __ne__(self, other):
        result = self.__eq__(other)
        return result if result is NotImplemented else not result

    def __lt__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented

        a, b = self._key(other)
        return a < b

    def __le__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented

        a, b = self._key(other)
        return a <= b

    def __gt__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented

        a, b = self._key(other)
        return a > b

    def __ge__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented

        a, b = self._key(other)
        return a >= b


    # --- sammenligninger ---

    def _key(self, other):
        """Returnerer (a, b) som kan sammenlignes ved kryssmultiplikasjon."""
        return (self._numerator * other._denominator,
                other._numerator * self._denominator)

    def __eq__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented

        return (self._numerator == other._numerator
                and self._denominator == other._denominator)

    def __ne__(self, other):
        result = self.__eq__(other)
        return result if result is NotImplemented else not result

    def __lt__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented

        a, b = self._key(other)
        return a < b

    def __le__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented

        a, b = self._key(other)
        return a <= b

    def __gt__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented

        a, b = self._key(other)
        return a > b

    def __ge__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented

        a, b = self._key(other)
        return a >= b