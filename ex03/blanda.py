import random
import time
"""
2. Skriv en funktion som konstruerar en slumpmässig blandning av en lista genom att slumpa fram ett element i taget, plocka ut det ur första listan och sätta in det i en annan lista som blir funktionens resultat.

Lösning: blanda.py. I den här lösningen förstörs parameterlistan eftersom listelementen successivt plockas ut ur listan.
Jämför med biblioteksfunktionen random.shuffle(alist). Vilken är skillnaden mellan hur resultatet (den slumpmässiga blandningen) ges?
"""

def shuffle_long(input_list):
    new_list = []
    while len(input_list) > 0:
        random_value = random.choice(input_list)
        input_list.remove(random_value)
        new_list.append(random_value)

    return new_list

def shuffle_compact(input_list):
    new_list = []
    while len(input_list) > 0:
        new_list.append(
            input_list.pop(
                random.randrange(0, len(input_list))))

    return new_list
    
def get_number_of_seconds_to_run_function_n_times(
        function, n):
    start_time = time.time()
    for _ in range(n):
        input_list = [3, 9, 2, 1, 2, 3, 9, 123, 123]
        function(input_list)
    end_time = time.time()
    
    dt = end_time - start_time
    return dt
    
def perform_time_test():
    n = 100000
    for function in [shuffle_compact, shuffle_long]:
        dt = get_number_of_seconds_to_run_function_n_times(
            function, n)
        
        print("It took", dt, "seconds")
    
def try_shuffle():
    input_list = [3, 4, 9, 1, -348484858585]
    new_list = shuffle(input_list)
    print(input_list, new_list)
    
#try_shuffle()
perform_time_test()
