# ===========================================================================
# Luas Segi-n
# ===========================================================================

print("=============================================")
print("Luas Segi-n")
print("---------------------------------------------")

import math

# 1. Input banyak sisi segi-n
banyakSisi = eval(input("Input banyak sisi segi-n : "))

# 2. Input panjang sisi segi-n
panjangSisi = eval(input("Input panjang sisi segi-n : "))

# 3. Hitung luas segi-n
luas = round(
                (banyakSisi * panjangSisi ** 2) / (4 * math.tan(math.pi / 5)),
                2
            )

# 4. Tampilkan hasil perhitungan luas segi-n
print(
        "Luas segi-", banyakSisi,
        "dengan panjang sisi",
        panjangSisi, "satuan panjang adalah ",
        luas, "satuan luas"
        )

print("==============================================")