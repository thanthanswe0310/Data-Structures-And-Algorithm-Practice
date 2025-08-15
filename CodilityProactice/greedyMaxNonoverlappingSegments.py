def solution(A, B):
    if not A:
        return 0
    
    N = len(A)
    segments = sorted(zip(A, B), key=lambda x: x[1])
    
    count = 1
    last_end = segments[0][1]
    
    for start, end in segments[1:]:
        if start > last_end:
            count += 1
            last_end = end
            
    return count

# Test case
print(solution([1, 3, 7, 9, 9], [5, 6, 8, 9, 10]))  # Output: 3
