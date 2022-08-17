# Menentukan aproksimasi nilai phi

i = 1
jumlah = 0

while i < 10000:
    suku = ((-1) ** (i + 1)) / (2 * i - 1)
    jumlah += suku
    phi = 4 * jumlah
    i += 1

print("\n-----------------------------------")
print("Nilai pi = ", phi)
print("-----------------------------------\n")