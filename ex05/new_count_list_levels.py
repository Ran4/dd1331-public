"""
Räkna antalet nästlade listnivåer i en lista, dvs i hur många nivåer listor i listor i listor .... som förekommer.

    Alla icke-listor ger 0 som funktionsvärde, t.ex.
    
    5 -> 0
    [3,4,-1] --> 1
    [3,[4,-3],-9] --> 2
    o.s.v. 
"""

def count_list_levels(seq):
    if not isinstance(seq, list):
        return 0
    else:
        return 1 + max([count_list_levels(val) for val in seq])

def test_count_list_levels():
    assert count_list_levels(5) == 0
    assert count_list_levels([3,4,-1]) == 1
    assert count_list_levels([3,[4,-3],-9]) == 2
    print("All tests passed")
    
test_count_list_levels()
