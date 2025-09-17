uzytkownicy = {
    "Marcin" : "12345",
    "Krakowiak" : "e3d3"
}
biblioteka = []

for i in range (3, 0,-1):

    login = input("Podaj nazwe uzytkownika: ")
    haslo = input("Podaj haslo: ")


    if login in uzytkownicy and uzytkownicy[login]==haslo:
        print("Login Prawidlowy:")


        while True:
            print("n---Menu---")
            print("1 .Dodaj film")
            print("2. Usun film")
            print("3. Sprawdz film")
            print("4. Pokaz wszystkie filmy")
            print("5. Wyjscie")

            wybor = input("Wybierz opcje (1-5): ")

            if wybor == "1":
                film = input("Podaj tytul filmu do dodania: ")
                if film in biblioteka:
                    print(f" Film '{film}' juz istnieje w Twojej bibliotece!")
                else:
                    biblioteka.append(film)
                    print(f"Film {film} zostal pomyslnie dodany do twojej biblioteki !")

            elif wybor == "2":
                film = input("Podaj tytul filmu do usuniecia: ")
                if film in biblioteka:
                   biblioteka.remove(film)
                   print(f"Fim '{film}' usuniety! ")
                else:
                   print("Nie ma takiego filmu")

            elif wybor == "3":
                film = input("Podaj tytul filmu do sprawdzeni:")
                if film in biblioteka:
                   print(f"Ten film{film} znajduje sie w bibliotece")
                else:
                   print(f"{film} nie znaleziono w bibliotece! ")
            elif wybor == "4":
                print("Twoja lista filmow: ", biblioteka)

            elif wybor == "5":
                print("Koniec programu")
                break
            else:
                print("Nieprawidlowy wybor, sprobuj ponownie ")

    else:
        print(f"Logowanie nie udane, sprobuj ponownie")
        print(f"Pozostala liczba prob logowania {i-1}")

else:
    print("Konto zablokowane")




