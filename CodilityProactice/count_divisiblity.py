def solution(A,B,K):

    import pdb;pdb.set_trace()

    c = int(B/K)-int(A/K)
    print("Count : ",c)
    if(A%K==0):
        c =c+1
    print("C : ",c)
    return c
    pass


solution(2,10,3)
      