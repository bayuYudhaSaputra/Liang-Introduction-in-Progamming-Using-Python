i = 50
jumlah = 0

# iterasi dimulai dari (1 / 50) + (1 / 49) + ... + (1 / 2) + 1
# agar terhindar dari kesalahan pembulatan
while i > 0:
    suku = 1 / i
    jumlah += suku
    i -= 1

print("\n------------------------------------------------------------------")
print("Jumlah 1 + (1 / 2) + (1 / 3) + (1 / 5) + ... + (1 / 50) adalah ", jumlah)
print("------------------------------------------------------------------\n")