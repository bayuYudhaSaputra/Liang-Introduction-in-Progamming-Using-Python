# Returns the area of the triangle.
def area(side1, side2, side3):
    halfPerimeter = (side1 + side2 + side3) / 2
    area = (halfPerimeter * (halfPerimeter - side1) * (halfPerimeter - side2) * (halfPerimeter - side3)) ** (1/2)
    return area

# Returns true if the sum of any two sides is
# greater than the third side.
def isValid(side1, side2, side3):
    errorMessage = "Invalid input"
    if side1 + side2 <= side3 :
        return errorMessage
    elif side2 + side3 <= side1 :
        return errorMessage
    elif side3 + side1 <= side1 :
        return errorMessage
    else:
        return area(side1, side2, side3)

def main():
    side1 = eval(input("Enter the length of the first side of the triangle : "))
    side2 = eval(input("Enter the length of the second side of the triangle : "))
    side3 = eval(input("Enter the length of the third side of the triangle : "))
    
    print(isValid(side1, side2, side3))

main()