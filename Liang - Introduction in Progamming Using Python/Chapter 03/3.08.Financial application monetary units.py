# ==========================================
# Menyatakan mata uang
# ==========================================

print("==========================================")
print("Menyatakan mata uang")
print("------------------------------------------")
# 1. Input jumlah mata uang
jumlahUang = eval(input("Input jumlah mata uang : "))

# 2. Hitung jumlah dolar dan sen
jumlahDolar = int(jumlahUang // 100)
jumlahSen = int(jumlahUang % 100)

# 3. Tampilkan hasil dolar dan sen
print("Uang sebesar",
        jumlahUang,
        "adalah",
        jumlahDolar,
        "dolar",
        jumlahSen,
        "sen."
)
print("=========================================")