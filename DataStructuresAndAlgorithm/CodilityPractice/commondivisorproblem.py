def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def prime_factors(n):
    factors = set()
    i = 2
    while i * i <= n:
        if n % i == 0:
            factors.add(i)
            n //= i
        else:
            i += 1
    if n > 1:
        factors.add(n)
    return factors

def solution(A, B):
    count = 0
    for i in range(len(A)):
        common_divisor = gcd(A[i], B[i])
        A_factors = prime_factors(A[i])
        B_factors = prime_factors(B[i])
        if A_factors == B_factors:
            count += 1
    return count

# Test cases
A = [15, 10, 9]
B = [75, 30, 5]
print(solution(A, B))  # Output: 1
