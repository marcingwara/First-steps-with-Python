a = float ( input("Podaj liczbe: "))
b = float(input("Podaj druga liczbe: "))

dzialanie = input("Wybierz dzialanie: (+, -, *, /): ")

if dzialanie == "+":
    wynik = a + b
elif dzialanie == "-":
    wynik = a - b
elif dzialanie == "*":
    wynik = a * b
elif dzialanie == "/":
    if b != 0:
       wynik = a / b
    else:
        wynik = " Nie dzielimy przez 0"
else:
    wynik = "Nie znane dzialanie"

print("Wynik", wynik)


