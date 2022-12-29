def ascendingOrder(num1, num2, num3):
    if num1 > num2: # jika num1 lebih dari num2         
        num1, num2 = num2, num1 # nilai num1 dan num2 ditukar
    if num1 > num3: # jika num1 lebih dari num3
        num1, num3 = num3, num1 # nilai num1 dan num3 ditukar
    if num2 > num3: # jika nilai num2 lebih dari num3
        num3, num2 = num2, num3 # nilai num2 dan num2 ditukar
    return num1, num2, num3

def main():
    num1 = eval(input("Input the first number :"))
    num2 = eval(input("Input the second number :"))
    num3 = eval(input("Input the third number :"))
    print(ascendingOrder(num1, num2, num3))

main()