def solution(S):
    p=0
    for i in range(0,len(S)):
        if S[i]=='(':
            p+=1
        elif S[i]==')':
            p-=1
        if p<0: return 0
    if p!=0: return 0
    else: return 1