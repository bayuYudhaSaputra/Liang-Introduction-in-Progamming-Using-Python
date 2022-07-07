# ===========================================
# Cek Bilangan
# ===========================================

bilangan = eval(input("Input bilangan asli : "))

# Cek apakah nilai yang ada dalam variabel "bilangan" habis dibagi 5 dan 6
if bilangan % 5 == 0 and bilangan % 6 == 0:
    print("Apakah", bilangan, "habis dibagi 5 dan 6 ? Benar...!!!")
else:
    print("Apakah", bilangan, "habis dibagi 5 dan 6 ? Salah...!!!")

# Cek apakah nilai yang ada dalam variabel "bilangan" habis dibagi 5 atau 6
if bilangan % 5 == 0 or bilangan % 6 == 0:
    print("Apakah", bilangan, "habis dibagi 5 atau 6 ? Benar...!!!")
else:
    print("Apakah", bilangan, "habis dibagi 5 atau 6 ? Salah...!!!")

# Cek apakah nilai yang ada dalam variabel "bilangan" habis dibagi 5 saja atau 6 saja
# (menggunakan operasi bitwise XOR)
if bilangan % 5 ^ bilangan % 6: # operasi bitwise XOR
    print("Apakah", bilangan, "habis dibagi 5 saja atau 6 saja ? Benar...!!!")
else:
    print("Apakah", bilangan, "habis dibagi 5 saja atau 6 saja ? Salah...!!!")
