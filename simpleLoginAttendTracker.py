correct_password = "admin123"
attempts = 0

while attempts < 3:
    pwd = input("Enter password: ")
    if pwd == correct_password:
        print("Login Successful")
        break
    else:
        attempts += 1
        print("Wrong password")

if attempts == 3:
    print("Account Locked")
