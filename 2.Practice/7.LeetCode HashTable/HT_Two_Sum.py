# HT: Two Sum ( ** Interview Question)
# two_sum()
# Problem:
# Given an array of integers nums and a target integer target, find the indices of two numbers in the array that add up to the target.
# The main challenge here is to implement this function in one pass through the array. This means you should not iterate over the array more than once. Therefore, your solution should have a time complexity of O(n), where n is the number of elements in nums.
# Input:
# A list of integers nums .
# A target integer target.
# Output:
# A list of two integers representing the indices of the two numbers in the input array nums that add up to the target. If no two numbers in the input array add up to the target, return an empty list [].

###### Explanation
# 1. We use a hash table (dictionary) to keep track of numbers we have seen and their indices.
# 2. For each number num, we calculate complement = target - num.
# 3. If complement is already in seen, we have found the pair -> return the indices.
# 4. Otherwise, store the number with its index.
#5. This works in O(n) Time and O(n) space.

def two_sum(nums,target):
    seen = { }

    for i,num in enumerate(nums):

        complement = target - num

        if complement in seen:

            return [seen[complement],i]

        seen[num] =i


    return []


print(two_sum([12, 7, 2, 15], 9))  # Output: [0, 1]
# print(two_sum([3, 2, 4], 6))       # Output: [1, 2]
# print(two_sum([3, 3], 6))          # Output: [0, 1]
# print(two_sum([1,2,3,8,7,6],9))