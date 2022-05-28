# ===============================================
# Hitung Luas Segilima
# ===============================================

print("=======================================================")
print("Luas Segilima")
print("-------------------------------------------------------")
import math

# 1. Input panjang sisi segilima
sisi = eval(input("Input panjang sisi segilima :"))

# 2. Hitung luas segilima
luas = round( # membulatkan dua angka di belakang titik.
            (5 * sisi ** 2) / (4 * math.tan(math.pi / 5)), # rumus luas segilima
                2
            )

# 3. Tampilkan hasil perhitungan luas segilima.
print("Luas segilima dengan panjang sisi",
        sisi,
        "satuan panjang adalah",
        luas,
        "satuan luas."
        )

print("======================================================")