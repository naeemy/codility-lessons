
def solution(A):
    A.sort()

    if len(A) == 0: # empty array
        return 1    
    elif len(A) == A[-1]: # single element
        return A[-1] + 1
    else:
        return abs(sum(range(1, A[-1]+1)) - sum(A))