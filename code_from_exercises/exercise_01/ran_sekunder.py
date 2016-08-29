#!/usr/bin/env python3

"""
2. Pythonkramaren, uppgift 24: Skriv ett program som frågar efter ett antal
sekunder och skriver ut hur många dagar, timmar, minuter och sekunder det är.
Lösning: [sekunder.py](sekunder.py).
"""

totalt_antal_sekunder = int(input("Hur många sekunder? "))

rest_sekunder = totalt_antal_sekunder % 60
rest_minuter = (totalt_antal_sekunder // 60) % 60
rest_timmar = (totalt_antal_sekunder // (60*60)) % 24
rest_dagar = (totalt_antal_sekunder // (60*60*24))

print("Det blir {} dagar, {} timmar, {} minuter och {} sekunder".format(
    rest_dagar, rest_timmar, rest_minuter, rest_sekunder))
