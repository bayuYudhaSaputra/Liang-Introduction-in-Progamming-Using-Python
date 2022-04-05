# Prompt the user for input
seconds = eval(input("Enter an integer for second :"))

# Get minutes and remaining second
minutes = seconds // 60 # Find minutes in seconds
remainingSecond = seconds % 60 # Second remaining
print(seconds, "seconds is", minutes,
        "minutes and", remainingSecond, "seconds")