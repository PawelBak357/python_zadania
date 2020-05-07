
def pole_trojkata(a: float, b: float, c: float) -> float:
    """
    Zwraca pole trójkąta obliczone z długości boków
    :param a: długość 1 boku
    :param b: długość 2 boku
    :param c: długość 3 boku
    :return: pole trojkata
    """
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Bok nie moze byc mniejszy od 0.")
    from math import sqrt
    p = (a + b + c) / 2
    pole = sqrt(p * (p - a) * (p - b) * (p - c))
    return pole

def test_wartosci_ujemne():
    with pytest.raises(ValueError):
        pole_trojkata(-10)

print(pole_trojkata(2,3,-4))