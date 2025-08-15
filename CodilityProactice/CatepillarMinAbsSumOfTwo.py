def solution(A):
    N = len(A)
    A.sort()
    
    left = 0
    right = N - 1
    min_abs_sum = float('inf')
    
    while left <= right:
        current_sum = A[left] + A[right]
        min_abs_sum = min(min_abs_sum, abs(current_sum))
        
        if current_sum <= 0:
            left += 1
        else:
            right -= 1
            
    return min_abs_sum

# Test cases
print(solution([1, 4, -3]))  # Output: 1
print(solution([-8, 4, 5, -10, 3]))  # Output: 3
