print("Podawaj liczby i zatwierdzaj enterem. Jeśli chcesz obliczyć, podaj o")
lp = 0
suma = 0
srednia = 0
min = None
max = None

while True:
    dane = (input("Podaj liczbę: "))
    if dane == "o":
        break
    else:
        liczba = float(dane)
        lp += 1
        suma += liczba
        srednia = suma / lp
        if min is None or liczba < min:
            min = liczba
        if max is None or liczba > max:
            max = liczba
        continue

print(f"Podano {lp} liczb")
print(f"Suma wynosi {suma}")
print(f"Średnia wynosi {srednia:.2f}")
print(f"Minimum wynosi {min}")
print(f"Maksimum wynosi {max}")