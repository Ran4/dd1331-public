#!/usr/bin/env python3
"""
4. Skriv en funktion som tar en strängparameter som kan vara en lång text som
består av många ord.

* Låt funktionen beräkna och returnera längden av det
längsta ordet.

* Ett ord är en följd av bokstäver.

* Alla tecken som inte är bokstäver betraktas som avskiljare mellan orden.

* Använd funktionen s.isalpha() som kan anropas på textsträngar och ger True om
strängen s bara innehåller bokstäver. s.isalpha() ger True även för svenska
bokstäver å,ä,ö.
"""

def is_divider(char):
    return not char.isalpha()

def add_word_from_char_list(words, char_list):
    word = "".join(char_list)
    words.append(word)

def get_words_from_word_string(word_string):
    words = []
    char_list = []
    for char in word_string:
        if is_divider(char):
            add_word_from_char_list(words, char_list)
            char_list = []
        else:
            char_list.append(char)
    add_word_from_char_list(words, char_list)
    return words

def find_longest_word(words):
    """Re-implementation of max(words, key=len)
    """
    if len(words) == 0:
        raise Exception("words can't be empty!")
    
    longest_word = words[0]
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word
    
def find_longest_word_from_word_string(word_string):
    """
    Inputs:
        word_string: a string that looks like a text with multiple words
            e.g. "hello world"
    """
    words = get_words_from_word_string(word_string)
    return find_longest_word(words)

def find_length_of_longest_word_from_word_string(word_string):
    return len(find_longest_word_from_word_string(word_string))

def test_find_longest_word_from_word_string():
    for word_string, longest_word in [
            ("hej hopp", "hopp"),
            ("hej hej", "hej"),
            ("", ""), ]:
        assert find_longest_word_from_word_string(word_string) == longest_word
        
    # Also load from example file
    filename = "test_word_string.txt"
    with open(filename) as f:
        word_string_from_file = f.read()
    
    assert find_longest_word_from_word_string(word_string_from_file) == \
        "Fadderullanlej"
    
test_find_longest_word_from_word_string()
