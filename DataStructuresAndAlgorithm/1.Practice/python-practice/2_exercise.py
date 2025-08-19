# Variables are dynamically typed 

# n =0 
# print('n =',n)

# # Mulitple assignments
# n, m= 0,'abc'

# n,m,z = 0.125,"abc",False

# # Increment
# n = n+1 
# n +=1

# # None is null (absence of value)
# n= 4
# n= None 

# If statements don't need parentheses 
# or curly braces.

# n = 1 
# if n>2:
#     n -=1 
# elif n ==2:
#     n *= 2
# else:
#     n +=2 

# parentheses needed for multi-line conditions. 
# and &&, or ||

# if ((n>2) and (n!=m) or n==m):
#     n +=1

# # while loops are similar
# n =0
# while n<5:
#     print(n)
#     n +=1

# looping from i =0 to i =4 
# for i in range(5):
#     print(i)

# # looping fro i =2 to i =5 
# for i in range(2,6):
#     print(i)


# # looping from i = 5 to i =2 
# for i in range(5,1,-1):
#     print(i)

# Division is decimal by default
# print(5/2)

# # Division slash rounds down 
# print(5//2)

# # careful : most languages round towards 0 by default 
# # so negative members will round down

# print(-3//2)

# A workaround for rounding towards zero is to use
# decimal division and then convert to int.

# print(int(-3/2))

# # Modding is similar to most languages
# print(10%3)

# # Except for negative values 
# print(-10%3)


# To be consistent with other languages modulo
# import math 
# print(math.fmod(-10,3))


# Max / Min int
# float("inf")

# float("-inf")

# # python numbers are infinite so they never overflow
# import math 
# print(math.pow(2,200))

# Arrays (called lists in python)
# arr =[1,2,3]

# Can be used as a stack
# arr.append(4)
# arr.append(5)
# print(arr)

# arr.pop()
# print(arr)

# arr.insert(1,7)
# print(arr)

# arr[0] =0
# arr[3] =3

# Initialize arr of size n with default value of 1 

# n =5
# arr =[1,2,3]

# print(arr[-1])

# Indexing -2 is the second to last value 

# arr = [1,2,3,4]
# print(arr[1:3])

# # Unpacking
# a,b,c = [1,2,3]

# print(a,b,c)

# Loop through arrays
# nums =[1,2,3]

# Using index
# for i in range(len(nums)):
#     print(nums)

# without index
# for n in nums:
#     print(n)

# for i,n in range(n):
#     print(i)

# Loop thorugh multiple arrays simultaeneously

# Sorting array
# arr =["b","aa","dd","ad","ea"]

# print(arr.sort())


# # Custom sort (by length of string)
# arr.sort(key=lambda x: len(x))

# List comprehension
# arr = [i for i in range(5)]
# print(arr)

# 2 D lists
# arr =[[0]*4 for i in range(4)]

# This won't work
# arr = [[0]*4]*4
# print(arr)

# Strings are similar to arrays
# s = "abc"
# print(s[0:2])

# # But they are immutable
# s[0] = "A"

# # Strings are similar to arrays 
# s = "abc"
# print(s[0:2])

# Valid numeric strings can be converted 
# print(int("123") + int("123"))

# # And numbers can be converted to strings 
# print(str(123) +str(123))

# ## In rare cases you may need the ASCII value of a char
# print(ord("a"))
# print(ord("b"))

# Combine a list of strings with an empty string delimitor

# strings = ["ab","cd","ef"]
# print("".join(strings))

# HashSet
# mySet = set()

# mySet.add(1)
# mySet.add(2)
# print(mySet)
# print(len(mySet))

# print(1 in mySet)
# print(2 in mySet)

# mySet.remove(1)
# print(2 in mySet)

# list to set
print(set([1,2,3]))

# Set comprehension
# mySet = {i for i in range(5)}
# print(mySet)


# HashMap (aka dict)
# myMap ={}
# myMap["alice"] =88

# Dict comprehension
myMap ={i :2*i for i in range(3)}
print(myMap)


myMap ={"alice":90,"bob":70}
for key in myMap:
    print(key,myMap[key])

for val in myMap.values():
    print(val)

for key,val in myMap.items():
    print(key,val)

# Tuples are like arrays but immutable
# tup = (1,2,3)
# print(tup)

# mySet = set()
# mySet.add(1,2)
# print((1,2) in mySet)

# Heaps
# import heapq

# # Under the hood are arrays
# minHeap =[]
# heapq.heappush(minHeap,3)
# heapq.heappush(minHeap,2)
# heapq.heappush(minHeap,4)

# # Min is always at index 0 
# print(minHeap[0])

# while len(minHeap):
#     print(heapq.heappop(minHeap))

import heapq

maxHeap =[]
heapq.heappush(maxHeap,-3)

# Max is always at index 0
print(-1 * maxHeap[0])

while len(maxHeap):
    print(-1 * heapq.heappop(maxHeap))

# Heaps
import heapq

# Build heap from initial values
arr =[2,1,8,4,5]
heapq.heapify(arr)

while arr:
    print(heapq.heappop(arr))

# Functions 
def myFunc(n,m):
    return n * m 

# Nested functions have access to outer variables
def outer(a,b):
    c ="c"
    def inner():
        return a+b+c 
    return c


# Can modify objects but not reassign unless using local keyword

def double(arr,val):
    def helper():
        # Modifying array works
        for i, n in enumerate(arr):
            arr[i] *=2

        nonlocal val 


# Class
class myClass:
    def __init__(self,nums):
        self.nums =nums
        self.size = len(nums)
    
    def getLength(self):
        return self.size
    
    def getDobuleLength(self):
        return 2* self.getLength()
    
    
