from collections import Counter

def first_unique_char(s):
    count = Counter(s)
    
    for char in s:
        if count[char] == 1:
            return char
    return None

print(first_unique_char("aabbcde"))