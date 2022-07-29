# ========================================
# Table Of Square Root
# ----------------------------------------

import math


indeks = 0 
print("================================== \n",
    "Table Of Square Root \n",
    "------------------------------------ \n"
    )
print("Number", "Square Root",
    "")
while indeks <= 10:
    number = 2 * indeks
    squareRoot = math.sqrt(number)
    print(number, "  |  " , round(squareRoot, 4))
    print("--------------------------")
    indeks += 1
