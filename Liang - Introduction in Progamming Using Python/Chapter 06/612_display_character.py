# define character function
def printChars(ch1, ch2, numberPerLine):
    while ch1 < ch2: # ketika ch1 < ch2, looping dijalankan
        j = 0 # j diberi nilai 0
        while j < numberPerLine:
            # ketika j < nilai dalam numberPerline, looping dijalankn
            print(format(str(chr(ch1)),"4s"), end = " ")
            j += 1
            ch1 += 1
            if ch1 > ch2: 
                break 
                # ketika nilai ch1 > ch2 , program langsung dihentikan walaupun looping belum selesai
        print("\n")
           
printChars(49, 90, 10)