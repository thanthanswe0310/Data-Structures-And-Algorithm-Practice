def solution(N, A):
    R = [0]*N
    m = 0
    b = 0
    for i in range(0, len(A)):
        if A[i] <= N:
            R[A[i]-1] = max(b, R[A[i]-1]) + 1
            m = max(m, R[A[i]-1])
        else:
            b = m
    for i in range(0, len(R)):
        if R[i] < b:
            R[i] = b
    return R  # Add this line to return the modified array R

# print(solution(5, [3, 4, 4, 6, 1, 4, 4]))


def solutions(N,A):
   
    counters = [0]*N
    max_value =0
    last_max_counters= 0

    for operation in A:
        if 1 <= operation <=N :
            counters[operation-1] +=1
            max_value = max(max_value,counters[operation-1])
        elif operation == N+1:
            last_max_counters =max_value
        else:
            raise ValueError("Invalid operation")
        
    # Update counters not yet updated by max counters
    for i in range(N):
        counters[i] = max(counters[i],last_max_counters)
    return counters

#input test
print(solutions(5,[4,5,2,3,5,3,4]))