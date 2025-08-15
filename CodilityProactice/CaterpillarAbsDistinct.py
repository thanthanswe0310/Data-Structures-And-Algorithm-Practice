def solution(A):
    abs_distinct_count = 0
    left, right = 0, len(A) - 1
    prev_abs_value = None

    while left <= right:
        left_value, right_value = abs(A[left]), abs(A[right])

        # If the absolute values are equal, move both pointers towards the center
        if left_value == right_value:
            if prev_abs_value is None or left_value != prev_abs_value:
                abs_distinct_count += 1
                prev_abs_value = left_value
            left += 1
            right -= 1
        # If the absolute value of the left element is greater, move the left pointer
        elif left_value > right_value:
            if prev_abs_value is None or left_value != prev_abs_value:
                abs_distinct_count += 1
                prev_abs_value = left_value
            left += 1
        # If the absolute value of the right element is greater, move the right pointer
        else:
            if prev_abs_value is None or right_value != prev_abs_value:
                abs_distinct_count += 1
                prev_abs_value = right_value
            right -= 1

    return abs_distinct_count

# Test case
A = [-5, -3, -1, 0, 3, 6]
print(solution(A))  # Output: 5
