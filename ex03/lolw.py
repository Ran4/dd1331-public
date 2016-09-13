#!/usr/bin/env python3
"""
4. Skriv en funktion som tar en strängparameter som kan vara en lång text som består av många ord. Låt funktionen beräkna och returnera längden av det längsta ordet.

* Ett ord är en följd av bokstäver.

* Alla tecken som inte är bokstäver betraktas som avskiljare mellan orden.

* Använd funktionen s.isalpha() som kan anropas på textsträngar och ger True om strängen s bara innehåller bokstäver. s.isalpha() ger True även för svenska bokstäver å,ä,ö.

* Testa även med en text inläst från en fil.
"""

def is_delimiter(character):
    return not character.isalpha()

def get_words_from_word_string(word_string):
    words = []
    character_list = []
    for character in word_string:
        if is_delimiter(character):
            word = "".join(character_list)
            words.append(word)
            character_list = []
        else:
            character_list.append(character)

    return words

def find_longest_word(words):
    pass

def funktion(word_string):
    words = get_words_from_word_string(word_string)
    find_longest_word(words)
    return len(longest_word)

def test_function():
    print(get_words_from_word_string("hej hopp"))
    
test_function()
