#!/usr/bin/env python3
"""
5. Pythonkramaren 54:
Byt ordning på två ord.
Från indata "Li Jiarong" producera och skriv ut "Jiarong Li".
Från indata "Agaton Sax" producera och skriv ut "Sax Agaton".
"Jiarong Li"
"""

def switch_order(name_with_space):
    name_with_space_words = name_with_space.split(" ")
    reshaped_words = name_with_space_words[1:] + [name_with_space_words[0]]
    reshaped_name_with_space = " ".join(reshaped_words)
    return reshaped_name_with_space

def test_switch_order():
    assert switch_order("Li Jiarong") == "Jiarong Li"
    assert switch_order("Agaton Sax") == "Sax Agaton"
    assert switch_order("Hej") == "Hej"
    print("Tests OK")
    
test_switch_order()
