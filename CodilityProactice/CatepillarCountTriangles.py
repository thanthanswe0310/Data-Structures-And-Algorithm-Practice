def solution(A):
    if len(A) < 3:
        return 0
    
    A.sort()
    count = 0
    
    for i in range(len(A)):
        left = 0
        right = i - 1
        
        while left < right:
            if A[left] + A[right] > A[i]:
                count += right - left
                right -= 1
            else:
                left += 1
    
    return count

# Test case
A = [10, 2, 5, 1, 8, 12]
print(solution(A))  # Output: 4
