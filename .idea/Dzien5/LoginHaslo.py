user = {
    "Kajtek" : 12345,
    "Majtek" : "me456",
    "User34" : "mel45"
}
login = input("Podaj nazwe uzytkownika: ")

if login in user:
    print(f"Uzytkownik o Loginie {login} istnieje")
else:
    print(f"Uzytkownik {login} nie istnieje")