# define character function
def printChars(ch1, ch2, numberPerLine):
    
    while ch1 < ch2:
        j = 0
        while j < numberPerLine:
            print(format(str(chr(ch1)),"4s"), end = " ")
            j += 1
            ch1 += 1
            if ch1 > ch2:
                break
        print("\n")
    
        
printChars(49, 90, 10)
