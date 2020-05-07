def stopy_na_metry(a:int) -> float:
    """
    Przelicznik stóp na metry
    :param a: długość w stopach
    :return: długość w metrach
    """
    return a*0.3048

################################

def max(a:float, b:float) -> float:
    """
    Zwraca większą z podanych liczb
    :param a: liczba 1
    :param b: liczba 2
    :return: większa liczba
    """
    if a > b:
        return a
    else:
        return b

####################################

def srednia(a: float, b: float) -> float:
    """
    Zwraca średnią z liczb
    :param a: liczba 1
    :param b: liczba 2
    :return: średnia z liczb
    """
    return (a + b) / 2

def test_basic():
    assert srednia(2, 4) == 3
    assert srednia(4, 8) == 6

######################################

def pole_kola(a: float) -> float:
    """
    Zwraca pole koła z podango promienia
    :param a: promień
    :return: pole koła
    """
    from math import pi
    return a * a * pi

#####################################
'''
def bmi(a: float, b: float) -> float:
    """
    Oblicza współczynnik BMI
    :param a: wzrost [m]
    :param b: waga [kg]
    :return: BMI [-]
    """
    return b / (a ** 2)

print("Program oblicza współczynnik BMI.")
wzrost = float(input("Podaj swój wzrost [m]: "))
waga = float(input("Podaj swoją wagę [kg]: "))
bmi = bmi(wzrost, waga)
print(f"Twój współczynnik BMI wynosi: {bmi:.2f}")

'''
##########################################

