# Aproksimasi Phi

jumlah = 0

for i in range(1,10001):
    suku = ((-1) ** (i + 1)) / (2 * i - 1)
    jumlah += suku
    phi = 4 * jumlah

print("\n-----------------------------------")
print("Nilai pi = ", phi)
print("-----------------------------------\n")