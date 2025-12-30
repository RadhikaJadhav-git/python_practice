import random
import string

count = int(input("How many passwords?: "))

for i in range(count):
    password = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
    print(password)
