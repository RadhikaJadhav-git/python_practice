import random

number = random.randint(1, 20)
attempts = 3

while attempts > 0:
    guess = int(input("Guess the number: "))
    if guess == number:
        print("You win!")
        break
    else:
        attempts -= 1
        print("Wrong! Attempts left:", attempts)

if attempts == 0:
    print("Number was:", number)
