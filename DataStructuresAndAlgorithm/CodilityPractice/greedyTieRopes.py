def solution(K, A):
    count = 0
    current_length = 0
    
    for length in A:
        current_length += length
        if current_length >= K:
            count += 1
            current_length = 0
            
    return count

# Test case
print(solution(4, [1, 2, 3, 4, 1, 1, 3]))  # Output: 3
