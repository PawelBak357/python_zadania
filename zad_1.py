#CZĘŚĆ 1
cena = float(input("Ile kosztuje kilogram ziemniaków? \n"))
wartosc = cena * 5
print(f"5 kg ziemniaków kosztuje {wartosc} zł.")

#CZĘŚĆ 2
cena = float(input("Ile kosztuje kilogram ziemniaków? \n"))
ilosc = float(input("Ile kilogramów chcesz kupić? \n"))
wartosc = cena * ilosc
print(f"Za {ilosc} kg ziemniaków musisz zapłacić {wartosc} zł.")

#CZĘŚĆ 3
cena_z = float(input("Ile kosztuje kilogram ziemniaków? \n"))
ilosc_z = float(input("Ile kilogramów chcesz kupić? \n"))
wartosc_z = cena_z * ilosc_z
cena_b = float(input("Ile kosztuje kilogram bananów? \n"))
ilosc_b = float(input("Ile kilogramów chcesz kupić? \n"))
wartosc_b = cena_b * ilosc_b
razem = wartosc_z + wartosc_b
print(f"Za {ilosc_z} kg ziemniaków i {ilosc_b} kg bananów musisz zapłacić {razem} zł.")
if wartosc_b == wartosc_z:
    print("Za banany i ziemniaki zapłacisz tyle samo")
else:
    if wartosc_z > wartosc_b:
        print("Więcej zapłacisz za ziemniaki.")
    else:
        print("Więcej zapłacisz za banany.")
