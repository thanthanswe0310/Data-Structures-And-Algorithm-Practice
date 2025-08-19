# Ologn algorithm - sorting algorithms

# Different terms for inputs

def print_items(n):
    for i in range(n):
        print(i)  # ==> O(n)

    for j in range(n):
        print(j)  # ==> O(n)

    ## ==> O(2n)


def print_items2(a,b):
    for i in range(a):
        for j in range(b):
            print(i,j)  # ==> O(a*b)


