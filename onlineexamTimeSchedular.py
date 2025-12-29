import time

seconds = 10
while seconds > 0:
    print("Time left:", seconds)
    time.sleep(1)
    seconds -= 1

print("Time Over! Auto Submit")
