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

bean = """
  xxxx 
 x    x
x   xx 
x   x  
x    x 
 xxxx  
"""

WALL = "x"
EMPTY = " "
array, HEIGHT, WIDTH = get_array_from_string(bean)

def get_valid_neighbors(y, x):
    valid_neighbors = []
    for neighbor_y, neighbor_x in [
            (y-1, x),
            (y+1, x),
            (y, x+1),
            (y, x-1),
            ]:
        if neighbor_y >= 0 and neighbor_y < HEIGHT and \
                neighbor_x >= 0 and neighbor_x < WIDTH:
            valid_neighbors.append((neighbor_y, neighbor_x))
    return valid_neighbors
        
def fill_array_at_point(array, y, x, fillchar):
    if array[y][x] == EMPTY:
        array[y][x] = fillchar
        for neighbor_y, neighbor_x in get_valid_neighbors(y, x):
            fill_array_at_point(array, neighbor_y, neighbor_x, fillchar)

def main():
    print_array(array)
    fill_array_at_point(array, 1, 2, '-')
    print_array(array)

main()
