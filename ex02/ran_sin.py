#!/usr/bin/env python3
import math

def fakultet(n):
    product = 1
    for number in range(2, n+1):
        product *= number
    return product

def taylor_sin(x):
    """
    We know that e.g.
    sin(x) = x - x^3/3! + x^5/5! -x^7/7! + x^9/9!
    
    This function calculates sin using this formula.
    Maximum error is given by the EPSILON variable
    """
    #term is our last calculated term (starting with the first term)
    sum_ = 0
    term = x
    
    EPSILON = 1e-10
    k = 1 # k corresponds to "x^k/k!" in a term
    sign = 1 # 1 or -1, start with the -1
    while abs(term) > EPSILON:
        term = sign * x**k / fakultet(k)
        sum_ += term
        sign = -sign
        k += 2
        
    return sum_

def test_taylor_sin():
    MAX_ACCEPTED_ERROR = 1e-5
    
    START_T = -10.0
    END_T = 10.0
    NUM_TESTS = 100
    step = (END_T - START_T) / NUM_TESTS
    
    t = START_T
    while t < END_T:
        t += step
        error = abs(taylor_sin(t) - math.sin(t))
        assert error < MAX_ACCEPTED_ERROR
    
test_taylor_sin()

t = 0.37
print("t =", t)
print("taylor_sin:", taylor_sin(t))
print("math.sin:  ", math.sin(t))
print()

t = 2.16
print("t =", t)
print("taylor_sin:", taylor_sin(t))
print("math.sin:  ", math.sin(t))
print()
