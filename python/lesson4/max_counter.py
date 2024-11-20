def solution(N, A):
    C = [0] * N
    max_counter = 0

    for a in A:
        if a == N+1:
            C = [max_counter] * N
        else:
            C[a-1] += 1
            max_counter = C[a-1] if C[a-1] > max_counter else max_counter

    return C
