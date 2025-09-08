dni_tygodnia = ["Poniedzialek","Wtorek","Sroda","Czwartek","Piatke","Sobota","Niedziela"]

dzien = int(input("Podaj numer dnia tygodnia "))

if 1 <= dzien <= 7 :
    print(dni_tygodnia[dzien-1])
else:
    print("Podales zly numer:")