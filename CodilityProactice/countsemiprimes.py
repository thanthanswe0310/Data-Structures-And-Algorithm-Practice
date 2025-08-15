def solution(N, P, Q):
    # Compute prime numbers up to N using Sieve of Eratosthenes
    primes = [True] * (N + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(N**0.5) + 1):
        if primes[i]:
            for j in range(i * i, N + 1, i):
                primes[j] = False
    
    # Compute semiprimes up to N
    semiprimes = [0] * (N + 1)
    for i in range(2, int(N**0.5) + 1):
        if primes[i]:
            for j in range(i * i, N + 1, i):
                if primes[j // i]:
                    semiprimes[j] += 1
    
    # Compute count of semiprimes up to each index
    for i in range(1, N + 1):
        semiprimes[i] += semiprimes[i - 1]
    
    # Compute the count of semiprimes within each query range
    result = []
    for i in range(len(P)):
        result.append(semiprimes[Q[i]] - semiprimes[P[i] - 1])
    
    return result

# Test cases
N = 26
P = [1, 4, 16]
Q = [26, 10, 20]
print(solution(N, P, Q))  # Output: [10, 4, 0]
