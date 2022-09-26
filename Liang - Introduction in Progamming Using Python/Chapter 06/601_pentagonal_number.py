# define function for pentagonal number
def getPentagonalNumbers(n):
    pentaNum = n * (3 * n - 1) / 2
    return pentaNum    

# define main function
def main():
    count = 0
    for n in range(1,100):
        print(format(getPentagonalNumbers(n),"6.0f"), end = '')
        # print function getPentagonalNumbers in for looping
        count += 1
        if count % 10 == 0:
            # 10 numbers per line
            print("\n")
    
main() # invoke main function