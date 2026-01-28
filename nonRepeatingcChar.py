def first_unique_char(s):
    from collections import Counter
    count = Counter(s)

    for ch in s:
        if count[ch] == 1:
            return ch
    return None
