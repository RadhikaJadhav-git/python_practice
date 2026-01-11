username = "admin"
password = "1234"

input_user = input("Enter username: ")
input_pass = input("Enter password: ")

if input_user == username and input_pass == password:
    print("Login Successful")
else:
    print("Invalid Credentials")
