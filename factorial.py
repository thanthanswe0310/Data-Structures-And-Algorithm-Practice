# We are given some positive integer n. Let’s compute the factorial of n and assign
# it to the variable factorial. The factorial of n is n! = 1 · 2 · . . . · n. We can obtain it by
# starting with 1 and multiplying it by all the integers from 1 to n.

# def factorial(N):
#     factorial=1

#     for i in range(N): # i starts with 0, then 

#         factorial *=i+1
#         print(factorial)
#     return factorial

# factorial(4)


# Let’s print a triangle made of asterisks (‘*’) separated by spaces. The triangle
# should consist of n rows, where n is a given positive integer, and consecutive rows should
# contain 1, 2, . . . , n asterisks. For example, for n = 4 the triangle should appear as follows:

# def trainglestar(N):
    
#     for i in range(1,N+1):
#         for j in range(i):
#             print('*', end=' ')
#         print()
#     return

# trainglestar(5)

# Let’s print a triangle made of asterisks (‘*’) separated by spaces and consisting
# of n rows again, but this time upside down, and make it symmetrical. Consecutive rows should
# contain 2n − 1, 2n − 3, . . . , 3, 1 asterisks and should be indented by 0, 2, 4, . . . , 2(n − 1)
# spaces. For example, for n = 4 the triangle should appear as follows:

# def reversetraingle_star(N):
#     for i in range(N,0,-1): # start, stop, step

#         for j in range(i):
#             print('*',end=' ')
#         print()
#     return

# reversetraingle_star(5)
