def suma(a: list) -> int:
    """
    Funkcja zwraca sumę jej elementów
    :param a: lista wejściowa
    :return: suma elemntów listy
    """
    sum = 0
    for x in a:
        sum += x
    return sum

def test_basic():
    assert suma([10, 20, 30, 40, 50]) == 150

lista_liczb = [10, 20, 30, 40, 50]
print(suma(lista_liczb))