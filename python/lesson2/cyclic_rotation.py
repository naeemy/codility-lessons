
def shiftElements(A, K):
    R = K % len(A)

    second = A[len(A)-R:]
    first = A[:len(A)-R]

    return second+first


def solution(A, K):
    if K==0 or len(A) == 0:
        return A

    if len(set(A)) == 1 or len(A) == K:
        return A

    return shiftElements(A, K)
    