from math import log

def shift_to_next_bit_one(N):
  return N ^ 2**int(log(N, 2))


def solution(N):
    max_gap = 0

    while shift_to_next_bit_one(N) > 0:
        gap = abs(int(log(N, 2)) - int(log(shift_to_next_bit_one(N), 2))) - 1
        max_gap = gap if gap > max_gap else max_gap
        N = shift_to_next_bit_one(N)

    return max_gap
