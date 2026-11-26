
"""pytest-tester for Temperature."""

import pytest
from temperature import Temperature


# 1. Initialization

def test_default_unit_is_celsius():
    assert Temperature(25).unit == "C"


@pytest.mark.parametrize("unit", ["c", "C", "f", "F", "k", "K"])
def test_units_case_insensitive(unit):
    assert Temperature(100, unit).unit == unit.upper()


def test_read_only_attributes():
    t = Temperature(25, "C")

    with pytest.raises(AttributeError):
        t.value = 30

    with pytest.raises(AttributeError):
        t.unit = "K"


# 2. Validation

@pytest.mark.parametrize("unit", ["X", "", "celsius", None, 5])
def test_invalid_unit(unit):
    with pytest.raises(ValueError):
        Temperature(10, unit)


@pytest.mark.parametrize("value, unit", [(-273.16, "C"), (-459.68, "F"), (-0.01, "K")])
def test_below_absolute_zero(value, unit):
    with pytest.raises(ValueError):
        Temperature(value, unit)


@pytest.mark.parametrize("value, unit", [(-273.15, "C"), (-459.67, "F"), (0, "K")])
def test_absolute_zero_allowed(value, unit):
    assert Temperature(value, unit).to_kelvin() == pytest.approx(0, abs=1e-9)


def test_invalid_target_unit():
    with pytest.raises(ValueError):
        Temperature(0, "C").convert_to("X")


# 3. Conversions: (C, F, K)

REFERENCE_POINTS = [
    (-273.15, -459.67, 0.0),
    (-40.0, -40.0, 233.15),
    (0.0, 32.0, 273.15),
    (37.0, 98.6, 310.15),
    (100.0, 212.0, 373.15),
]


@pytest.mark.parametrize("c, f, k", REFERENCE_POINTS)
def test_conversions_from_celsius(c, f, k):
    t = Temperature(c, "C")

    assert t.to_celsius() == pytest.approx(c)
    assert t.to_fahrenheit() == pytest.approx(f)
    assert t.to_kelvin() == pytest.approx(k)


@pytest.mark.parametrize("c, f, k", REFERENCE_POINTS)
def test_conversions_from_fahrenheit(c, f, k):
    t = Temperature(f, "F")

    assert t.to_celsius() == pytest.approx(c)
    assert t.to_kelvin() == pytest.approx(k)


@pytest.mark.parametrize("c, f, k", REFERENCE_POINTS)
def test_conversions_from_kelvin(c, f, k):
    t = Temperature(k, "K")

    assert t.to_celsius() == pytest.approx(c)
    assert t.to_fahrenheit() == pytest.approx(f)


def test_convert_to_returns_new_instance():
    t = Temperature(100, "C")
    result = t.convert_to("f")

    assert isinstance(result, Temperature)
    assert result.unit == "F"
    assert result.value == pytest.approx(212)
    assert t.unit == "C"  # original uendret


# 4. Round-trip

@pytest.mark.parametrize("c", [-273.15, -40, 0, 37, 100, 1234.5])
def test_round_trip(c):
    original = Temperature(c, "C")

    back = original.convert_to("F").convert_to("K").convert_to("C")

    assert back.unit == "C"
    assert back.value == pytest.approx(c)
    assert back == original


# 5. Comparisons

def test_equality_across_units():
    assert Temperature(0, "C") == Temperature(32, "F")
    assert Temperature(0, "C") == Temperature(273.15, "K")
    assert Temperature(-40, "C") == Temperature(-40, "F")


def test_inequality():
    assert Temperature(0, "C") != Temperature(33, "F")
    assert not (Temperature(0, "C") != Temperature(32, "F"))


def test_ordering_mixed_units():
    cold = Temperature(0, "C")
    warm = Temperature(100, "F")
    hot = Temperature(400, "K")

    assert cold < warm < hot
    assert hot > warm > cold
    assert cold <= Temperature(32, "F")
    assert cold >= Temperature(273.15, "K")
    assert not (warm < cold)
    assert not (cold > warm)


def test_tolerance():
    assert Temperature(0, "C") == Temperature(0 + 1e-10, "C")
    assert Temperature(0, "C") != Temperature(0 + 1e-6, "C")


def test_comparison_with_other_types():
    t = Temperature(0, "C")

    assert t.__eq__(5) is NotImplemented
    assert t.__ne__(5) is NotImplemented
    assert t.__lt__(5) is NotImplemented
    assert t.__le__(5) is NotImplemented
    assert t.__gt__(5) is NotImplemented
    assert t.__ge__(5) is NotImplemented

    assert (t == 5) is False

    with pytest.raises(TypeError):
        t < 5


# 6. Formatting

def test_str():
    assert str(Temperature(25, "C")) == "25.00 °C"
    assert str(Temperature(98.6, "f")) == "98.60 °F"
    assert str(Temperature(0, "K")) == "0.00 °K"


def test_repr():
    assert repr(Temperature(25, "C")) == "Temperature(25.0, 'C')"
    assert repr(Temperature(300, "k")) == "Temperature(300.0, 'K')"