
def count_list_levels(seq):
    if not isinstance(seq, list):
        return 0
    else:
        return 1 + max([count_list_levels(val) for val in seq])
    
def count_list_levels_using_map(seq):
    if not isinstance(seq, list):
        return 0
    else:
        return 1 + max(map(count_list_levels, seq))

def test_count_list_levels():
    values_and_answers = [
         (5,  0),
         ([3,4,-1],  1),
         ([3,[4,-3],-9],  2),
         ]
    for value, answer in values_and_answers:
        assert count_list_levels(value) == answer
        
test_count_list_levels()
