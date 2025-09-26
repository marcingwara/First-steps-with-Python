import random
from itertools import count

wyniki = []
for i in range(10):
    rzut = random.randint(1,6)
    wyniki.append(rzut)
    print("Rzut: ", rzut)
    print("Wyniki rzotow: ", wyniki)

def srednia(lista):
    return sum(lista)/len(lista)

def maksymalna(lista):
    return max(lista)

def minimum(lista):
    return min(lista)


print("---PODSUMOWANIE---")
print(f"Srednia z rzutow to: ", srednia(wyniki))
print("Najwiekszy wyrzucony to",max(wyniki))
print("Najmniejsza wyrzucona to :", min(wyniki))
print()
print("---Statystyki rzutow---")
for liczba in range(1,6+1):
    print(f"Liczba {liczba} wypadla {wyniki.count(liczba)} razy")

