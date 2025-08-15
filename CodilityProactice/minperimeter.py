import math

def solution(N):
    min_perimeter = float('inf')
    i = 1

    while i * i <= N:
        if N % i == 0:
            factor1 = i
            factor2 = N // i
            perimeter = 2 * (factor1 + factor2)
            min_perimeter = min(min_perimeter, perimeter)
        i += 1

    return min_perimeter

# Test case
N = 30
print(solution(N))  # Output: 22
