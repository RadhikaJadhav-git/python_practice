sentence = "Improve your English"
vowels = "aeiouAEIOU"

count = 0
for ch in sentence:
    if ch in vowels:
        count += 1

print("Vowel count:", count)
