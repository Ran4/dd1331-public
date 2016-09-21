#!/usr/bin/env python3

def get_array_from_string(string):
    """Turns a string into a list of lists ("an array"), and returns
    a tuple consisting of the array, the height and the width.
    """
    array = []
    for row in string.split("\n"):
        if row:
            array.append(list(row))
    height = len(array)
    width = len(array[0])
    return array, height, width

def print_array(array):
    """Takes a list of lists `array` and prints it to the screen, row for row,
    by joining each row with "".join
    """
    for row in array:
        print("".join(row))

bean_string = """
  xxxx 
 x    x
x---xx 
x- -x  
x    x 
 xxxx  
"""

WALL = "x"
EMPTY = " "
array, HEIGHT, WIDTH = get_array_from_string(bean_string)

def replace_characters_in_array(array, from_character, to_character):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if array[y][x] == from_character:
                array[y][x] = to_character

def main():
    print_array(array)
    
    replace_characters_in_array(array, "-", "!")
    
    print()
    print_array(array)

main()
