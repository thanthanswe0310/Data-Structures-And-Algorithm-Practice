# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, P, Q):
    N = len(S) # S = ACCGTA
    M = len(P) 
    
    # Preprocess to calculate cumulative counts of nucleotides
    prefix_sums = [[0] * (N + 1) for _ in range(4)]  # A, C, G, T
    
    for i in range(N):
        impact_factor = 0
        if S[i] == 'A':
            impact_factor = 1
        elif S[i] == 'C':
            impact_factor = 2
        elif S[i] == 'G':
            impact_factor = 3
        elif S[i] == 'T':
            impact_factor = 4
        
        for j in range(4):
            prefix_sums[j][i+1] = prefix_sums[j][i] + (1 if j + 1 == impact_factor else 0)
    
    # Process queries
    result = []
    for k in range(M):
        start = P[k]
        end = Q[k] + 1
        
        for nucleotide in range(4):
            if prefix_sums[nucleotide][end] - prefix_sums[nucleotide][start] > 0:
                result.append(nucleotide + 1)
                break
    
    return result


solution('CAGCCTA',[2,3,0,4],[4,5,3,6])