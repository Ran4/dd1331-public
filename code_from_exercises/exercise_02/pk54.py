# coding: latin1

# Den har lösningen använder endast sådant som vi gått
# igenom i kursen före övningen
# Funktionen har en textsträng som parameter.
# Vi antar att det finns (minst) ett blanktecken i texten
# Funktionen returnerar en text som byggs upp av
# texten efter blanktecknet + ett blanktecken + texten före blanktecknet
# T.ex. "Agaton Sax" -> "Sax Agaton"
# Inga felkontroller görs

def bytOrdfoljd(s):
    k = 0
    for i in range(len(s)):
        if s[i] == ' ':
            k = i
            break

    return s[i+1:] + ' ' + s[:i]


# Testanrop
print()
print(bytOrdfoljd('Agaton Sax'))
print(bytOrdfoljd('Jiarong Li'))


