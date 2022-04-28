# ==================================================================================
# Ubah selang waktu detik ke tahun sisa beberapa hari
# ----------------------------------------------------------------------------------

# Langkah 1. Input jangka waktu dalam satuan detik dengan variabel
selangWaktuDetik = eval(input("Input selang waktu dalam detik :  "))

# Langkah 2. Hitung 1 hari dalam detik
banyakDetikSatuHari = 24 * 3600

# Langkah 3. Ekstrak hari
ekstrakHari = selangWaktuDetik // banyakDetikSatuHari

# Langkah 3. Ubah detik menjadi hari
hari = ekstrakHari % 365

# Langkah 4. Ubah detik menjadi tahun
tahun = ekstrakHari // 365

# Langkah 5. Tampilkan hasil perhitungan konversi detik ke tahun sisa beberapa hari
print("===========================================")
print("Selang waktu", selangWaktuDetik, "detik")
print("jika dikonversi menjadi tahun dan hari menjadi :")
print(tahun, "tahun", hari, "hari")
print("===========================================")

# ==================================================================================