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

a. * polyval:
        * inre loop: n+1 multiplikationer ~ (för stora n:) n
        * yttre loop: len(coeff\_values) - 1 ~ len(coeff\_values) ~ (för stora n:) n
        * -> inre * yttre = n * n == n**2
        * svar: O(n**2)
   * horner: 
        * inre och enda loop: len(coeff_values) multiplikationer ~ n
        * svar: O(n)

b. 

