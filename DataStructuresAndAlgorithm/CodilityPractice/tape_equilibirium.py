def solution(A):
    if len(A)<2:
        return 0
    s = sum(A)
    minDiffer =2000
    sl=0
    for i in range(0,len(A)-1):
        sl +=A[i]
        diff = abs(2*sl-s)
        minDiffer = min(minDiffer,diff)
    return minDiffer


print(solution([1,2,6,4,5]))