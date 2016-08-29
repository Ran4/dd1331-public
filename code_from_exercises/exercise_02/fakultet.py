# coding: latin1
# Definition av funktion for fakultetsberäkning

def fakultet(n):
    prod = 1
    for k in range(2,n+1):
        prod *= k

    return prod


# Testa med några olika anrop
# Python overgår automatiskt till att använda godtyckligt
# långa heltal när det behövs. Det finns förstås en övre 
# gräns för talens storlek. Talen måste få plats i minnet.

print('0! =', fakultet(0))
print('1! =', fakultet(1))
print('5! =', fakultet(5))
print('7! =', fakultet(7))
print('17! =', fakultet(17))
print('37! =', fakultet(37))
