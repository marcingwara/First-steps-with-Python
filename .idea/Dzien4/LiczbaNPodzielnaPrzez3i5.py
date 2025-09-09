N = int(input("Podaj liczbe N: "))

suma = 0

for i in range(1, N+1): # od 1 do N
    if i % 3 ==0 and i % 5 == 0:
        suma += i
print(f"Suma liczb podzielnych przez 3 i 5 w zakresie 1-{N} to: {suma}")