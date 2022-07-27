import random

# Generate a random number to be guessed
number = random.randint(0,100)

print("Guess a magic number between 0 and 100")

guess = -1
# nilai guess diberi nilai -1 karena di luar rentang 0 hingga 100
# nilai digunakan untuk memastikan looping berjalan

# Prompt the user guess the number
while guess != number:
    guess = eval(input("Enter your guess : "))

    if guess == number:
        print("Yes, the number is", number)
    elif guess > number:
        print("Your guess is too high")
    else:
        print("Your guess is too low")