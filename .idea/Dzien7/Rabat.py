def rabat(cena, rabat = 10):
    cena_po_rabacie = cena -(cena*rabat/100)
    return cena_po_rabacie
print(rabat(200))
print(rabat(345,4))