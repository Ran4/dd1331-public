### ATT JÄMFÖRA SORTERINGSMETODER.

Tilda och Totte skrev var sin sorteringsfunktion. Tilda valde en utsökt mergesort medan Totte tog en standard selectionsort (urvalssortering). När de provkörde med tusen objekt gick ändå Tottes program lika fort som Tildas, eftersom han har superdator. Men med tiotusen objekt vann Tilda. Med hur mycket?

#### Tidsåtgång, average case:

* Selection sort: `O(N^2)`

* Merge sort: `O(N log N)`

Om vi tänker oss att Tottes dator är `x` gånger snabbare än Tildas dator, så kan vi ställa upp tidskvoten mellan
Tilde och Tottes lösning:

```
t(Tilda)  /  t(Totte)  =  (N log N)  /  (N^2 / x)
```

---

#### Hur mycket snabbare är Tottes dator?

Vi vet att för N = 1000 gäller att
```
t(Tilda) / t(Totte) = 1
```

Således

```
1 = (N log N)  /  (N^2 / x)
1 = x N log N / N^2
1 = x log N / N
```

Då `N = 1000 ~ 1024 = 2^10`

får vi att

```
log N = log 1000 ~ log 2^10 = 10 log 2 = 10
log 1000 ~ 10
```

vilket leder till

```
x log N / N = 1
x (10 / 1000) = 1
x = 100
```

**Delsvar:** Tottes dator är 100 gånger snabbare än Tildas dator.

---

Vi kan nu ställa upp `t(Tilda)  /  t(Totte)` för alla N:

```
t(Tilda) / t(Totte) = N log N / (N^2 / 100)
                    = 100 N log N / N^2
                    = 100 log N / N
```

Med N = 10000 = 10^4 fås

```
t(Tilda) / t(Totte) = 100 log N / N
                    = 400 log 10 / 10
                    = 40 log 10
                    = 40 * 3.3219
                    = 132.88
```

**Svar:** Tildas algoritm löser problemet runt 130 gånger snabbare, trots att hennes dator är hundra gånger långsammare.
