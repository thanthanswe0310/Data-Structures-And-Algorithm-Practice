def solution(X,A):
    B =[0]*X
    s=0
    for i in range(0,len(A)):
        if(B[A[i]-1]==0 and A[i]<=X):
            s+=1
            B[A[i]-1] = 1
        if(s==X):
            return i
    return -1
    pass

print(solution(5, [2,3,2,3,2]))  # Corrected function call with parentheses
