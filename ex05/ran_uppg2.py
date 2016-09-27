"""
Visa hur man kan läsa en textfil med ett ord per rad och få orden som en lista i sitt program. Alltså om filen är textfil så ska listan bli
['Vad', 'tror', 'du', 'att', 'det', 'hände', 'sen', '?']
"""

def read_words_from_file_to_list(filename):
    lines = []
    with open(filename) as f:
        for line_with_newline in f.readlines():
            line = line_with_newline.rstrip("\n")
            lines.append(line)
    return lines
            
def read_words_from_file_to_list_using_list_comprehension(filename):
    """Like read_words_from_file_to_list, but written using
    a list comprehension.
    """
    with open(filename) as f:
        return [line.rstrip("\n") for line in f.readlines()]

filename = "min_fil.txt"
lines = read_words_from_file_to_list(filename)
lines2 = read_words_from_file_to_list_using_list_comprehension(filename)
print(lines)
print(lines2)
