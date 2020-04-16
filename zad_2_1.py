from random import randint
a = randint(0, 99)
b = randint(0, 99)
wynik = a + b

while True:
    print(f"Wylosowane liczby to {a} i {b}")
    odp = int(input("Ile wynosi suma tych liczb? "))

    if odp == wynik:
        print("Dobry wynik")
        break
    else:
        print("Zły wynik!")
        continue

