def check_password(password):
    if len(password) < 8:
        return "Weak password"
    if not any(char.isdigit() for char in password):
        return "Password must contain a digit"
    if not any(char.isupper() for char in password):
        return "Password must contain an uppercase letter"
    return "Strong password"

pwd = input("Enter password: ")
print(check_password(pwd))
