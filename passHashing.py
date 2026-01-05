import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

password = "Radhika@123"
hashed = hash_password(password)

print("Original:", password)
print("Hashed:", hashed)
