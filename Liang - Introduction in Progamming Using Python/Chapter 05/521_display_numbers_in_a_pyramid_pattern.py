banyakBaris = 9
for i in range(0, banyakBaris):
    for j in range(1, banyakBaris - i + 1):
        print(end = '    ')
    # pengatur spasi
    
    for j in range(0, i):
        hasilPangkat1 = 2 ** j
        print(format(hasilPangkat1, ">3d"), end = ' ')
    
    for k in range(i, -1, -1):
        hasilPangkat2 = 2 ** k
        print(format(hasilPangkat2, ">3d"), end = ' ')
    
    print("\n")