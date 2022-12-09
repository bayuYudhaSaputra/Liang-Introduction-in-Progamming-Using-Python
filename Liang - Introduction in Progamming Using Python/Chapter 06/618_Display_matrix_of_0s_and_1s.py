import random

def printMatrix(numberOfColumn, numberOfRow, endPointRandom):
    for i in range(1, numberOfColumn + 1):
        for j in range(1, numberOfRow + 1):
            entry = random.randint(0,endPointRandom)
            print(entry, end = " ")
        print(" ")

def main():
    numberOfRow = eval(input("How many row ? "))
    numberOfColumn = eval(input("How many column ? "))
    return printMatrix(numberOfRow, numberOfColumn, 1)
    
main()