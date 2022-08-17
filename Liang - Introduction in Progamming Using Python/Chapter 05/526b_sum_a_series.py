jumlah = 0

for n in range(1,50):
    suku = (2 * n - 1) / (2 * n + 1)
    jumlah += suku
    print("------------------------------")
    print("Jumlah", n, "suku pertama adalah ", jumlah)
    print("------------------------------")