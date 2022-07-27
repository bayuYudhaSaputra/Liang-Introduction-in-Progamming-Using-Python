import random

# 1. Generate two random single digit
number1 = random.randint(0,9)
number2 = random.randint(0,9)

# 2. If number1 < number2, swap number
if number1 < number2:
    number1, number2 = number2, number1

# 3. Prompt the student to answer "What is number1 - number2 ?"
answer = eval(input("What is " + str(number1) + " - " + str(number2) + "? "))

# 4. Repeatly ask the question until the answer is correct
while number1 - number2 != answer:
    answer = eval(input("Wrong answer, Try again. What is " + str(number1) + " - " + str(number2) + "? "))

print("You got it!") 