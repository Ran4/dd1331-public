# Memoization

def finfib(n, previous_fibs=None):
    global ANTAL_ANROP
    ANTAL_ANROP += 1
    
    if n <= 1:
        return 1
    
    if previous_fibs is None:
        previous_fibs = {}
        
    if n not in previous_fibs:
        previous_fibs[n] = finfib(n-1, previous_fibs) + finfib(n-2, previous_fibs)
        
    return previous_fibs[n]

def fulfib(n):
    global ANTAL_ANROP
    ANTAL_ANROP += 1
    
    if n <= 1:
        return 1
    else:
        return fulfib(n-1) + fulfib(n-2)
    
for n in [2, 4, 8, 16, 32]:
    global ANTAL_ANROP
    ANTAL_ANROP = 0
    print("fulfib({}) = {} och kräver {} beräkningar".format(n, fulfib(n), ANTAL_ANROP))
    #~ ANTAL_ANROP = 0
    #~ print("finfib({}) = {} och kräver {} beräkningar".format(n, finfib(n), ANTAL_ANROP))
