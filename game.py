import random

number = random.randint(1, 10)

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 10.")
print("You have 3 attempts.")

for attempt in range(1, 4):
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("Congratulations! You guessed correctly.")
        break
    elif guess < number:
        print("Too low!")
    else:
        print("Too high!")
else:
    print("Game over!")
    print("The correct number was:", number)