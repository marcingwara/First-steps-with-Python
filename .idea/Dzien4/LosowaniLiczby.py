import random

liczba = random.randint(1,101)

zgadniecie = False

while not zgadniecie:
    N = int(input("Podaj liczbe od 1 do 100: "))

    if N < liczba:
        print("Podales za mala liczbe, sprobuj jeszcze raz ")
    elif N > liczba:
        print("Podales za duza liczbe, sprobuj jeszcze raz ")
    else:
        print("Brawo TRAFILES !!!")
        zgadniecie = True
