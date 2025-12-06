import random

number = random.randint(1, 50)
attempts = 0

while True:
    guess = int(input("Guess the number (1–50): "))
    attempts += 1

    if guess == number:
        print(f"Correct! You guessed in {attempts} attempts.")
        break
    elif guess < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
