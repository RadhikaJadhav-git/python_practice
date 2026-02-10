# Check whether a number is prime

num = int(input("Enter a number: "))
flag = True

if num <= 1:
    flag = False
else:
    for i in range(2, num):
        if num % i == 0:
            flag = False
            break

if flag:
    print(num, "is Prime")
else:
    print(num, "is Not Prime")
