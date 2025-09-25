def powitanie(imie, jezyk="pl"):
    if jezyk == "pl":
        return f"Czesc, {imie}!"
    elif jezyk == "en":
        return f"Hallo, {imie}!"
    else:
        return f"Nieznany jezyk dla {imie}"
print(powitanie("Marcin"))
print(powitanie("Magda","en"))
print(powitanie("Jan","de"))