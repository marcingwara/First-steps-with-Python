def dodawanie(a, b):
    return a + b
def pole(a,b):
    return a*b
def srednia( a,b,c):
    wynik = a+b+c
    return wynik /3

for i in range(10):
    print("---MENU---")
    print("1: Dodawanie dwuch liczb")
    print("2: Obliczanie pola")
    print("3: Obliczanie sredniej trzech liczb")
    print("4: Zakoncz")

    dzialanie = int (input("Wybierz rodzaj działania od 1-4: "))

    if dzialanie == 1:
        a = float(input("Podaj pierwsza liczbe: "))
        b = float(input("Podaj druga liczbe: "))
        print("Suma liczb to: ", dodawanie(a,b))
        print()

    elif dzialanie == 2:

        a = float(input("Podaj dlugosc pierwszego boku prostokąta: "))
        b = float(input("Podaj dlugosc drugiego boku prostokąta: "))
        print("Pole prostokąta to: ", pole(a,b))
        print()

    elif dzialanie == 3:
        a = float(input("Podaj pierwsza liczbe: "))
        b = float(input("Podaj druga liczbe: "))
        c = float(input("Podaj trzecia liczbe: "))
        print("Srednia z trzech liczb to: ", srednia(a,b,c))
        print()
    elif dzialanie == 4:
        break
    else:
        print("Nie wlasciwe dzialnie")
        print()