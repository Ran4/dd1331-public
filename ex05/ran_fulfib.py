def fulfib(n):
    global ANTAL_ANROP
    ANTAL_ANROP += 1
    if n <= 1:
        return n
    return fulfib(n - 1) + fulfib(n - 2)

def finfib(n, fib_dict=None):
    global ANTAL_ANROP
    ANTAL_ANROP += 1
    
    if fib_dict is None:
        fib_dict = {}
    
    if n <= 1:
        return n

    if n not in fib_dict:
        fib_dict[n] = finfib(n - 1, fib_dict) + finfib(n - 2, fib_dict)
    return fib_dict[n]

# Testanrop:
def skriv_ut_antalet_anrop(function_name, f):
    """Kör en funktion f (med strängrepresentationen function_name),
    och skriver ut den globala vairabeln ANTAL_ANROP för några funktionsvärden
    """
    #for n in range(2, 30, 4):
    for n in range(1, 30, 1):
        global ANTAL_ANROP
        ANTAL_ANROP = 0
        f(n)
        print("{}({}) gör {} anrop!".format(function_name, n, ANTAL_ANROP))
        
skriv_ut_antalet_anrop("fulfib", fulfib)
skriv_ut_antalet_anrop("finfib", finfib)
