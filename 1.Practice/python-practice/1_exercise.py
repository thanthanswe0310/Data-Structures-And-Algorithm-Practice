# # Variables are dynamicaly typed

# # n = 0 
# # print('n :', n)

# # # Multiple assignments
# # n,m =0 ,'abc'

# # # Increment
# # n = n +1 
# # n += 1

# # # None is null (absence of value)
# # n =4

# # # If statements don't need parentheses or curly braces.
# # n = 1 
# # if n > 2:
# #     n -= 1 
# # elif n ==2 :
# #     n *=2 

# # Parentheses needed for multi-line conditions.
# # and = && 
# # or = ||
# n,m = 1,2 

# # while loops are similar 
# # n = 0 
# # while n<5:
# #     print(n)
# #     n +=1 

# # # Looping from i =0 to i =4 
# # for i in range(5):
# #     print(i)

# # looping from i = 2 to i =5
# # for i in range(2,6):
# #     print(i)

# # Division is decimal by default 
# # print(5/2)

# # Double slash rounds down
# # print(5//2)

# # Careful : most languages rounds towards 0 by 
# # default so negative numberes will round down
# # print(-3//2)


# # A workaround for rounding towards zero is to use
# # decimal division and then convert to int.
# # print(int(-3/2))


# # Modding is similar to most language
# # print(10%3)

# # Except for negative values
# # print(-10 % 3)

# import math 
# print(math.floor(3/2))

# # Max/min int 
# float("inf")
# float("-inf")


# # Python numbers are infinite so they never overflow 
# import math

# # array called lists in python
# arr = [1,2,3]
# print(arr)

# #Can be used as a stack
# arr.append(4)
# arr.append(5)
# print(arr)

# arr.pop()
# print(arr)

# arr.insert(1,7)
# print(arr)

# arr[0] = 0
# arr[3] = 3

# # Initialize array of size n with 
# n =5
# arr=[1]*3

# print(arr[-1])

# # Indexing -2 is the second to last value, etc
# print(arr[-2])

# # Sublists (aka slicing)
# arr =[1,2,3,4,]
# print(arr[1:3])

# # Similar to for -loop ranges, last index is non inclusive 
# print(arr[0:4])


# # Unpacking 
# a,b,c = [1,2,3]
# print(a,b,c)

# # Be careful though
# nums = [1,2,3]

# # Using index 
# for i in range(len(nums)):
#     print(nums[i])

# # Without index
# for n in nums:
#     print(n)

# # With index and value 
# for i,n in enumerate(nums):
#     print(i,n)

# # loop through multiple arrays simultaenously with unpacking
# nums1 =[1,2,3]
# nums1.reverse()
# nums1.sort()
# print(arr)


# arr =["bob","alice","jane","doe"]
# arr.sort()
# print(arr)

# # Custom sort (by length of string)
# arr.sort(key= lambda x:len(x))

# print(arr)

# # List comprehension 
# arr =[ i for i in range(5)]
# print(arr)

# # 2-D lists
# arr =[[0]*4]*4

# print(arr)

# # Strings are similar to arrays
# s ="abc"

# print(s[0:2])

# # But they are immutable

# # so this creates a new string 
# s +="def"
# print(s)

# # valid numeric strings can be converted 
# print(int("123")+int("123"))

# # in rare cases you may need the ASCII vale

# # join a string

# strings = ["abc","cd","ed"]
# print("".join(strings))

# # Queues (double ended queue)
# from collections import deque

# queue = deque()
# queue.append(1)
# queue.append(2)

# queue.popleft()
# print(queue)

# queue.appendleft(1)

# print(queue)

# queue.pop()
# print(queue)

# # Hashset
# mySet = set()

# mySet.add(1)
# mySet.add(2)
# print(mySet)

# print(1 in mySet)
# print(2 in mySet)
# print(3 in mySet)

# mySet.remove(2)
# print(2 in mySet)

# list to set

# print(set([1,2,3]))

# # Set to comprehension
# mySet = {i for i in range(5)}

# HashMap (aka dict)
# myMap ={}
# myMap["alice"] = 88
# myMap["bob"] = 77
# print(myMap)
# print(len(myMap))

# myMap["alice"] = 80
# print(myMap["alice"])

# print("alice" in myMap)
# myMap.pop("alice")

# print("alice" in myMap)
# myMap.pop("alice")

# print("alice" in myMap)

# myMap = {"alice": 90,"bob":70}

# Dict comprehension
# myMap ={i:2*i for i in range(3)}

# print(myMap)

# Looping through maps
# myMap = {'alice':90,"bob":70}

# for key in myMap:
#     print(key,myMap[key])


# for val in myMap.values():
#     print(val)

# for key,val in myMap.items():
#     print(key,val)

# Can be used as Key for hash map/set 
# myMap = {(1,2):3}
# print(myMap[(1,2)])

# mySet = set()
# mySet.add((1,2))
# print((1,2) in mySet)


# Heaps
# import heapq

# # under the hood are arrays 
# minHeap =[]
# heapq.heappush(minHeap,3)
# heapq.heappushpop(minHeap,2)


# # Min is always at index 0
# print(minHeap[0])

# while len(minHeap):
#     print(heapq.heappop(minHeap))

# maxHeap =[]
# heapq.heappush(maxHeap,-3)

# Can modify objects but not reassign 
# Unless using nonlocal keyword

# def double(arr,val):
#     def helper():
#         # Modifying array works
#         for i, n in enumerate(arr):
#             arr[i] *=2
        

# Heaps 
# import heapq

# # Build heap from initial values
# arr = [2,1,8,4,5]

# heapq.heapify(arr)
# while arr:
#     print(heapq.heappop(arr))


# Functions 
# def outer(a,b):
#     c ="c"

#     def inner():
#         return a+b+c 
#     return inner()


# def  double(arr,val):
#     def helper():
#         for i, n in enumerate(arr):
#             arr[i] *=2
        
#         # Will only modify val in the helper scope 
#         # val *=2

#         # this wil modify val outside helper scope 
#         nonlocal val 
#         val *= 2
#     helper()

#     print(arr,val)


# nums =[1,2]
# val =3 

# Class 
# class myClass:
#     # constructor
#     def __init__(self,nums):
#         # Create member variables
#         self.nums = nums 
#         self.size = len(nums)

#     # self key word required as param 
#     def getLength(self):
#         return self.size 

#     def getDoublength(self):
#         return 2* self.getDoublength()




