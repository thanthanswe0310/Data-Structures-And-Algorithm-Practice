# WRITE FIND_LONGEST_STRING FUNCTION HERE #
def find_longest_string(strings):
    if not strings:  # handle empty list
        return None

    longest = strings[0]
    for s in strings[1:]:
        if len(s) > len(longest):
            longest = s
    return longest


string_list = ['apple', 'banana', 'kiwi', 'pear']
longest = find_longest_string(string_list)
print(longest)

"""
    EXPECTED OUTPUT:
    ----------------
    banana

"""