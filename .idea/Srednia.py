m = float(input("Ocena Matematyka: "))
p = float(input("Ocena Polski: "))
a = float(input("Ocena Angielski: "))
f = float(input("Ocena Fizyka: "))
h = float(input("Ocena Historia: "))
imie = "Marcin"


srednia = (m + p + a + f + h) / 5

if srednia >=3:
    print("Uczen: ", imie, " Zdal ze srednia ocen : ", srednia)
else:
    print("Uczen nie zdal !!!")