memo =[None] *100
counter=0
def fib(n):
    global counter
    counter +=1

    if memo[n] is not None:
        return memo[n]

    if n==0 or n ==1:
        return n

    memo[n]= fib(n-1) + fib(n-2)
    return memo[n]

n = 7

print('Fib of ',n,'=',fib(n))
print('Counter : ',counter)

#Memoization in Python is a technique used to speed up programs by storing the results of expensive function calls and returning
# the cached result when the same inputs occur again.
# It's especially useful for recursive algorithms like Fibonacci, where the same values are computed multiple times.

counter = 0

def fib(n):
    global counter
    counter +=1
    if n==0 or n ==1:
        return n
    return fib(n-1) +fib(n-2)

n=30
print("\nFib of ",n,"=",fib(n))
print("\nCounter:",counter)

# Memoization
memo =[None]*100

def fib(n):
    if memo[n] is not None:
        return memo[n]

    if n==0 or n==1:
        return n

    memo[n]= fib(n-1) +fib(n-2)

    return memo[n]


