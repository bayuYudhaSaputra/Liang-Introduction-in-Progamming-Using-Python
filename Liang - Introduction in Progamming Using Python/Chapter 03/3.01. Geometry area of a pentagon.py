# =========================================
# Menghitung Luas Segilima
# =========================================

import math 

print("=======================================================")
# Langkah 1 : Ambil data jarak titik pusat segilima dengan titik sudut segilima dari input pengguna
jarakPusatDanSudut = eval(input("Input jarak titik pusat dengan titik sudut : "))

# Langkah 2 : Hitung panjang sisi segilima
panjangSisi = 2 * jarakPusatDanSudut * math.sin(math.pi / 5)

# Langkah 3 : Hitung luas segilima
luas = ((3 * math.sqrt(3)) / 2) * pow( panjangSisi, 2)
roundLuas = round(luas, 2)

# Langkah 4 : Tampilkan luas segilima
print("-------------------------------------------------------")
print("Luas segilima dengan jarak titik pusat dengan titik sudut",
        jarakPusatDanSudut,
        "satuan panjang adalah :",
        roundLuas,
        "satuan luas"
        )
print("======================================================")

# ======================================================================