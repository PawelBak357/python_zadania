"""Program losuje liczbę z zakresu od 0 do 999. Użytkownik ma zgadnąć tę liczbę nie widząc jej. Kiedy użytkownik poda
nieprawidłowy wynik, program podpowiada pisząc czy podana liczba była za duża, czy za mała. Gdy użytkownik poda właściwą
liczbę, program wypisuje gratulacje jednocześnie informując, w której próbie udało się zgadnąć liczbę.
​
Nawiasem mówiąc technika wyszukiwania oparta o "podpowiedzi" za dużo/za mało nazywa się bisekcją i pełni w informatyce
bardzo ważną rolę. Umiejętnie ją stosując powinno się te zagadki rozwiązywać w 9-10 próbach (bo 2^10=1024)."""

from random import randint
liczba = randint(0, 999)
i = 0
while True:
    odp = int(input("Podaj liczbę: "))
    i += 1
    if odp == liczba:
        print(f"Brawo! Zgadłeś w {i}. próbie.")
        break
    else:
        if odp < liczba:
            print("Za mała!")
            continue
        else:
            print("Za duża!")
            continue
