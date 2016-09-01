# coding: latin1

# Vi antar att personnumret skrivs pa formen yymmdd-ssss, 
# t.ex. 920508-0329 
# Om tionde tecknet (index 9) är en jämn siffra så är det
# ett kvinnligt personnummer, annars ett manligt.
# dig % 2 betyder resten då dig divideras med 2
# Denna rest är 0 for jämna tal
# Inga som helst felkontroller görs av personnumret
# Funktionen returnerar True för kvinna, False for man

def isFemale(pnr):
    dig = int(pnr[9])
    return dig % 2 == 0


# Testanrop
print('Mamma',isFemale('yymmdd-0022'))
print('Pappa',isFemale('yymmdd-1458'))
print('Lillasyster',isFemale('yymmdd-0127'))
print('Lillebror',isFemale('yymmdd-0110'))
print('Storebror',isFemale('yymmdd-0312'))
    
