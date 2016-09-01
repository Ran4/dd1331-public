#!/usr/bin/env python3
"""
Byt ordning på två ord. Från indata "Li Jiarong" producera och skriv ut "Jiarong Li".
"""

def find_space_in_name(name):
    """Returns the position of a space character in a name
    or -1 if no name was found.
    """
    i = 0
    for i in range(len(name)):
        if name[i] == " ":
            return i
    return -1

def switch_order(name):
    space_in_name_index = find_space_in_name(name)
    
    first_part = name[0:space_in_name_index]
    second_part = name[space_in_name_index+1:]
    
    name_with_switched_order = second_part + " " + first_part
    return name_with_switched_order

def test_switch_order():
    assert switch_order("Li Jiarong") == "Jiarong Li"
    assert switch_order("Agaton Sax") == "Sax Agaton"
    print("All tests OK")
    
test_switch_order()
