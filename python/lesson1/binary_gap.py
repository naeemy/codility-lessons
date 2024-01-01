from math import log

def shiftToNextBitOne(N):
  return N ^ 2**int(log(N, 2))


def solution(N):
    max_gap = 0

    while shiftToNextBitOne(N) > 0:
        gap = abs(int(log(N, 2)) - int(log(shiftToNextBitOne(N), 2))) - 1
        max_gap = gap if gap > max_gap else max_gap
        N = shiftToNextBitOne(N)

    return max_gap
