def solution(A):
    if len(A)==0:
        return 0
    A.sort()
    c=1
    for i in range(1,len(A)):
        if A[i]!= A[i-1]:
            c+=1
    return c
    pass

print(solution([1,2,1,2,3,5,4,4,3,0]))