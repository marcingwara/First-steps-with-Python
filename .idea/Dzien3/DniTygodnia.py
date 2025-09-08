dzien = int(input("Podaj numer dnia tygodnia od 1-7 "))


if dzien < 1 or dzien > 7:
    print("Podales zly numer dnia tygodnia. Sprobuj jeszcze raz!!!")
elif dzien == 1:
    print("Jest Poniedzialelk")
elif dzien ==2:
    print("Jest Wtorek")
elif dzien == 3:
    print("Jest Sroda")
elif dzien == 4:
    print("Mamy Czwartek")
elif dzien == 5:
    print("Mamy Piatek")
elif dzien == 6:
    print("Mamy Sobote")
else:
    print("Mamy Niedziele")