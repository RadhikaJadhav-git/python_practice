def validate_registration(name, email, phone):
    if len(name) < 3:
        return "Name too short"

    if "@" not in email:
        return "Invalid email"

    if not phone.isdigit() or len(phone) != 10:
        return "Invalid phone number"

    return "Registration data is valid"


print(validate_registration("Radhika", "radhika@gmail.com", "9876543210"))
