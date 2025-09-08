wiek = int(input("Podaj ile masz lat: "))

if wiek < 0 or wiek > 120:
    print("Nie prawidlowy wiek !!! Spruboj jeszcze raz")
elif wiek < 18:
    print(f"Masz {wiek} lat przysluguje ci bilet ulgowy")
elif 18 <= wiek <=65:
    print(f"Masz {wiek} lat przysluguje ci bilet normalny")
else:
    print(f"Masz {wiek} lat przysluguje ci bilet seniora")
