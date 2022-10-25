# define character function

def printChars(ch1, ch2, numberPerLine):
    
    if ch1 < ch2: # jika nilai ch1 < ch2
        while ch1 < ch2:
            j = 0
            while j < numberPerLine:
                print(format(str(chr(ch1)),"4s"), end = " ")
                j += 1
                ch1 += 1
            print("\n")
        
printChars(50, 90, 10)