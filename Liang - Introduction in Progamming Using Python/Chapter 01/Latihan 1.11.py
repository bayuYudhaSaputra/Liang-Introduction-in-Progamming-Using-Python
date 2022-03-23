# =========================
# Memproyeksi Populasi
# =========================

'''
    Diketahui :
        1 kelahiran setiap 7 detik
        1 kematian setiap 13 detik
        1 imigran baru setiap 45 detik
        Jumlah populasi sekarang 312032486
        1 tahun = 365 hari
    Ditanya : Proyeksi jumlah populasi 5 tahun lagi.

'''
# -------------------------------------
# Langkah 1 :
# hitung jumlah detik dalam 5 tahun
banyakDetik5Thn = 5 * 365 * 24 * 3600
# -------------------------------------

# -------------------------------------
# Langkah 2 :
# Hitung banyak kelahiran
banyakKelahiran = banyakDetik5Thn // 7
# -------------------------------------

# -------------------------------------
# Langkah 3 :
# Hitung banyak kematian
banyakKematian = banyakDetik5Thn // 13
# -------------------------------------

# -------------------------------------
# Langkah 4 :
# Hitung banyak imigran baru
banyakImigran = banyakDetik5Thn // 45
# -------------------------------------

# -------------------------------------------------------------------------------
# Langkah 5 :
# Hitung Proyeksi banyak penduduk 5 tahun lagi
banyakPenduduk = 312032486 + banyakKelahiran + banyakImigran - banyakKematian
# -------------------------------------------------------------------------------

# -------------------------------------------------------------------------------
# Langkah 6 :
# Tampilkan Output
print("============================================================")
print("Menentukan Proyeksi Penduduk 5 Tahun Mendatang")
print("============================================================")
print("Jika diasumsikan :")
print("1 kelahiran setiap 7 detik;")
print("1 kematian setiap 13 detik;")
print("1 imigran baru setiap 45 detik;")
print("Jumlah populasi sekarang 312.032.486 jiwa;")
print("1 tahun = 365 hari")
print("-------------------------------------------------------------")
print("Maka 5 tahun lagi diproyeksikan bahwa,")
print("Jumlah Kelahiran diprediksi menjadi :")
print(banyakKelahiran)
print("Jumlah kematian diprediksi menjadi:")
print(banyakKematian)
print("Jumlah Imigran Baru Diprediksi Menjadi :")
print(banyakImigran)
print("============================================================")
print("Sehingga 5 tahun lagi, Jumlah Penduduk Diproyeksi Menjadi :")
print(banyakPenduduk)
print("============================================================")

        
        
        
        

# -------------------------------------------------------------------------------