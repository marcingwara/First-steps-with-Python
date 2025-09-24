def dodawanie(a, b):
    return a + b
def pole(a,b):
    return a*b
def srednia( a,b,c):
    wynik = a+b+c
    return wynik /3

while True:
    print("---MENU---")
    print("1: Dodawanie dwuch liczb")
    print("2: Obliczanie pola")
    print("3: Obliczanie sredniej trzech liczb")
    print("4: Zakoncz")
    try:
        dzialanie = int (input("Wybierz rodzaj działania od 1-4: "))
    except ValueError :
        print("To nie jest liczba, sprobuj ponownie")
        print()
        continue


    if dzialanie == 1:
        try:
            a = float(input("Podaj pierwsza liczbe: "))
            b = float(input("Podaj druga liczbe: "))
            print("Suma liczb to: ", dodawanie(a,b))
            print()
        except ValueError:
            print("Musisz podac liczbe!!!")
            print()

    elif dzialanie == 2:
        try:
            a = float(input("Podaj dlugosc pierwszego boku prostokąta: "))
            b = float(input("Podaj dlugosc drugiego boku prostokąta: "))
            print("Pole prostokąta to: ", pole(a,b))
            print()
        except ValueError:
            print("Musisz podac liczeb!!!")
            print()

    elif dzialanie == 3:
        try:
            a = float(input("Podaj pierwsza liczbe: "))
            b = float(input("Podaj druga liczbe: "))
            c = float(input("Podaj trzecia liczbe: "))
            print("Srednia z trzech liczb to: ", srednia(a,b,c))
            print()
        except ValueError:
            print("Musisz podac liczbe!!!")
            print()
    elif dzialanie == 4:
        print("Koniec programu, do zobaczenia")
        break
    else:
        print("Nie wlasciwe dzialnie")
        print()