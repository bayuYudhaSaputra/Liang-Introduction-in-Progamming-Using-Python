# Define sumOfNumber function
def sumOfNumber(n):
    numberOfDigit = len(str(n)) # count the number of digit in n
    sum = 0

    for i in range(numberOfDigit, 0, -1):
        digit = n // 10 ** (i - 1)
        remainder = n % 10 ** (i - 1)
        n = remainder
        sum += digit # sum of digit
    return sum
    
# Define main function
def main():
   numberInput = eval(input("Input the integer : "))
   print("Sum of digit", numberInput, "is", sumOfNumber(numberInput))

# invoke main function
main()