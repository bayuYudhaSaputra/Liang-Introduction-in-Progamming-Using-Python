import random

lotteryDigit1 = random.randint(0,9)

lotteryDigit2 = random.randint(0,9)

while lotteryDigit2 == lotteryDigit1:
    lotteryDigit2 = random.randint(0,9)
    print("----------------------------------")
    print(str(lotteryDigit1) + str(lotteryDigit2))

print("====================================")
print(str(lotteryDigit1) + str(lotteryDigit2))
print("====================================")