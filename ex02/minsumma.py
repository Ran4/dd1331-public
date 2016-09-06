def min_summa(seq):
    sum_ = seq[0]
    for i in range(1,len(seq)):
        sum_ += seq[i]
    return sum_

print(min_summa(["he", "j"]))
