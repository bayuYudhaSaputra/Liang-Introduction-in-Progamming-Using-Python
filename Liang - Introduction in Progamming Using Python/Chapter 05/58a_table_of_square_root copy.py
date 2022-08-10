# ========================================
# Table Of Square Root
# ----------------------------------------

import math

indeks = 0 

print("\n==============================")
print("||", format("Number","9s"), "|", format("Square Root","12s"), "||")
print("------------------------------")

while indeks <= 10:
    number = 2 * indeks
    squareRoot = math.sqrt(number)
    print("||", format(number,"7.3f"), "  |  " , format(squareRoot, "10.5f"), "||")
    indeks += 1
print("==============================\n")