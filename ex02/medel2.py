# coding: latin1
# Det h�r programmet fr�gar f�rst efter antalet tal.
# D�refter fr�gar det efter alla talen, l�ser in och ber�knar medel.

antal = int(input("Hur manga tal har du? "))
sum = 0

for i in range(antal):
    x = float(input("N�sta tal: "))
    sum += (x)

print("Medelv�rdet av dina",antal,"tal blev", round(sum/antal,2))


