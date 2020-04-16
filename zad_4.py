wiek = int(input("Podaj swój wiek: "))
l_nocy = int(input("Podaj liczbę nocy, które chcesz tu spędzić: "))
if wiek < 18:
    cena = l_nocy * 100
else:
    if l_nocy == 1:
        cena = 200
    elif l_nocy > 1 and l_nocy < 5:
        cena = l_nocy * 180
    elif l_nocy >= 5:
        cena = l_nocy * 150

if wiek >= 65:
    cena = cena * 0.9

print(f"Za {l_nocy} nocy osoba, która ma {wiek} lat zapłaci {cena} zł.")