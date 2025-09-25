import math
import random

liczba = [random.randint(1,100) for i in range(5)]
print("Wyosowane liczby to:")
for l in liczba:
    print("-",l)
print()

for liczba in liczba:
    print(f"Pierwiastek z {liczba} = {math.sqrt(liczba)}")