def kilometry_na_mile(a: float) -> float:
    """
    Przelicza kilometry na mile
    :param a: odległość w kilometrach
    :return: odległość w milach
    """
    return a*0.621371

def test_basic():
    assert kilometry_na_mile(1) == 0.621371

print("Program przelicza odległość podaną w kilometrach na mile")
a = float(input("Podaj odległość w kilometrach: "))
print(f"Ta odległość to {kilometry_na_mile(a):.2f} mil.")


################################################

def mile_na_kilometry(a: float) -> float:
    """
    Przelicza mile na kilometry
    :param a: odległość w milach
    :return: odległość w kilometrach
    """
    return a*1.60934

def test_basic():
    assert kilometry_na_mile(1) == 1.60934