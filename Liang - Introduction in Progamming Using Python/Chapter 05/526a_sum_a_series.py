n = 1
jumlah = 0

while n < 50:
    suku = (2 * n - 1) / (2 * n + 1)
    jumlah += suku
    print("------------------------------------")
    print("Jumlah", n, "suku pertama adalah", jumlah)
    print("------------------------------------")
    n += 1
    