def solution(A):
    max_ending = max_slice = A[0]

    for num in A[1:]:
        max_ending = max(num, max_ending + num)
        max_slice = max(max_slice, max_ending)

    return max_slice

# Test case
A = [3, 2, -6, 4, 0]
print(solution(A))  # Output: 5
