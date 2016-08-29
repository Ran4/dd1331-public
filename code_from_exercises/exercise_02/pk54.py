# coding: latin1

# Den har l�sningen anv�nder endast s�dant som vi g�tt
# igenom i kursen f�re �vningen
# Funktionen har en textstr�ng som parameter.
# Vi antar att det finns (minst) ett blanktecken i texten
# Funktionen returnerar en text som byggs upp av
# texten efter blanktecknet + ett blanktecken + texten f�re blanktecknet
# T.ex. "Agaton Sax" -> "Sax Agaton"
# Inga felkontroller g�rs

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


