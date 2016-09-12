#!/usr/bin/env python3
import random
"""
Skriv en funktion som konstruerar en slumpmässig blandning av en lista genom att slumpa fram ett element i taget, plocka ut det ur första listan och sätta in det i en annan lista som blir funktionens resultat. Lösning: blanda.py. I den här lösningen förstörs parameterlistan eftersom listelementen successivt plockas ut ur listan.
Jämför med biblioteksfunktionen random.shuffle(alist). Vilken är skillnaden mellan hur resultatet (den slumpmässiga blandningen) ges?
"""

def impure_shuffle_list(input_list):
    """Shuffles a list input_list by randomly removing elements in li to a new
    list, which is then returned
    """
    new_list = []
    
    while input_list:
        random_index_in_element = random.randint(0, len(input_list) - 1)
        popped_element = input_list.pop(random_index_in_element)
        new_list.append(popped_element)
    return new_list

def main():
    NUM_ELEMENTS = 10
    input_list = random.sample(range(1000), NUM_ELEMENTS)
    input_list_repr = str(input_list)
    new_list = impure_shuffle_list(input_list)
    print(input_list_repr, new_list)

main()
