#!/usr/bin/env python3
import math

"""
1. Om sidlängderna hos en triangle är a,b och c så kan triangelns yta beräknas
med hjälp av [Herons formel](http://sv.wikipedia.org/wiki/Herons_formel).

Låt s = (a+b+c)/2 och A = sqrt(s*(s-a)*(s-b)*(s-c)).

Skriv ett program som frågar efter a,b och c samt beräknar och skriver ut
triangelytan.

Låt programmet även göra kontroller av a,b,c så att de angivna värdena
verkligen kan bilda en triangel. Lösning: [heronsFormel.py](heronsFormel.py).
"""

print("Skriv in sidlängderna för din triangel: ")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a < b + c and b < c + a and c < a + b:
    s = (a + b + c) / 2

    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    print("Arean är:", area)
else:
    print("De angivna sidlängderna kan inte bilda en triangel!")
