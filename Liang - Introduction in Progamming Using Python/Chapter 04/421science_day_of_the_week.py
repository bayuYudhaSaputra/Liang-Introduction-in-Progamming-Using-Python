# ================================================
# Menentukan Hari
# ================================================

import sys

print("========================================================== \n",
    "Menentukan Hari \n",
    "------------------------------------------------------------"
    )

# 1. Menentukan tahun
tahun = eval(input("Input tahun : "))

# Menentukan bulan
indeksBulan = eval(input("Input bulan (antara 1 - 12) : "))

if indeksBulan == 1:
    bulan = "Januari"
elif indeksBulan == 2:
    bulan = "Februari"
elif indeksBulan == 3:
    bulan = "Maret"
elif indeksBulan == 4:
    bulan = "April"
elif indeksBulan == 5:
    bulan = "Mei"
elif indeksBulan == 6:
    bulan = "Juni"
elif indeksBulan == 7:
    bulan = "Juli"
elif indeksBulan == 8:
    bulan = "Agustus"
elif indeksBulan == 9:
    bulan = "September"
elif indeksBulan == 10:
    bulan = "Oktober"
elif indeksBulan == 11:
    bulan = "November"
elif indeksBulan == 12:
    bulan = "Desember"
else:
    print("Input hanya boleh antara 1 hingga 12.")
    print("======================================================")
    sys.exit()

indeksHari = eval(input("Input indeks hari (antara 1 hingga 31) : "))

j = tahun / 100
k = tahun % 100

h = (indeksBulan + (26 * ((indeksBulan + 1) / 10)) + k + (k/4) + (j/4) + 5 * j) % 7

if h == 0:
   hari = "Sabtu"
elif h == 1:
    hari = "Minggu"
elif h == 2:
    hari = "Senin"
elif h == 3:
    hari = "Selasa"
elif h == 4:
    hari = "Rabu"
elif h == 5:
    hari = "Kamis"
else:
    hari = "Jumat"

print("----------------------------------------------------------------")
print("Tanggal", indeksHari, "-", bulan, "-", tahun, "adalah hari", hari)
print("================================================================")