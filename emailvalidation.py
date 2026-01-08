import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return "Valid Email"
    return "Invalid Email"

print(validate_email("test@gmail.com"))
