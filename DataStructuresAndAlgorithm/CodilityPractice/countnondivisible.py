import math

def solution(A):
    # Find the maximum value in array A
    max_val = max(A)
    
    # Count the occurrences of each number in array A
    count = {}
    for num in A:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    # Initialize a result array to store the count of non-divisors
    result = []
    
    # Iterate over each element in array A
    for num in A:
        divisors_count = 0
        
        # Iterate from 1 up to the square root of the element
        for divisor in range(1, int(math.sqrt(num)) + 1):
            if num % divisor == 0:
                # If the current number is a divisor of the element,
                # add its count of occurrences to divisors_count
                if divisor in count:
                    divisors_count += count[divisor]
                other_divisor = num // divisor
                if other_divisor != divisor and other_divisor in count:
                    divisors_count += count[other_divisor]
        
        # Calculate the count of non-divisors for the current element
        non_divisors_count = len(A) - divisors_count
        
        # Append the count of non-divisors to the result array
        result.append(non_divisors_count)
    
    return result

# Test case
A = [3, 1, 2, 3, 6]
print(solution(A))  # Output: [2, 4, 3, 2, 0]
