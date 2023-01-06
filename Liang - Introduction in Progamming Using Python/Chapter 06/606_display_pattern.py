# define displayPattern function
def displayPattern(n):
    for numColomn in range(1, n + 1):
    # membuat kolom
        for numRow in range(numColomn, 0, -1):
        # menampilkan bilangan dalam baris
            print(numRow, end = ' ')
            
        print(" ")
    return "" # agar tidak mengembalikan nilai none

def main():
    n = eval(input("Input number :"))
    print(displayPattern(n))

main()