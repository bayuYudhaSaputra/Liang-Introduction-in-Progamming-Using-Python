from Listing65_GCD_function import gcd # import the gcd function

# Prompt the user to enter two integers
n1 = eval(input("Enter the first integer :"))
n2 = eval(input("Enter the second integer :"))

print("The greatest common divisor for", n1,
    "and", n2, "is", gcd(n1, n2))