# Övning 1

Begrepp att öva på:
* Inläsning, beräkning och utskrift.
* Felkontroll av indata (med if-sats).
* Repetition med while.

#### Förslag till uppgifter:

1. Om sidlängderna hos en triangle är a,b och c så kan triangelns yta beräknas
   med hjälp av [Herons formel](http://sv.wikipedia.org/wiki/Herons_formel).
   Låt s = (a+b+c)/2 och A = sqrt(s*(s-a)*(s-b)*(s-c)). Skriv ett program som
   frågar efter a,b och c samt beräknar och skriver ut triangelytan. Låt
   programmet även göra kontroller av a,b,c så att de angivna värdena verkligen
   kan bilda en triangel. Lösning: [heronsFormel.py](ran_heronsformel.py).

2. Pythonkramaren, uppgift 24: Skriv ett program som frågar efter ett antal
   sekunder och skriver ut hur många dagar, timmar, minuter och sekunder det
   är. Lösning: [sekunder.py](sekunder.py).

3. Pythonkramaren, uppgift 25: Beräkna siffersumman för ett tresiffrigt heltal.
   Siffersumman av 413 är 4 + 1 + 3 = 8. Lösning:
   [siffer3summa.py](ran_siffer3summa.py).

4. Utvidga föregående uppgift så att den beräknar siffersumman av ett hetal med
   godtyckligt antal siffror. Lösning: siffersumma.py.  a. Skriv ett program
   som summerar n st termer av serien 1/1 + 1/2 + 1/3 + 1/4 + .... Lösning:
   harmsum.py b. Skriv ett annat program som beräknar hur många termer som
   behövs för att summan av samma serie ska blir större än något visst värde.
   Lösning: [antalTermer.py](ran_antaltermer.py)
