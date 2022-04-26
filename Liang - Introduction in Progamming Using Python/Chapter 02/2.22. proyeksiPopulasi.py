# ==========================================================================================
# Hitung proyeksi penduduk setelah n tahun
# ------------------------------------------------------------------------------------------

# Langkah 1. Input data jumlah populasi sekarang dengan variabel jumlahPopulasiSekarang
#            dan jangka waktu dalam satuan tahun dengan variabel jangkaWaktuTahun
jumlahPopulasiSekarang = eval(input("Berapa jumlah populasi sekarang?"))
jangkaWaktuTahun = eval(input("Berapa tahun jangka waktu proyeksi populasi?"))

# Langkah 2. Hitung banyak detik dalam n tahun dengan rumus :
jangkaWaktuDetik = jangkaWaktuTahun * 365 * 24 * 3600

# Langkah 3. Hitung proyeksi jumlah kelahiran dalam jangka waktu n tahun
banyakKelahiran = jangkaWaktuDetik // 7

# Langkah 4. Hitung proyeksi jumlah kematian dalam jangka waktu n tahun 
banyakKematian = jangkaWaktuDetik // 7

# Langkah 5. Hitung proteksi jumlah imigran baru dalam jangka waktu n tahun
banyakImigran = jangkaWaktuDetik // 7

# Langkah 6. Hitung proyeksi jumlah penduduk dalam jangka waktu n tahun 
proyeksiPopulasi = jumlahPopulasiSekarang + banyakKelahiran + banyakImigran - banyakKematian

# Langkah 7. Tampilkan proyeksi jumlah penduduk dalam n tahun
print("================================================================")
print("Jumlah penduduk sekarang adalah", jumlahPopulasiSekarang, "jiwa.")
print(jangkaWaktuTahun,
        "tahun lagi, jumlah populasi diproyeksikan menjadi",
        proyeksiPopulasi, "jiwa."
        )
print("================================================================")

# ==============================================================================================