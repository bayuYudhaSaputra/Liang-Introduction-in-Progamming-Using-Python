print("\n-------------------------------------")
count = 1
for i in range(33,128):
    # menampilkan kode ascii dari 33 ke 127
    kodeAscii = chr(i)
    print(format(kodeAscii, "<3s"), end = '')
    # menampilkan 10 karakter tiap baris
    
    if count % 10 == 0:
        print(" \n ")
    else:
        print(end = '')
    count += 1
print("\n------------------------------------\n")