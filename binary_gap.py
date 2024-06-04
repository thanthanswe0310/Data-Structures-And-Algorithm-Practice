

def solution(N):

    # import pdb;pdb.set_trace()

    # Convert N to binary representation
    binary_repr= bin(N)[2:]

    #Initialize variables to track the legnth of the current binary gap and the longest binary gap:

    current_gap = 0
    max_gap = 0

    #Iterate throught the binary representation:

    for digit in binary_repr:
        if digit =='0':
            #If the digit is 0, increment the current gap length 
            current_gap+=1
        else:
            #If the digit is 1, update the max gap if the current is longer
            max_gap = max(max_gap, current_gap)
            current_gap = 0

    return max_gap

result = solution(20)

print("The result : ",result)

# first return statement is max_gap =0
# second return statement is max_gap =2
