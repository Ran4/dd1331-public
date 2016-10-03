#### LÖNAR DET SIG ATT SORTERA?

En miljon dumbolotter säljs var månad. För varje lott sparas lottnumret och köparen i ett objekt. En lista med en miljon objekt finns alltså i datorn vid dragningen, då tusen vinstnummer slumpas fram, ett efter ett. För varje nummer måste hela listan letas igenom, eftersom den är osorterad. Hur många jämförelser får man räkna med totalt? Lönar det sej att först sortera listan, en gång för alla?

### Svar:

Problemuppställning: Hur många slagningar `x` behöver vi som minst göra tills det är mer effektivt att sortera en lista och slå i den `x` gånger än att slå `x` gånger i en osorterad lista?

* Average case:

    * x slagningar i osorterad lista: `x * N / 2`

    * Sortera med quicksort: `N log(N)`

    * x slagningar i sorterad lista: `x * log(N)`

* De två metoderna:
    * Leta i osorterad lista = x * N / 2

    * Sortera + leta i sorterad lista = N log(N) + x * log(N)

### Uppställning:
```
N log(N) + x * log(N) < x * N / 2
N log(N) < x * (N / 2 - log(N))
x > (N log(N)) / (N / 2 - log(N))
```

För N = 10^6 :

```
10^6 = ( 10^3 )^2 ~ ( 2^10 )^2 = 2^20
log(N) ~ log(2^20) = 20 log(2) = 20
```

Om vi matar in N = 1e6 får vi:

```
x > 20e6 / (5e5 - 20)
x > 40.0016
```

**Svar:** Vid 41 dragningar eller fler så är det värt att sortera först

**Kontroll:**

* Sortera med quicksort + 41 slagningar:
    * `1e6*log(1e6) + 41 * log(1e6) = 19 932 386`

* 41 slagnignar i osorterad lista:
    * `41 * 1e6 / 2 = 20 500 000`
