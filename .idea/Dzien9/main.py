import calculator

while True:
    print("===Kalkulator===")
    print(" 1: Dodawanie")
    print(" 2: Odejmowanie")
    print(" 3: Mnozenie")
    print(" 4: Dzielenie")
    print(" 5: Zakoncz")

    dzialanie = int(input("Wybierz dzialanie (1-5):"))

    if dzialanie == 5:
        print("Do zobaczenie!")
        break

    elif dzialanie in [1,2,3,4]:
        a = float(input("Podaj pierwsza liczbe: "))
        b = float(input("Podaj druga liczbe: "))

        if dzialanie == 1:
            print("Wynik dodawania to: ", calculator.dodaj(a,b))
        elif dzialanie == 2:
            print("Wynik odejmowania to:", calculator.odejmowanie(a,b))
        elif dzialanie == 3:
            print("Wynik mnozenia to: ", calculator.mnozenie(a,b))
        elif dzialanie == 4:
            print("Wynik dzielenia to: ", calculator.dzielenie(a,b))
    else:
        print("Niewlasciwe dzialanie!!, sprobij jeszcze raz !!" )
