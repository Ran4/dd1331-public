def pretty_row_repr(row, separator=", "):
    """
    Example:
        pretty_row_repr([3, 4, 5]) == "3, 4, 5"
    """
    row_as_strings = map(str, row)
    return separator.join(row_as_strings)

def pretty_print_matrix(matrix):
    """
    Example:
        >>> pretty_print_matrix([[3, 4], [1, 9])
        is the same as
        >>> "3, 4\n1, 9"
    """
    pretty_rows = [pretty_row_repr(row, separator=" ") for row in matrix]
    pretty_representation = "\n".join(pretty_rows)
    print(pretty_representation)
