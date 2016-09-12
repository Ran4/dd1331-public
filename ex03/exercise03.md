## Övning 3

**Begrepp att öva på:**
* Listor och funktioner
* Textsträngar med anrop av strängmetoder
* Att tänka på listor och textsträngar som objekt
* Funktioner bör alltid kompletteras med anrop som testar att funktionen fungerar även om det inte står uttryckligen i uppgiften (testkod!)

## Uppgifter:

1. Pythonkramaren 63: 
Skriv en funktion som har en listparameter och ger True om alla element i listan är positva tal, False annars. Lösning: allapos.py.
    * Lösning: [krock.py](ran_krock.py)

2. Skriv en funktion som konstruerar en slumpmässig blandning av en lista genom att slumpa fram ett element i taget, plocka ut det ur första listan och sätta in det i en annan lista som blir funktionens resultat. Lösning: blanda.py. I den här lösningen förstörs parameterlistan eftersom listelementen successivt plockas ut ur listan.
Jämför med biblioteksfunktionen random.shuffle(alist). Vilken är skillnaden mellan hur resultatet (den slumpmässiga blandningen) ges?
    * Lösning: [blanda.py](ran_blanda.py)

3. Skriv en funktion som gör en nxn-enhetsmatris.
    * Lösning: [enhetsmatris.py](ran_enhetsmatris.py)
    
4. Skriv en funktion som tar en strängparameter som kan vara en lång text som består av många ord. Låt funktionen beräkna och returnera längden av det längsta ordet. Ett ord är en följd av bokstäver. Alla tecken som inte är bokstäver betraktas som avskiljare mellan orden. Använd funktionen s.isalpha() som kan anropas på textsträngar och ger True om strängen s bara innehåller bokstäver. s.isalpha() ger True även för svenska bokstäver å,ä,ö.  Testa även med en text inläst från en fil.
    * Lösning: [lengthoflongestword.py](ran_lengthoflongestword.py)
