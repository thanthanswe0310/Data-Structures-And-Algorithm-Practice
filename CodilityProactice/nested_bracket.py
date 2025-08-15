def solution(S):
    if len(S)==0: return 1
    V =[]

    c={'[': +1, ']':-1,'(':+2,')':-2,'{':+3,'}':-3}

    for i in range(0,len(S)):
        if (i==0 and c[S[i]]<0):
            return 0
        if (c[S[i]]<0 and c[S[i]]!= -v[-1]):
            return 0
        elif (c[S[i]]<0):
            V.pop()
        else: V.append(c[S[i]])

    if(len(V)==0): return 1
    else: return 0

    pass

solution(['{}{[]()()}'])