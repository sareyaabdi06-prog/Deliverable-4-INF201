
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


    @staticmethod
    def _validate_unit(unit):
        if not isinstance(unit, str) or unit.upper() not in _VALID_UNITS:
            raise ValueError(f"Invalid unit {unit!r}. Use 'C', 'F' or 'K'.")
        return unit.upper()

    # --- read-only attributter ---

    @property
    def value(self):
        return self._value

    @property
    def unit(self):
        return self._unit

    # --- konverteringer ---

    def to_celsius(self):
        if self._unit == "C":
            return self._value

        if self._unit == "K":
            return self._value - 273.15

        return (self._value - 32) * 5 / 9  # Fahrenheit

    def to_fahrenheit(self):
        if self._unit == "F":
            return self._value

        if self._unit == "C":
            return self._value * 9 / 5 + 32

        return (self._value - 273.15) * 9 / 5 + 32  # Kelvin

    def to_kelvin(self):
        if self._unit == "K":
            return self._value

        if self._unit == "C":
            return self._value + 273.15

        return (self._value - 32) * 5 / 9 + 273.15  # Fahrenheit

    def convert_to(self, target_unit):
        """Returnerer en NY Temperature i target_unit."""
        target = self._validate_unit(target_unit)

        converters = {"C": self.to_celsius, "F": self.to_fahrenheit, "K": self.to_kelvin}

        return Temperature(converters[target](), target)

    