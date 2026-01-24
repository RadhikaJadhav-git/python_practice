# vowel_count.py

text = "Radhika Jadhav"
vowels = "aeiouAEIOU"

count = 0
for ch in text:
    if ch in vowels:
        count += 1

print("Vowel count:", count)
