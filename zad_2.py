dzien_oddania = int(input("Którego dnia oddałeś buty? \n Pon = 1 \n Wt = 2 \n Śr = 3 \n Czw = 4 \n Pt = 5 \n Sob = 6 \n Nd = 7 \n"))
czas_realizacji = int(input("Ile trwa naprawa? \n"))
dzien_odbioru = (dzien_oddania + czas_realizacji) % 7
tydzien = ("poniedzialek", "wtorek", "srode", "cztartek", "piatek", "sobote", "niedziele")
print(f"Buty będą do odbioru w {tydzien[dzien_odbioru-1]}")
