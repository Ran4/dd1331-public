#coding:latin1
talet = int(input("Skriv ditt heltal > 0: "))

siffersumma = 0
while talet > 0:
    siffra = talet % 10
    siffersumma += siffra
    talet //= 10

print("Siffersumman är ", siffersumma)
