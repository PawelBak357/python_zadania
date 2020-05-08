def liczba_dni_miesiaca(a: str) -> int:
    """
    Podaje liczbę dni dla podanej nazwy miesiąca
    :param a: nazwa miesiąca
    :return: liczba dni
    """
    x_31 = ['styczen', 'marzec', 'maj', 'lipiec', 'sierpien', 'pazdziernik', 'grudzien']
    x_30 = ['kwiecien', 'czerwiec', 'wrzesien', 'listopad']
    x_l = ['luty']
    if a in x_31:
        return 31
    elif a in x_30:
        return 30
    elif a in x_l:
        return liczba_dni_lutego(int(input("Podaj rok: ")))
    else:
        raise ValueError("Zła nazwa!")

def liczba_dni_lutego(a: int) -> int:
    """
    Sprawdza, czy rok jest przestępny czy nie i zwraca liczbę dni lutego
    :param a: rok
    :return: liczba dni lutego
    """
    if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
        return 29
    else:
        return 28

miesiac = input("Podaj nazwę miesiąca: ")
print(liczba_dni_miesiaca(miesiac))

