# Set: Has Unique Chars ( ** Interview Question)
# Write a function called has_unique_chars that takes a string as input and returns True if all the characters in the string are unique, and False otherwise.
#
# For example, has_unique_chars('abcdefg') should return True, while has_unique_chars('hello') should return False.

# How It Works:
# set(s) → string အတွင်းရှိ character များကို unique set အဖြစ်ပြောင်းသည်။
# len(unique_chars) vs len(s) →
# တူရင် → all characters unique → return True
# မတူရင် → duplicate characters ရှိ → return False
# Time and Space Complexity:
# Time Complexity: O(n) — string ကို iterate လုပ်ပြီး set ထဲ insert လုပ်ရမယ်။
# Space Complexity: O(n) — set မှာ character များကို store လုပ်ရမယ်။

def has_unique_chars(s):
    # Convert string to set
    unique_chars = set(s)

    # Compare lengths
    return len(unique_chars) == len(s)

print(has_unique_chars('abcdefg'))  # True
print(has_unique_chars('hello'))    # False
