# Define distance of two point in carteius
def distance(x1, x2, y1, y2):
    r = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2)
    # r is distance of two point
    return r

def main():
    x1, y1 = eval(input("Input first point (ex. 1,2) : "))
    x2, y2 = eval(input("Input second point (ex. 3,4) : "))
    print("Distance of point",
            "(", x1, ",", y1, ")", "and",
            "(", x2, ",", y2, ")", "is"            
            )
    print(distance(x1, x2, y1, y2))

main()