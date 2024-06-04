def fibN(N):
    fib = [0] * 100
    fib[1] =1
    for i in range(2,100):
        fib[i]= fib[i-1]+fib[i-2]
        if fib[i]>N:
            return fib[2:i]

def solution(A):
    A.append(1)
    fib = fibN(len(A))
    reachsteps =[0]*(len(A))

    for j in fib:
        if A[j-1]==1:
            reachsteps[j-1] =1

    for i in range(len(A)):
        if A[i]==0 or reachsteps[i]>0:
            continue
        
        min_i = -1
        min_v = 100000
        for j in fib:
            previous = i-j
            if previous < 0 :
                break
            if reachsteps[previous]>0 and min_v> reachsteps[previous]:
                min_v = reachsteps[previous]
                min_i = previous
        if min_i != -1:
            reachsteps[i] = min_v +1
    if reachsteps[len(A)-1]>0:
        return reachsteps[len(A)-1]
    else: return -1

pass



print(solution([2, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0]))
