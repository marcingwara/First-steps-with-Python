waga = float(input("Podaj wage: "))
wzrost = float(input("Podaj wzrost: "))

bmi = waga /(wzrost * wzrost)

print("Twoje BMI wnosi: ", bmi)

if bmi < 18.5:
    print("Niedowaga ")
elif 18.5 <= bmi < 25:
    print("Twoja waga jest w normir ")
elif 25 <= bmi <30:
    print("Nadwage ")
else:
    print("Masz otylosc ")
