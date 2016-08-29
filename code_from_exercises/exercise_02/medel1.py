# coding: latin1
# Här skriver man in sina tal och avslutar med enter utan tal före.
# Programmet räknar hur många tal som skrivits in.

print("Skriv dina tal, avsluta med enter (utan tal fore)")
sum = 0
antal = 0
while True:
    x = input("Nästa tal:")
    if x == "":
        break
    sum += float(x)
    antal += 1

print("Medelvärdet av dina",antal,"tal blev", round(sum/antal,2))


