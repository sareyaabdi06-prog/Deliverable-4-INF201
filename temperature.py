
# Task 1: Temperatures

"""Modul for Temperature-klassen (Oppgave 1)."""

TOLERANCE = 1e-9  # toleranse for sammenligning av flyttall

_VALID_UNITS = ("C", "F", "K")


class Temperature:
    """Temperatur i Celsius (C), Fahrenheit (F) eller Kelvin (K)."""

    def __init__(self, value, unit="C"):
        unit = self._validate_unit(unit)

        self._value = float(value)
        self._unit = unit

        # Sjekk absolutt nullpunkt (0 K) ved å regne om til Kelvin
        if self.to_kelvin() < -TOLERANCE:
            raise ValueError("Temperature cannot be below absolute zero (0 K).")