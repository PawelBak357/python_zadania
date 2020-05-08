def srednia(a: list) -> float:
    """
    Funkcja zwraca średnią z elementów listy wejściowej
    :param a: lista elemetów wejściowych
    :return: średnia elementów listy
    """
    sum = 0
    for x in a:
        sum += x
    sred = sum / len(a)
    return sred

lista_liczb = [10, 20, 30, 40, 50]
print(srednia(lista_liczb))

#######################################

def max(a: list) -> float:
    """
    Funkcja zwraca maksimum z elementów listy wejściowej
    :param a: lista elemetów wejściowych
    :return: maksimum z elementów listy
    """
    maks = None
    for x in a:
        if maks is None or x > maks:
            maks = x
    return maks

lista_liczb = [10, 20, 60, 40, 50]
print(max(lista_liczb))


def roznica_min_max(a: list) -> float:
    """
    Funkcja zwraca różnicę między minimum a maksimum elementów listy wejściowej
    :param a: lista elemetów wejściowych
    :return: różnica między minimum a maksimum
    """
    if len(a) == 0:
        return 0
    else:
        maks = None
        min = None
        for x in a:
            if maks is None or x > maks:
                maks = x
            if min is None or x < min:
                min = x
    return maks - min

lista_liczb = [10, 20, 60, 40, 50]
print(roznica_min_max(lista_liczb))

################################################

def pierwsza_wieksza(liczby: list, x: float) -> float:
    """
    Zwraca pierwszą znalezioną na liście liczbę, która jest większa
    :param liczby: lista wejściowa
    :param x:
    :return:
    """
    for a in liczby:
        if a > x:
            return a
    return x

print(pierwsza_wieksza(lista_liczb, 100))

##################################################

def suma_wiekszych(liczby: list, x: int) -> int:
    """
    zwraca (`return`) sumę liczb z listy `liczby`, które są większe niż `x
    :param liczby: lista liczb
    :param x: liczba
    :return: suma większyc
    """
    suma = 0
    for a in liczby:
        if a > x:
            suma += a
    return suma
print('$' * 30)
print(suma_wiekszych(lista_liczb, 15))
print('$' * 30)


##################################################

def ile_wiekszych(liczby: list, x: float) -> float:
    """
    Zwraca pierwszą znalezioną na liście liczbę, która jest większa
    :param liczby: lista wejściowa
    :param x:
    :return:
    """
    i = 0
    for a in liczby:
        if a > x:
            i += 1
    return i

print(ile_wiekszych(lista_liczb, 10))


######################################################

def wypisz_podzielne(liczby: list, x: int) -> list:
    """
    Zwraca listę liczb podzielnych
    :param liczby: lista wejściowa
    :param x: dzielnik
    :return: lista podzielnych
    """
    lista_podzielnych = []
    for a in liczby:
        if a % x == 0:
            list.append(lista_podzielnych, a)
    return print(lista_podzielnych)

wypisz_podzielne(lista_liczb, 20)


########################################################

def pierwsza_podzielna(liczby: list, x: int) -> int:
    """
    Zwraca pierwszą podzielną przez x
    :param liczby: lista
    :param x: liczba
    :return: pierwsza podzielna
    """
    for a in liczby:
        if a % x == 0:
            return a
    return None
print()
print(pierwsza_podzielna(lista_liczb, 20))
print(pierwsza_podzielna(lista_liczb, 100))


###########################################################


def znajdz_wspolny(liczby1: list, liczby2: list) -> list:
    """
    zwraca element (liczbę), który występuje zarówno w liście `liczby1`, jak i `liczby2`; zwraca `None`, jeśli takiego elementu nie ma
    :param liczby1: lista 1
    :param liczby2: lista 2
    :return: wspólne elementy
    """
    wspolne = []
    for a in liczby1:
        for b in liczby2:
            if a == b:
                list.append(wspolne, a)
    return wspolne

lista_liczb = [10, 20, 60, 40, 50]
lista_liczb2 = [15, 25, 60, 45, 50]

print(znajdz_wspolny(lista_liczb, lista_liczb2))