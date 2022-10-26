# define character function
def printChars(ch1, ch2, numberPerLine):
    
    if ch1 < ch2 and numberPerLine > 0:
        # Perulangan dilakukan ketika ch1 < ch2 dan numberLine > 0
        while ch1 < ch2:
            j = 0
            while j < numberPerLine:
                print(format(str(chr(ch1)),"4s"), end = " ")
                j += 1
                ch1 += 1
            print("\n")
    else: # jika ch1, ch2 dan numberPerLine tidak memenuhi syarat maka muncul teks berikut
        print("ch1 harus kurang dari ch2 dan numberPerLine harus lebih dari 0")
        
printChars(48, 100, 10)