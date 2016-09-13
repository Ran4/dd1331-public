"""
4. Skriv en funktion som tar en strängparameter som kan vara en lång text som består av många ord.

* Låt funktionen beräkna och returnera längden av det längsta ordet.

* Ett ord är en följd av bokstäver. Alla tecken som inte är bokstäver betraktas som avskiljare mellan orden. Använd funktionen s.isalpha() som kan anropas på textsträngar och ger True om strängen s bara innehåller bokstäver. s.isalpha() ger True även för svenska bokstäver å,ä,ö.

* Testa även med en text inläst från en fil.
"""
def get_longest_word(words):
    print("in get_longest_word, words:", words)
    longest_word = words[0]
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

def is_divider(character):
    return not character.isalpha()

def get_words_from_word_string(word_string):
    """
    Example:
        get_words_from_word_string("Alla tecken som inte är bokstäver") == \
            ["Alla", "tecken", "som", "inte", "är", "bokstäver"]
    """
    words = []
    character_list = []
    for character in word_string:
        if is_divider(character):
            new_word = "".join(character_list)
            words.append(new_word)
            character_list = []
        else:
            character_list.append(character)
    
    if character_list:
        new_word = "".join(character_list)
        words.append(new_word)
        
    return words

def get_length_of_longest_word_from_word_string(word_string):
    words = get_words_from_word_string(word_string)
    longest_word = get_longest_word(words)
    return len(longest_word)

def test():
    word_string = "Alla tecken som inte är bokstäver"
    
    assert get_words_from_word_string(
        word_string) == \
        ["Alla", "tecken", "som", "inte", "är", "bokstäver"]
    print("Test of get_words_from_word_string was successful")
    
    words = get_words_from_word_string(word_string)
    longest_word = get_longest_word(words)
    print("longest word:", longest_word)
    
    print("längsta ordet har längden",
        get_length_of_longest_word_from_word_string(word_string))
        
test()
