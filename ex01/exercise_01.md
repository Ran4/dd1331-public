# Övning 1

## Texteditorer

Det finns en uppsjö med med olika text-editorer och [IDE](https://en.wikipedia.org/wiki/Integrated_development_environment)s att välja på.

Egentligen spelar det inte så stor roll vad du använder, men det kan vara svårt att välja.

Nedan följer en liten tabell över texteditorer som finns till samtliga tre stora operativsystem
(Windows, OS X och Linux).

| Namn         | Kommando | Svårighetsgrad | Kan även köras i terminalen | Finns på Ubuntudatorerna i datorsalarna | Öppen mjukvara |
|--------------|----------|----------------|-----------------------------|-----------------------------------------|----------------|
| Sublime text | subl     | Låg            | Nej                         | Nej                                     | Nej
| Gedit        | gedit    | Låg            | Nej                         | Ja                                      | Ja
| Vim          | vim      | Hög            | Ja                          | Ja                                      | Ja
| Emacs        | emacs    | Hög            | Ja (`emacs -nw`)            | Ja                                      | Ja
| Nano         | nano     | Låg            | Ja                          | Ja                                      | Ja

Se till att ni inte använder "rich text"-editorer såsom Word/WordPad i Windows eller textEdit i OS X.
Risken är annars stor att editorn ändrar på det ni skrivit in.

Utöver detta finns det ett gäng IDE's, såsom PyCharm, Pythonplugin till Eclipse och Visual Studio, och mycket
mycket mer.

## Inställningar för texteditorer

För att undvika problem under kursen så finns det vissa saker man bör se till att sin texteditor är inställd
på.

1. Se till att använda konsistent indentering (indrag). Nästan alla pythonprogram använder en intendering om 4 mellanslag: se till att ställa in din texteditor så att tab-knappen (eller motsvarande) intenderar med fyra mellanslag och ingenting annat.
2. Om du använder windows, se till att din texteditor är inställd att använda "unix newlines" (till skillnad från "dos fileendings" eller liknadne)). Annars kan du få problem om någon annan öppnar din fil.
3. Det kan vara praktiskt att aktivera syntax highlighting (text blir färgad beroende på innehållet)
4. När ett program kraschar får du ofta en s.k. traceback som visar dig på vilket radnummer koden kraschade. Det kan därför vara praktiskt att aktivera radnummer.
5. Se till att din fil sparas i utf-8, och ingenting annat. **Du ska --inte-- behöva skriva in '#encoding: utf-8' för att få ÅÄÖ att fungera!**.

## Det som gicks igenom under föreläsning var i grova drag:

Variabler och typer.
Tilldelningar.
Python interactive mode, python som miniräknare

Begrepp att öva på:
* Inläsning, beräkning och utskrift.
* Felkontroll av indata (med if-sats).
* Repetition med while.

Era repositories kommer att ligga på adresserna:
* `https://gits-15.sys.kth.se/användarnamn-gruproglab1`
* Exempel: `https://gits-15.sys.kth.se/ransin-gruproglabb1`

## Förslag till uppgifter, från grupdaten, med lösningar:

1. Om sidlängderna hos en triangel är a,b och c så kan triangelns yta beräknas
   med hjälp av [Herons formel](http://sv.wikipedia.org/wiki/Herons_formel).
   Låt `s = (a+b+c)/2` och `A = sqrt(s*(s-a)*(s-b)*(s-c))`. Skriv ett program som
   frågar efter a,b och c samt beräknar och skriver ut triangelytan. Låt
   programmet även göra kontroller av a,b,c så att de angivna värdena verkligen
   kan bilda en triangel. Lösning: [heronsFormel.py](grupdat/ran_heronsformel.py).

2. Pythonkramaren, uppgift 24: Skriv ett program som frågar efter ett antal
   sekunder och skriver ut hur många dagar, timmar, minuter och sekunder det
   är. Lösning: [sekunder.py](grupdat/ran_sekunder.py).

3. Pythonkramaren, uppgift 25: Beräkna siffersumman för ett tresiffrigt heltal.
   Siffersumman av 413 är 4 + 1 + 3 = 8. Lösning:
   [siffer3summa.py](grupdat/ran_siffer3summa.py).

4. Utvidga föregående uppgift så att den beräknar siffersumman av ett hetal med
   godtyckligt antal siffror. Lösning: siffersumma.py.  a. Skriv ett program
   som summerar n st termer av serien 1/1 + 1/2 + 1/3 + 1/4 + .... Lösning:
   harmsum.py b. Skriv ett annat program som beräknar hur många termer som
   behövs för att summan av samma serie ska blir större än något visst värde.
   Lösning: [antalTermer.py](grupdat/ran_antaltermer.py)
