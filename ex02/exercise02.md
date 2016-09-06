
## Från förra veckan

Kolla in [felaktiga-program-mappen](../felaktiga_program/)

## Testdriven utveckling

Testdriven utveckling (eng. [test driven development](https://en.wikipedia.org/wiki/Test-driven_development),
"TDD") är en ganska stor gren inom mjukvaruutveckling idag, men är långt ifrån denna kurs fokus. Vi kommer därför
bara att anamma en av de mest centrala delarna inom TDD: testfunktionen.

När man skriver knepiga funktioner så är det lätt hänt att man introducerar buggar, eller att man inte tänker
på alla situationer som kan uppkomma.

Ett enkelt sätt att se om en funktion fungerar som den ska är att köra den och se att resultatet är korrekt.
Men om man testar sin funktion genom att manuellt skriva in dem i exempelvis pythontolken så är det lätt hänt
att man bara testar de enklaste fallen, och att man inte testar allt som man borde testa. Ett sätt att undvika
detta är att för varje funktion skriva en separat test-funktion, med några testfall (eng. test cases). Så fort
som du gör en ändring i din funktion så kan du köra om testfunktionen för att snabbt testa att den fungerar
som den ska.

Nedan följer ett mycket enkelt exempel på en funktion, och en testfunktion.

```python
def count_in_list(seq, value):
    """Re-implementation of seq.count(value): returns the number of times value
    is found in sequence seq.
    Example:
        count_in_list([3, 2, 3, 1], 3) # 2
    """
    num_matching_values = 0
    for element in seq:
        if element == value:
            num_matching_values += 1
    return num_matching_values

def test_count_in_list():
    assert count_in_list([], 42) == 0
    assert count_in_list([3, 2, 3, 1], 3) == 2
    assert count_in_list(["", "", " "], " ") == 1
    assert count_in_list([True, False, False, True], True) == 2
    assert count_in_list(range(1000), 47) == 1
    
test_count_in_list()
print("All tests completed!")
```

Koden använder python-nyckelordet `assert`, vilket kraschar programmet om det får ett icke-sant-liknande
värde. (Överkurs: rent tekniskt så kraschar assert faktiskt inte Python: om det assert får inte är sant så
"lyfter den ett undantag" eller på engelska "raises an exception", i det här fallet ett
AssertionError-undantag.  Om ett undantag inte fångas ("if the exception isn't caught") så kraschar python,
och visar en s.k. traceback).

## Man - manual

Om du inte vet hur ett kommando fungerar i ett unix-liknande operativsystem
(Linux eller OS X, eller i liknande miljö i windows, t.ex. i git bash) så kan man använda kommandot `man`.

Exempel: om vi har glömt vad `-a`-argumentet gör i `git commit -a`, så kan vi ta reda på det genom att öppna
en terminal och skriva in

```
man git commit
```

Vilket program som `man` öppnar manualen i varierar. På de flesta system öppnas man-sidorna i ett program som
heter `less`, som fungerar lite som `cat`, men du har möjlighet att scrolla runt med pilarna (eller j/k,
ctrl+d/u m.fl). Söka kan du göra genom att trycka på `/`, och nästa sökresultate fås genom att trycka på `n`

Mer information om man kan passande fås genom att skriva `man man`.

Värt att nämna är att beskrivningarna som ges i manualsidorna ofta är väldigt tekniska, och innehåller ofta få
eller inga exempel, så det kan vara värt att kolla in andra källor. Men för att snabbt kolla in vilken
parameter ett program tar så är det mycket användbart.

## Uppgifter:

1. Skriv ett program som beräknar antalet termer som behövs för att summan av 1/i, i = 1..N ska nå ett visst mål.
    * Lösning: ["../ex01/grupdat/ran\_antaltermer.py"]("../ex01/grupdat/ran_antaltermer.py")

2. Skriv ett program som läser in ett antal tal och beräknar deras medelvärde.
    * Lösning: [ran\_medel1.py](ran_medel1.py)

3. Skriv en funktion som beräknar n-fakultet, alltså 1*2*3*...*n. Visa anrop av
funktionen.
    * Lösning:  [ran\_fakultet.py](ran_fakultet.py)

4. Pythonkramaren 54: Byt ordning på två ord.  Från indata "Li Jiarong"
producera och skriv ut "Jiarong Li".  Från indata "Agaton Sax" producera och
skriv ut "Sax Agaton".
    * "manuell" lösning: [pk54.py](ran_pk54.py)

    * Mer pythonaktig lösning: [pk54\_pythonic.py](ran_pk54_pythonic.py)

    * Lösning på KTHs github som gjordes under övningen: [gits-15.sys.kth.se/ransin/wordswitcher](https://gits-15.sys.kth.se/ransin/wordswitcher)

5. Pythonkramaren 53: funktion som avgör från ett personnummer om ett nummer är
manligt eller kvinnligt.
    * Lösning: [pk53.py](ran_pk53.py).
    
6. Pythonkramaren 55: Från en KTH-årskursbeteckning, t.ex. "F-08", beräkna hur
många år som gått sedan personen började på KTH.
    * Lösning: [pk55.py](ran_pk55.py)
   
7. Skriv ett program som beräknar ett närmevärde till sin(x) m.h.a.
Taylorutvecklingen sin(x) = x - x^3/3! + x^5/5! -x^7/7! + x^9/9! + .....
Utnyttja att en term i serien liknar föregående term ganska mycket! Lösning:
    * [sin.py](sin.py)

8. Skriv en funktion som beräknar största gemensamma delare till två tal med
Euklides algoritm. Lösning: euklides.py. Här är en minimal lösning som
använder dubbel tilldelning:
    * Lösning: [euklidesMINI.py](euklidesMINI.py)
   
9. Beräkna (i program eller funktion) semifakultet: n*(n-2)*(n-4)*...*s där s
är 1 eller 2 beroende på om n är udda eller jämn. Det går att lösa problemet
utan att testa om n är udda eller jämn!
    * Lösning: [semifakultet.py](semifakultet.py).
