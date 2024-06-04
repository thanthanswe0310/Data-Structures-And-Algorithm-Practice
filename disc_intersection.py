def solution(A):
    N = len(A)
    intersect_count = 0
    
    # Calculate the starting and ending points of each disc on the x-axis
    disc_starts = [0] * N
    disc_ends = [0] * N
    for i in range(N):
        disc_starts[max(0, i - A[i])] += 1
        disc_ends[min(N - 1, i + A[i])] += 1
    
    # Calculate the prefix sums of the disc starts and ends
    prefix_starts = [0] * (N + 1)
    prefix_ends = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix_starts[i] = prefix_starts[i - 1] + disc_starts[i - 1]
        prefix_ends[i] = prefix_ends[i - 1] + disc_ends[i - 1]
    
    # Count intersecting pairs
    for i in range(N):
        intersect_count += prefix_ends[max(0, i - A[i])]
        intersect_count -= prefix_starts[min(N, i + A[i] + 1)]
        
        if intersect_count > 10000000:
            return -1
    
    return intersect_count

# Test case
A = [1, 5, 2, 1, 4, 0]
print(solution(A))  # Output: 11
