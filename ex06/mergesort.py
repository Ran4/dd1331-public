


def mergesort(seq):
    if len(seq) <= 1:
        return seq
    
    mid = len(seq) // 2
    left_sorted, right_sorted = mergesort(seq[:mid]), mergesort(seq[mid:])
    
    sorted_seq = []
    while left_sorted and right_sorted:
        if left_sorted[0] > right_sorted[0]:
            sorted_seq.append(right_sorted.pop(0))
        else:
            sorted_seq.append(left_sorted.pop(0))
            
    sorted_seq.extend(left_sorted + right_sorted)
    
    return sorted_seq

def main():
    seq = [54,26,93,17,77,31,44,55,20]
    sorted_seq = mergesort(seq)
    print(sorted_seq)
    assert sorted_seq == sorted(seq)

if __name__ == "__main__":
    main()
