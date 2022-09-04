# ========================================
# Table Of Square Root
# ----------------------------------------

import math

print("\n==============================")
print("||", format("Number","9s"), "|", format("Square Root","12s"), "||")
print("------------------------------")

for i in range(0,11):
    number = 2 * i
    squareRoot = math.sqrt(number)
    print("||", format(number,"7d"), "  |  " , format(squareRoot, "10.5f"), "||")

print("==============================\n")