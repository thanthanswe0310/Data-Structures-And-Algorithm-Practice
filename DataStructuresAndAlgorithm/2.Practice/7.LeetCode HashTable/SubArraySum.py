# HT: Subarray Sum ( ** Interview Question)
# Given an array of integers nums and a target integer target, write a Python function called subarray_sum that finds the indices of a contiguous subarray in nums that add up to the target sum using a hash table (dictionary).
# Your function should take two arguments:
# nums: a list of integers representing the input array
# target: an integer representing the target sum
# Your function should return a list of two integers representing the starting and ending indices of the subarray that adds up to the target sum. If there is no such subarray, your function should return an empty list.

### This one is a classic Hash Table (prefix sum) problem.

## Logic here:
# How It Works:
# cum_sum = အစမှ လက်ရှိ index အထိ အရေအတွက် စုစုပေါင်း။
# cum_sum_dict က hash table ဖြစ်ပြီး key = cumulative sum, value = index လို့ သိမ်းထားတယ်။
# တစ်ခုချင်း iterate လုပ်ပြီး၊ (cum_sum - target) ကို hash table မှာ ရှိမရှိ စစ်တယ်။
# ရှိရင် contiguous subarray ရှိတယ် ဆိုပြီး starting နှင့် ending index ကို return လုပ်တယ်။
# မတွေ့ရင် cum_sum_dict မှာ cum_sum ကို index နဲ့ထည့်ထားတယ်။
# တစ်ခုလုံး iterate ပြီးလည်း မတွေ့ရင် [] return လုပ်တယ်။


# Time complexity is O(N)
# Space Complexity is O(N)

def subarray_sum(nums, target):
    # hash table to store cumulative sum and its index
    cum_sum_dict = {0: -1}  # key: cumulative sum, value: index
    cum_sum = 0

    for i, num in enumerate(nums):
        cum_sum += num

        # check if (cum_sum - target) exists in the hash table
        if (cum_sum - target) in cum_sum_dict:
            return [cum_sum_dict[cum_sum - target] + 1, i]

        # store the cumulative sum with its index
        cum_sum_dict[cum_sum] = i

    return []


print(subarray_sum([1, 2, 3, 4, 5], 9))

