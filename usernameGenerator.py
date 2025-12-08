import random

first = input("Enter first name: ").lower()
last = input("Enter last name: ").lower()

number = random.randint(100, 999)
username = first[:3] + last[:3] + str(number)

print("Generated Username:", username)
