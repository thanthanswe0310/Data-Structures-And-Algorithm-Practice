# Set: Find Pairs ( ** Interview Question)
# You are given two lists of integers, arr1 and arr2, and a target integer value, target. Your task is to find all pairs of numbers (one from arr1 and one from arr2) whose sum equals target.
#
# Write a function called find_pairs that takes in three arguments: arr1, arr2, and target, and returns a list of all such pairs.  Assume that each array does not contain duplicate values.
#
# The tests for this exercise assume that arr1 is the list being converted to a set.
# How It Works:
#
# set(arr1) → arr1 ကို set ပြောင်းပြီး lookup O(1) လုပ်နိုင်အောင်။
#
# arr2 ကို iterate လုပ်ပြီး target - num ကို arr1 set မှာ ရှိမရှိ စစ်တယ်။
#
# ရှိရင် (arr1_num, arr2_num) အဖြစ် pair အဖြစ် append လုပ်တယ်။
#
# Time and Space Complexity:
#
# Time Complexity: O(n + m)
#
# n = len(arr1) → set conversion
#
# m = len(arr2) → iteration
#
# Space Complexity: O(n) → set_arr1 store လုပ်ရန်


def find_pairs(arr1, arr2, target):
    # Convert arr1 to set for O(1) lookups
    set_arr1 = set(arr1)

    pairs = []

    # Iterate over arr2 and check if (target - num) exists in set_arr1
    for num in arr2:
        if (target-num) in set_arr1:
            pairs.append((target-num,num))

    return pairs
arr1 = [1, 2, 3, 4]
arr2 = [2, 3, 5, 7]
target = 7

print(find_pairs(arr1, arr2, target))
# Output: [(3, 4), (2, 5)]
