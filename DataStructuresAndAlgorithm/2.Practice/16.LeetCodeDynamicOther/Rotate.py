# WRITE ROTATE FUNCTION HERE #
def rotate(nums, k):
    n = len(nums)
    if n == 0:
        return

    k %= n  # Handle cases where k > n

    # Reverse helper
    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    # Step 1: Reverse the whole array
    reverse(0, n - 1)
    # Step 2: Reverse first k elements
    reverse(0, k - 1)
    # Step 3: Reverse remaining n-k elements
    reverse(k, n - 1)


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(nums, k)
print("Rotated array:", nums)

"""
    EXPECTED OUTPUT:
    ----------------
    Rotated array: [5, 6, 7, 1, 2, 3, 4]

"""