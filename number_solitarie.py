def solution(A):
    N = len(A)
    max_sum = [float('-inf')] * N
    max_sum[0] = A[0]  # Base case: starting position
    
    for i in range(N):
        for j in range(1, 7):  # Rolling the die from 1 to 6
            if i + j < N:
                max_sum[i + j] = max(max_sum[i + j], max_sum[i] + A[i + j])
    
    return max_sum[-1]

# Example usage:
A = [1, -2, 0, 9, -1, -2]
print(solution(A))  # Output: 8