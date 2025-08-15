def solution(A):
    A.sort()
    n = len(A)
    # Case 1: Product of the three largest elements
    max_product1 = A[-1] * A[-2] * A[-3]
    # Case 2: Product of the two smallest elements and the largest element
    max_product2 = A[0] * A[1] * A[-1]
    # Return the maximum of the two cases
    return max(max_product1, max_product2)

# Example usage:
A = [-3, 1, 2, -2, 5, 6]
print(solution(A))  # Output: 60
