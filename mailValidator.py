email = input("Enter email: ")

if "@" in email and "." in email and email.index("@") < email.index("."):
    print("Valid Email ID")
else:
    print("Invalid Email ID")
