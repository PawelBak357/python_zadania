towar = input("Co chcesz kupić? ")
cena = float(input("Podaj cenę towaru: "))
ilosc = float(input("Podaj ilość towaru: "))

wartosc = cena * ilosc
print(f"Za {towar}, które chcesz kupić, zapłacisz {wartosc:.2f} zł.")