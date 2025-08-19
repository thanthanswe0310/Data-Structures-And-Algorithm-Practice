# HT: First Non-Repeating Character ( ** Interview Question)
# You have been given a string of lowercase letters.
# Write a function called first_non_repeating_char(string) that finds the first non-repeating character in the given string using a hash table (dictionary). If there is no non-repeating character in the string, the function should return None.
# For example, if the input string is "leetcode", the function should return "l" because "l" is the first character that appears only once in the string. Similarly, if the input string is "hello", the function should return "h" because "h" is the first non-repeating character in the string.

#### Logic ####
#1. Use a dictionary (counts) to count the frequency of each character.
#2. Iterate through the string in order and return the first character with count 1.
#3. If no such character exists, return None.


def first_non_repeating_char(string):
    counts ={}

    # Step 1 : Count each other
    for ch in string:
        counts[ch] = counts.get(ch,0) +1 
    
    # Step 2: Find the first character with count 1
    for ch in string:
        if counts[ch] ==1:
            return ch 
    # Step3 : None 
    return None 

print( first_non_repeating_char('leetcode') ) # l 

print( first_non_repeating_char('hello') ) # h

print( first_non_repeating_char('aabbcc') ) # none