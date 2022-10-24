# define character function

numberPerLine = 10
i = 0
index_ASCII_code = 48

while i < 8:
    j = 0
    while j < numberPerLine:
        print( format(str(chr(index_ASCII_code)),"4s"), end = " ")
        j += 1
        index_ASCII_code += 1
    print("\n")
    i += 1


    