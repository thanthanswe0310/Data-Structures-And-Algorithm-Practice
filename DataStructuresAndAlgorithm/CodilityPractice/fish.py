def solution(A,B):
    ds =[]
    c =0
    for i in range(0,len(B)):
        if (B[i]==1):
            ds.append(A[i])
        else:
            while(len(ds)!=0):
                if (ds[-1]>A[i]):
                    c =c +1
                    break
                elif ds[-1]<A[i]:
                    ds.pop()
                    c=c+1
    return len(A)-c
    pass
