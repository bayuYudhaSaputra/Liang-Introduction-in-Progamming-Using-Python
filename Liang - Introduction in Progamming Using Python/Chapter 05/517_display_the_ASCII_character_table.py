banyakBaris = 9
for i in range(0,banyakBaris + 1):
    
    for j in range(i, 11):
        kodeAscii = chr(32 + j)
        print(kodeAscii, end = '  ')
   
    print("\n")