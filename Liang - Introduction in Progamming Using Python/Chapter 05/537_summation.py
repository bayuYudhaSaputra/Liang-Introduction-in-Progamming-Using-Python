print("\nHasil penjumlahan dari :")
print("1 / (1 + akar(2)) + 1 / (akar(2) + akar(3)) + ... + 1 / (akar(624) + akar(625))")
print("adalah :")
jumlah = 0
for i in range(1,625):
    suku = 1 / ((i ** 1/2) + ((i + 1) ** 1/2))
    jumlah += suku

print(jumlah)