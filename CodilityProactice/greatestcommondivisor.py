def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def solution(N, M):
    # Find the greatest common divisor of N and M
    gcd_value = gcd(N, M)
    
    # The number of chocolates eaten will be N divided by the GCD
    return N // gcd_value

# Test cases
N = 10
M = 4
print(solution(N, M))  # Output: 5



# Test cases
N = 10
M = 4
print(solution(N, M))  # Output: 5