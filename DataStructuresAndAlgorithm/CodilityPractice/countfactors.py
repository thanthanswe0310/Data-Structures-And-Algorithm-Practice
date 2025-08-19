def solution(N):
    count = 0
    i = 1

    while i * i <= N:
        if N % i == 0:
            if i * i == N:
                count += 1
            else:
                count += 2
        i += 1

    return count

# Test case
N = 24
print(solution(N))  # Output: 8
