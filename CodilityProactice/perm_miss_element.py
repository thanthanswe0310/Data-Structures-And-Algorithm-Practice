def solution(A):
    import pdb;pdb.set_trace()
    if len(A)==0:
        return 1
    A.sort()

    for i in range(0,len(A)):
        if A[i]!= i+1:
            return i+1
    return (len(A)+1)
    pass


print(solution([1,2,4]))