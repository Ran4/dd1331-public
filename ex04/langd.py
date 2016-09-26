

def length(seq):
    if not seq:
        return 0
    else:
        mindre_lista = seq[1:]
        return 1 + length(mindre_lista)
