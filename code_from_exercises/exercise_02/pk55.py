# coding: latin1

# Här antar vi att årskursbeteckning alltid ser ut som X-yy 
# och att om yy är > 12 så avses nittonhundratalet annars
# tjugohundratalet. Inga felkontroller gors


def tid(studstat,aktuelltar):
    y = int(studstat[2:])
    if y > 12:
        return aktuelltar - (1900+y)
    else:
        return aktuelltar - (2000+y)

# Testanrop

print('F-86',tid('F-86', 2012))
print('F-98',tid('F-98', 2012))
print('F-02',tid('F-02', 2012))
print('F-06',tid('F-06', 2012))
print('F-12',tid('F-12', 2012))
