import math
while True:
    a = float(input("Podaj długość 1 boku: "))
    b = float(input("Podaj długość 2 boku: "))
    c = float(input("Podaj długość 3 boku: "))

    if a + b < c or a + c < b or b + c < a:
        print("Nie można utworzyć trójkąta! Zacznij jeszcze raz. \n")
        continue
    else:
        p_obw = (a + b + c) / 2
        pole = math.sqrt(p_obw * (p_obw - a) * (p_obw - b) * (p_obw - c))
        print(f"Pole trójkąta wynosi: {pole:.2f}")
        break


