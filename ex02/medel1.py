# coding: latin1
# H�r skriver man in sina tal och avslutar med enter utan tal f�re.
# Programmet r�knar hur m�nga tal som skrivits in.

print("Skriv dina tal, avsluta med enter (utan tal fore)")
sum = 0
antal = 0
while True:
    x = input("N�sta tal:")
    if x == "":
        break
    sum += float(x)
    antal += 1

print("Medelv�rdet av dina",antal,"tal blev", round(sum/antal,2))


