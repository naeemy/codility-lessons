
from collections import Counter

def solution(A):
    count = Counter(A)

    for number, count in count.items():
        if count & 1:
            return number

    return 0