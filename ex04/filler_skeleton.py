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
x   xx 
x   x  
x    x 
 xxxx  
"""

WALL = "x"
EMPTY = " "
array, HEIGHT, WIDTH = get_array_from_string(bean_string)

def fill_array_at_point(array, y, x, fillchar):
    # INSERT CODE HERE
    pass

def main():
    print_array(array)
    fill_array_at_point(array, 1, 2, '-')
    print_array(array)

main()
