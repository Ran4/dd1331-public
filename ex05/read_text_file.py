
"""Visa hur man kan läsa en textfil med ett ord per rad och få orden som en lista i sitt program. Alltså om filen är textfil så ska listan bli
['Vad', 'tror', 'du', 'att', 'det', 'hände', 'sen', '?'].
"""

with open("text.txt", "r") as f:
    for line_with_newlines in f.readlines():
        line = line_with_newlines.rstrip("\n")
        print(line)
