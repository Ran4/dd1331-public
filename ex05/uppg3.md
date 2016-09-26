# Uppgift 3, från tentamen 12-03-17

Antag att polynom representeras med listor så att första elementet är koefficienten för högstagradstermen och sista elementet är den konstanta termen.

Listan [a_{n}, a_{n-1}, ... a_{0}] är polynomet a_{n} x^n + a_{n-1} x^{n-1} + ... + a_1 x + a_{0}.

Följande två algoritmer beräknar polynomets värde för något värde på x:

```python
def polyval(coeff_values, x):
    result = 0
    n = len(coeff_values) - 1
    for coeff in coeff_values:
        xs = 1
        for i in range(n):
            xs *= x
        result += coeff * xs
        n -= 1
    return result

def horner(coeff_values, x):
    result = 0
    for coeff in coeff_values:
        result = result * x + coeff
    return result
```


a. Ange komplexiteten för varje algoritm räknat i **antal multiplikationer**.

N är polynomets gradtal.

Ge svaret som O(logn), O(n) eller liknande.

b. En helt annan algoritm implementerades och kördes för olika problemstorlekar, n.

Med n = 100 tog körningen 0.21 sekunder, för n = 200 tog den 1.7 sekunder och för n = 400 gick det åt 14.1 sekunder.

Konstruktören av algoritmen hävdar optimistiskt att dess tidskomplexitet är O(n^2).

Är det rimligt? Vilken tidskomplexitet tror du att det är?

Motivera svaret med hjälp av de angivna körtiderna.

### SVAR:

**a1. Polyval:**

* inre loop: 1 multiplikation, körs n gånger (där `n = len(coeff_values) - 1 .. 1`)

* yttre loop: inre loop + 1 multiplikation, körs `len(coeff_values)` gånger

* Totalt: med `N = len(coeff_values)`: N + (N-1) + (N-2) + (N-3) + ... + 1 = N(N+1)/2 ggr

* För stora N: N(N)/2 = N^2 / 2 ggr.

* Vi bryr oss inte om konstanterna -> N^2

* **SVAR:** O(N^2)
        
**a2. Horner:** 

* inre och enda loop: 1 multiplikation, körs `len(coeff_values)` gånger
* svar: O(N)


**b.** 

Vi ritar upp tiderna i en tabell:

| N (1) | Tid (s) |
|-------|---------|
| 100   | 0.21    |
| 200   | 1.7     |
| 400   | 14.1    |

Vi kollar vad som händer med tiden när N fördubblas:

1.7 / 0.21 = 8.095238

14.1 / 1.7 = 8.294118

Vi ser alltså att tiden 8-faldigas vid varje dubbling: algoritmen är därmed O(n^3).
