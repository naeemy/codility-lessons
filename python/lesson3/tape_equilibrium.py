
from math import inf

def solution(A):
    if len(A) == 2:
        return abs(A[0] - A[1])

    sum_of_all = sum(A)
    first_half = 0
    P = inf
    for e in A:
        first_half += e
        S = sum_of_all - first_half
        D = abs(first_half - S)
        P = D if D < P else P

    return P


[-10, -20, -30, -40, 100]