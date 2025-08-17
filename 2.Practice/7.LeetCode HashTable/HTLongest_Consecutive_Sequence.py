# Given an unsorted array of integers, write a function that finds the length of the  longest_consecutive_sequence (i.e., sequence of integers in which each element is one greater than the previous element).
# Use sets to optimize the runtime of your solution.
# Input: An unsorted array of integers, nums.
# Output: An integer representing the length of the longest consecutive sequence in nums.
# How It Works:
# num_set = set(nums) → duplicates remove လုပ်ပြီး lookup O(1) လုပ်နိုင်အောင်။
#
# Iterate over num_set → each number အတွက် sequence start ဖြစ်မဖြစ် စစ်တယ် (num-1 not in set)။
# Sequence start ဖြစ်ရင် consecutive numbers ကို count လုပ်ပြီး longest ကို update လုပ်တယ်။
import pdb


# Time and Space Complexity:
# # Time Complexity: O(n) — set conversion + iteration, each number visited once
# Space Complexity: O(n) — store numbers in a set

def longest_consecutive_sequence(nums):

    if not nums:
        return 0

    num_set = set(nums)
    longest= 0

    for num in num_set:
        # Only start counting if num-1 is not set (start of a sequence)
        if num-1 not in num_set:
            current_num = num
            current_length = 1

            # Count consecutive numbers
            while current_num+1 in num_set:
                current_num +=1
                current_length += 1

            longest = max(longest,current_length)

    return longest

nums = [100, 4, 200, 1, 3, 2]
print(longest_consecutive_sequence(nums))
# Output: 4 (sequence: 1, 2, 3, 4)
