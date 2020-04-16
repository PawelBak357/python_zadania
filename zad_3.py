wzrost = float(input("Podaj swój wzrost [cm]: "))
waga = float(input("Podaj swoją wagę [kg]: "))
bmi = waga / ((wzrost/100)**2)
print(f"Twoje BMI wynosi {bmi:.2f}.")
if bmi < 18.5:
    print("Masz niedowagę.")
if bmi >= 18.5 and bmi <=24.9:
    print("Masz prawidłową wagę.")
if bmi > 24.9 and bmi <=29.9:
    print("Masz nadwagę.")
if bmi > 29.9:
    print("Masz otyłość.")