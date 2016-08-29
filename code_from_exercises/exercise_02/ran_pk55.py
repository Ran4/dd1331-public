def years_since_started(name, current_year):
    """Given name of type "F-XX" and current year given as an integer,
    calculate the number of years since "F-XX" started.
    
    If the last two digits of name is more than the current year,
    assume that we're talking about the 1900s, not the 2000s.
    E.g. F-19 must be F-1919, not F-2019
    """
    current_year_twodigits = current_year % 100
    year_twodigits = int(name[-2:])
    if year_twodigits > current_year_twodigits:
        return current_year - (1900 + year_twodigits)
    else:
        return current_year - (2000 + year_twodigits)
    
print('F-86', years_since_started('F-86', 2016))
print('F-98', years_since_started('F-98', 2016))
print('F-02', years_since_started('F-02', 2016))
print('F-06', years_since_started('F-06', 2016))
print('F-12', years_since_started('F-12', 2016))
print('F-15', years_since_started('F-15', 2016))
