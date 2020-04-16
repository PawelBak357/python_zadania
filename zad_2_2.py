ll = int(input("Podaj liczbę linii choinki: "))

for i in range(1, ll):
    z = (ll - i)*2
    print("  "*z, end="")
    print("*   "*(i*2-1))


