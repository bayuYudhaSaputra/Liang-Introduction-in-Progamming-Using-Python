import random
import time

# Count the number of correct answers
correctCount = 0

# Count the number of questions
count = 0

# 5 question only
NUMBER_OF_QUESTIONS = 5

# Get start time
startTime = time.time()

while count < NUMBER_OF_QUESTIONS:
    # Generate two random single digit integers
    number1 = random.randint(0,9)
    number2 = random.randint(0,9)

    # If number1 < number2, swap number1 with number2
    if number1 < number2:
        number1, number2 = number2, number1

    # Prompt the student to answer "What is number1 - number2 ?"
    answer = eval(input("What is " + str(number1) + \
        " - " + str(number2) + "? "
        ))
    
    # Grade the answer and display the result
    if number1 - number2 == answer:
        print("You are correct!")
        correctCount += 1
    else:
        print("Your answer is wrong \n",
            number1, "-", number2, " = ",number1 - number2 
            )
    # Increase the count
    count += 1

# Get end time
endTime = time.time()

# Get test time
testTime = int(endTime - startTime)
print("Correct count is", correctCount,
    "out of", NUMBER_OF_QUESTIONS,
    "\n Test time is", testTime, "second"
    )