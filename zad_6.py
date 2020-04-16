while True:
    wiek = float(input("Podaj wiek: "))
    l_bil = int(input("Podaj liczbę biletów: "))

    if wiek < 0 or l_bil < 1:
        print("Błąd. Jeszcze raz. \n")
        continue
    else:
        if wiek <7:
            cena = 0
            break
        elif wiek >= 7 and wiek < 18:
            cena = l_bil * 2.28
            break
        elif wiek >=18 and wiek < 65:
            cena = l_bil * 3.8
            break
        elif wiek >= 65:
            cena = l_bil * 1.9
            break

print(f"Zapłacisz {cena:.2f} zł.")

