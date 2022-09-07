banyakBaris = 9
for i in range(1, banyakBaris):
    for j in range(1, banyakBaris - i + 1):
        print(end = '    ')
    # pengatur spasi
    
    for j in range(1, i):
        print(format(j, ">3d"), end = ' ')
    
    for k in range(i, 0, -1):
        print(format(k, ">3d"), end = ' ')
    
    print("\n")