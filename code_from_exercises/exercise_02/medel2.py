# coding: latin1
# Det här programmet frågar först efter antalet tal.
# Därefter frågar det efter alla talen, läser in och beräknar medel.

antal = int(input("Hur manga tal har du? "))
sum = 0

for i in range(antal):
    x = float(input("Nästa tal: "))
    sum += (x)

print("Medelvärdet av dina",antal,"tal blev", round(sum/antal,2))


