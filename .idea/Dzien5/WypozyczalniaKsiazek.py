biblioteka = {}

for i in range(100):
   print("----- Wypozyczalnia Ksiazek -----")
   print("1. Dodaj Ksiazje ")
   print("2. Wypozycz ksiazke")
   print("3. Oddaj ksiazke")
   print("4. Sprawdz status ksiazki")
   print("5. Pokaz wszystkie ksiazki")
   print("6. Zakoncz")



   ksiazka = input("Wybierz jedna z powyszych opcji: ")

   if ksiazka == "1":
        tytul = input("Podaj tytul ksiazki ktora chcesz dodac :")
        if tytul in biblioteka:
            print("Ksiazka juz istnieje !")
        else:
            biblioteka[tytul] = True
        print("Ksiazka dodana")
   elif ksiazka == "2":
       tytul = input("Podaj tytul ksiazki do wypozyczenia: ")
       if tytul in biblioteka and biblioteka[tytul] == True:
           biblioteka[tytul] == False
           print("Gratulacje ,Ksiazka zostala wypozycona !!!")
       else:
           print("Ksiazka nie dostepna badz nie istnieje !")
   elif ksiazka == "3":
       tytul = input("Podaj nazwe ksiazki ktora chcesz oddac: ")
       if tytul in biblioteka and biblioteka[tytul] == False:
           biblioteka[tytul] == True
           print("Ksiazka zostala oddana")
       else:
           print("Nie mozna oddac tej ksiazki !")
   elif ksiazka == "4":
       tytul = input("Podaj  tytul ksiazki: ")
       if tytul in biblioteka:
           if biblioteka[tytul]:
               print("Ksiazka jest dostepna")
           else:
               print("Brak ksiazki w bazie")

   elif ksiazka == "5":
       print("Lista ksiazek w bibliotece: ")
       for tytul , status in biblioteka.items():
           print(f"{tytul} - {"Dostepna" if status else "Wypozyczona"}")
   elif ksiazka =="6":
       break
else:
    print("Niewlasciwy wybor")

