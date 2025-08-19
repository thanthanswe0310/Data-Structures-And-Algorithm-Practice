def solution(A):
    if len(A) < 2:
        return 0

    max_profit = 0
    min_price = A[0]

    for price in A[1:]:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit

# Test case
A = [23171, 21011, 21123, 21366, 21013, 21367]
print(solution(A))  # Output: 356
