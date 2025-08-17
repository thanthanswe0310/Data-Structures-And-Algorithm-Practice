# HT: Group Anagrams ( ** Interview Question)
# You have been given an array of strings, where each string may contain only lowercase English letters. You need to write a function group_anagrams(strings) that groups the anagrams in the array together using a hash table (dictionary). The function should return a list of lists, where each inner list contains a group of anagrams.
# For example, if the input array is ["eat", "tea", "tan", "ate", "nat", "bat"], the function should return [["eat","tea","ate"],["tan","nat"],["bat"]] because the first three strings are anagrams of each other, the next two strings are anagrams of each other, and the last string has no anagrams in the input array.
# You need to implement the group_anagrams(strings) function and return a list of lists, where each inner list contains a group of anagrams according to the above requirements.
# Please calculate time and space complexity as well.
#
# Approach
# Use a dictionary anagrams where:
# Key = a signature of the word (sorted string).
# Value = list of words with that signature.
# Iterate through each string in the input array:
# Sort the string → get the key.
# Append the string to the dictionary under that key.
# Return the values of the dictionary as a list of lists.



def group_anagrams(strings):

    anagrams = {} # dictionary to hold list of anagrams
    for word in strings:
        key = ''.join(sorted(word))
        if key in anagrams:
            anagrams[key].append(word)
        else:
            anagrams[key] =[word]

    return list(anagrams.values())

input_strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(input_strings))
