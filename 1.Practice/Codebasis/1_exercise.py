def get_squared_numbers(numbers):
    squared_number =[]
    for n in numbers:
        squared_number.append(n*n)
    return squared_number


numbers = [2,5,8,9]
get_squared_numbers(numbers) # O(n)


def find_first_pe(prices,eps, index):
    pe = prices[index]/eps[index]  # O(1)
    return pe 


numbers = [3,6,2,4,3,6,8,9]
duplicate = None 
for i in range(len(numbers)):  # O(n)
    for j in range(i+1, len(numbers)):  # O(n)
        if numbers[i] ==numbers[j]:  # a 
            print(numbers[i] + " is a duplicate")  # ==> a+ O(n^2)+b
            break

for i in range(len(numbers)):
    if numbers[i] == duplicate:  # n iterations
        print(i)


# 1. Keep fastest growing term 
# 2. Drop constants

# BigO refers to very large value of n. Hence if you have a function like
# time = 5 * n^2 + 3*n + 20

# When value of n is very large b*n +c become irrevalant 

# example : n = 1000

# time = 5*1000 + 3*1000+ 20
# time = 500000 + 3020
# 
# 

 