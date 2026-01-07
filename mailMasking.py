def mask_email(email):
    username, domain = email.split("@")
    masked = username[:2] + "*" * (len(username) - 2)
    return masked + "@" + domain

email = input("Enter email: ")
print("Masked Email:", mask_email(email))
