# ======================================
# Membalik urutan digit bilangan
# ======================================

print(
    "================================================= \n",
    "\t Membalik bilangan 4 digit \n",
    "-------------------------------------------------"
)

# 1. Input bilangan ribuan
bilangan = eval(input("Input bilangan ribuan (Mis. 5413) : "))
print("------------------------------------------------- \n")
# 2. Ambil digit ribuan
digitRibuan = bilangan // 1000
sisaRibuan = bilangan % 1000

# 3. Ambil digit ratusan
digitRatusan = sisaRibuan // 100
sisaRatusan = sisaRibuan % 100

# 4. Ambil digit puluhan dan satuan
digitPuluhan = sisaRatusan // 10
digitSatuan = sisaRatusan % 10

# 5. Menyatukan digit ribuan, ratusan, puluhan dan satuan
bilanganKebalikan = int(
    str(digitSatuan) + str(digitPuluhan) + str(digitRatusan) + str(digitRibuan)
)

# 6. Menampilkan hasil pembalikan bilangan 4 digit.
print(
    "Bilangan",
    bilangan,
    "dibalik menjadi",
    bilanganKebalikan,
)

print("===============================================")