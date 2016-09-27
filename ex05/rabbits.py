import random

LEFT = -1
RIGHT = 1
RABBIT = "*"
EMPTY = " "
rabbits = list("* **   *   ***  ")

def get_random_direction():
    return random.choice([LEFT, RIGHT])

def can_move_to_position(rabbits, position):
    if position < 0 or position >= len(rabbits):
        return False
    
    return rabbits[position] == EMPTY

def print_rabbits(rabbits):
    print("|" + "".join(rabbits) + "|")

def move_rabbits(rabbits):
    new_rabbits = rabbits[:]
    n = len(new_rabbits)
    for x in range(n):
        char = new_rabbits[x]
        
        if char == RABBIT:
            direction = get_random_direction()
            new_x = x + direction
            if can_move_to_position(new_rabbits, new_x):
                new_rabbits[x] = EMPTY
                new_rabbits[new_x] = RABBIT
                print_rabbits(new_rabbits)

    return new_rabbits

def count_rabbits_at_position(rabbits, position):
    if position < 0 or position >= len(rabbits):
        return 0
    else:
        left_side = rabbits[:position]
        right_side = rabbits[position+1:]
            
        left_count =  count_rabbits_at_position(left_side, len(left_side)-1)
        right_count =  count_rabbits_at_position(right_side, 0)
        middle_count = 1 if rabbits[position] == RABBIT else 0
        
        count = left_count + middle_count + right_count
        return count

def update_rabbits(rabbits):
    new_rabbits = rabbits[:]
    for x, char in enumerate(rabbits):
        rabbits_at_position = count_rabbits_at_position(rabbits, x)
        if rabbits_at_position == 3:
            new_rabbits[x] = EMPTY
    return new_rabbits
    

print_rabbits(rabbits)
print()
for _ in range(20):
    #rabbits = move_rabbits(rabbits)
    rabbits = update_rabbits(rabbits)
    print_rabbits(rabbits)
    print()
