lista_zakup = []



print("1: Wyswietl liste")
print("2: Usun produkt z listy")
print("3: Wyczysc liste")
print("4: Zakoncz! ")



for i in range(10):
    produkt = input("Dodaj produkt do listy: ")
    if produkt == "1":
        print("---Twoja lista zakup---")
        for p in lista_zakup:
            print("-",p)
    elif produkt == "2":
        print(f"Ktory produkt chcesz usunuc z listy ? ")
        for p in lista_zakup:
            print("-",p)
        do_usunecie = input("Wpisz produkt do usuniecia: ")
        lista_zakup.remove(do_usunecie)
        print(f"produkt {do_usunecie} zostal usuniety! ")
    elif produkt == "3":
        lista_zakup.clear()
        print("Lista zostala wyczyszczona")
    elif produkt == "4":
        break
    elif produkt not in lista_zakup:
            lista_zakup.append(produkt)
            print(f"{produkt} zostal dodany ")
    else:
            print(f"Produkt {produkt} juz instnieje na liscie ! ")
