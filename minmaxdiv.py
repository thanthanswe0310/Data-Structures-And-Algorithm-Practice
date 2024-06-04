def count_blocks(A, max_block_sum):
    count = 1
    block_sum = 0
    for num in A:
        block_sum += num
        if block_sum > max_block_sum:
            count += 1
            block_sum = num
    return count

def solution(K, M, A):
    lower_bound = max(A)
    upper_bound = sum(A)
    
    while lower_bound <= upper_bound:
        mid = (lower_bound + upper_bound) // 2
        if count_blocks(A, mid) <= K:
            upper_bound = mid - 1
        else:
            lower_bound = mid + 1
            
    return lower_bound

# Test case
print(solution(3, 5, [2, 1, 5, 1, 2, 2, 2]))  # Output: 6
