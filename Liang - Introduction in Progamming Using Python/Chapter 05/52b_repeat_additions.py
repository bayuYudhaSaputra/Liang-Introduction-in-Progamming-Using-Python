import random
import time

# Count the number of correct answers
correctCount = 0

print("=========================================================== \n",
    "Adding Quiz \n",
    "-------------------------------------------------------------"
    )

# Get start time
startTime = time.time()

for countAnswer in range(0,10):
    # Generate two random single digit integers
    number1 = random.randint(0,9)
    number2 = random.randint(0,9)

    # Prompt the student to answer "What is number1 - number2 ?"
    answer = eval(input(str(countAnswer + 1) + ". What is " + str(number1) + \
        " + " + str(number2) + "? "
        ))
    
    # Grade the answer and display the result
    if number1 + number2 == answer:
        print("Response : \n","\t You are correct! \n")
        correctCount += 1
    else:
        print("Response : \n"
            "\t Your answer is wrong \n",
            "\t", number1, "+", number2, " = ",number1 + number2, "\n"
            )

# Get end time
endTime = time.time()

print("-------------------------------------------------------------")
# Get test time
testTime = int(endTime - startTime)
print("Correct count is", correctCount,
    "out of", 10,
    "\nTest time is", testTime, "second"
    )
print("===========================================================")