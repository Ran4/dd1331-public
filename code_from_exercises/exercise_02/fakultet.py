# coding: latin1
# Definition av funktion for fakultetsber�kning

def fakultet(n):
    prod = 1
    for k in range(2,n+1):
        prod *= k

    return prod


# Testa med n�gra olika anrop
# Python overg�r automatiskt till att anv�nda godtyckligt
# l�nga heltal n�r det beh�vs. Det finns f�rst�s en �vre 
# gr�ns f�r talens storlek. Talen m�ste f� plats i minnet.

print('0! =', fakultet(0))
print('1! =', fakultet(1))
print('5! =', fakultet(5))
print('7! =', fakultet(7))
print('17! =', fakultet(17))
print('37! =', fakultet(37))
