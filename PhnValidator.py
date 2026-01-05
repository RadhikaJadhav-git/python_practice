import re

def is_valid_phone(number):
    pattern = r'^[6-9]\d{9}$'
    return bool(re.match(pattern, number))

print(is_valid_phone("9876543210"))
print(is_valid_phone("1234567890"))
