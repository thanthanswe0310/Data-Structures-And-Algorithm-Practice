def solution(A):
    N = len(A)
    min_sum = float('inf')
    
    # Generate all possible combinations of signs for the elements in A
    for i in range(1 << N):
        current_sum = 0
        for j in range(N):
            # If j-th bit is 0, use -1; otherwise, use 1
            sign = -1 if (i >> j) & 1 == 0 else 1
            current_sum += sign * A[j]
        min_sum = min(min_sum, abs(current_sum))
    
    return min_sum

print(solution([1, 4, -3, -1]))