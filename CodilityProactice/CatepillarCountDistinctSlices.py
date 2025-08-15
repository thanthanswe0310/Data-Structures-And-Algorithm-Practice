def solution(M, A):
    # Initialize variables
    distinct_slices = 0
    seen = set()
    left = 0
    
    # Iterate through the array using the right pointer
    for right in range(len(A)):
        # If the current element is already in the set, move the left pointer
        while A[right] in seen:
            seen.remove(A[left])
            left += 1
        # Add the current element to the set
        seen.add(A[right])
        # Update the distinct slices count
        distinct_slices += (right - left + 1)
        # Check if the distinct slices count exceeds 1,000,000,000
        if distinct_slices > 1000000000:
            return 1000000000
    
    return distinct_slices

# Test case
M = 6
A = [3, 4, 5, 5, 2]
print(solution(M, A))  # Output: 9
