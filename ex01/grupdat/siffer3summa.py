#coding:latin
talet = int(input("Skriv ditt tresiffriga tal: "))
if talet >= 1000:
    print("För stort!")
else:
    siffersumma = 0
    # Första siffran (högraste)
    siffra = talet % 10
    siffersumma += siffra
    talet //= 10
    # Andra siffran
    siffra = talet % 10
    siffersumma += siffra
    talet //= 10
    # Tredje siffran
    siffra = talet % 10
    siffersumma += siffra
    print("Siffersumman är ", siffersumma)
