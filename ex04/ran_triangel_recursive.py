#!/usr/bin/env python3

def triangelbas_upp(indentering, bredd):
    row = indentering * " " + bredd * "*"
    if bredd > 0:
        return row + "\n" + triangelbas_upp(indentering+1, bredd-2)
    return row

print(triangelbas_upp(1, 7))
