n = 49
jumlah = 0

while n > 0:
    suku = (2 * n - 1) / (2 * n + 1)
    jumlah += suku
    
    n -= 1
print("\n------------------------------------------------------------------")
print("Jumlah (1 / 3) + (3 / 5) + (5 / 7) + ... + (97 / 99) adalah ", jumlah)
print("------------------------------------------------------------------\n")