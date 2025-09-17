import random

liczba = random.randint(1, 101)

zgadnienie = False

while not zgadnienie:
    N = int(input("Podaj liczbe od 1 do 100: "))
    if N < liczba:
        print("Podales za mala liczbe, spruboj jeszcze raz")
    elif N > liczba:
        print("Podales za duza liczbe, spruboj jeszcze raz")
    else:
        print("Brawo Trafiles !!!!")
        zgadnienie = True