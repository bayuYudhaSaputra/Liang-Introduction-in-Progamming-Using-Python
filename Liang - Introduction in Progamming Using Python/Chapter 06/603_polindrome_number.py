# Define reverse number function
def reverse(number):
    reverseNumber = 0
    while number != 0:
        digit = number % 10
        reverseNumber = reverseNumber * 10 + digit
        number = number // 10
    return reverseNumber

# Define function to check polindrome
def isPolindrome(number):
    if number == reverse(number):
        return (str(number) + " " + "is polindrome number")
    else:
        return (str(number) + " " + "isn't polindrome number")

# Define main function
def main():
    inputNumber = eval(input("Input integer number : "))
    print(isPolindrome(inputNumber))

# Invoke main function
main()