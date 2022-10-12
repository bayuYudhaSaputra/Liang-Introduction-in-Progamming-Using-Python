# Define reversed number function
def reverseNumber(num):
    reversed_num = 0
    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10
    return reversed_num

# Define main function
def main():
    print("\n--------------------------------------")
    inputNum = int(input("Input integer : "))
    print("Reversed Number of", inputNum, "is", reverseNumber(inputNum))
    print("--------------------------------------\n")

main()