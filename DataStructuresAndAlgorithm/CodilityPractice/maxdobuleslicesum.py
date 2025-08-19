def solution(A):
    N = len(A)
    
    max_ending = [0] * N
    max_starting = [0] * N

    for i in range(1, N-1):
        max_ending[i] = max(0, max_ending[i-1] + A[i])
    
    for i in range(N-2, 0, -1):
        max_starting[i] = max(0, max_starting[i+1] + A[i])

    max_double_slice = 0

    for i in range(1, N-1):
        max_double_slice = max(max_double_slice, max_ending[i-1] + max_starting[i+1])

    return max_double_slice

# Test case
A = [3, 2, 6, -1, 4, 5, -1, 2]
print(solution(A))  # Output: 17
