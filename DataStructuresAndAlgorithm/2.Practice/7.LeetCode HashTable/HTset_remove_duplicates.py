# Set: Remove Duplicates ( ** Interview Question)
# You have been given a list my_list with some duplicate values. Your task is to write a Python program that removes all the duplicates from the list using a set and then prints the updated list.
#
# You need to implement a function remove_duplicates(my_list) that takes in the input list my_list as a parameter and returns a new list with no duplicates.
#
# Your function should not modify the original list, instead, it should create a new list with unique values and return it.

#Explanation:
#
# set(my_list) → duplicates ကို automatically remove လုပ်ပေးတယ်။
#
# list(unique_set) → set ကို list ပြန်ပြောင်းပြီး return လုပ်တယ်။
#
# Original list ကို modify မလုပ်ပါ; new list အနေနဲ့ unique elements ရမယ်။

# Time and Space Complexity:
#
# Time Complexity: O(n) — list ကို iterate လုပ်ပြီး set ထဲသို့ insert လုပ်တာ။
#
# Space Complexity: O(n) — unique elements တွေကို store လုပ်ရန် set နဲ့ list လိုအပ်တယ်။

def remove_duplicates(my_list):
    # Convert list to set to remove duplicates
    unique_set = set(my_list)

    # Convert back to list
    unique_set = list(unique_set)

    return unique_set
my_list = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(my_list))
# Output: [1, 2, 3, 4, 5] (order may vary)
