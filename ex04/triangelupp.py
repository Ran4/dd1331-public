

def triangelbas_upp(indentering, bredd):
    text = " " * indentering + bredd * "*"
    if bredd > 0:
        text += "\n" + triangelbas_upp(indentering - 1, bredd +2)
    return text

print(triangelbas_upp(1, 7))
