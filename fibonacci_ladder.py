def solution(A, B):
    max_rungs = max(A)
    max_power = max(B)
    
    # Calculate Fibonacci sequence up to max_rungs
    fib = [0] * (max_rungs + 2)
    fib[1] = 1
    for i in range(2, max_rungs + 2):
        fib[i] = (fib[i - 1] + fib[i - 2]) % (1 << max_power)
    
    result = []
    for i in range(len(A)):
        result.append(fib[A[i] + 1] % (1 << B[i]))
    
    return result

# Test cases
print(solution([4, 4, 5, 5, 1], [3, 2, 4, 3, 1]))  # Output: [5, 1, 8, 0, 1]
