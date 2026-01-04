import random
import string

def short_url():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

print("Short URL code:", short_url())
