# ==================================================================================================
# Hitung hasil investasi
# --------------------------------------------------------------------------------------------------
# Langkah 1. Input nilai investasi di akhir periode, jangka waktu investasi, dan suku bunga tahunan
# Langkah 2. Hitung tingkat suku bunga bulanan
# Langkah 3. Hitung jangka waktu dalam bulan
# Langkah 4. Hitung dana awal investasi yang dibutuhkan
# Langkah 5. Tampilkan dana awal investasi yang dibutuhkan
# --------------------------------------------------------------------------------------------------

# Langkah 1.
nilaiInvestasiAkhir = eval(input("Input hasil dana investasi yang diinginkan (dalam Rp) : "))
jangkaWaktuTahunan = eval(input("Input jangka waktu investasi (dalam tahun) : "))
bungaTahunan = eval(input("Berapa suku bunga per tahun ?"))

# Langkah 2.
bungaBulanan = bungaTahunan / 1200

# Langkah 3.
jangkaWaktuBulanan = 12 * jangkaWaktuTahunan

# Langkah 4.
danaAwal = (nilaiInvestasiAkhir) / ((1 + bungaBulanan) ** jangkaWaktuBulanan)
danaAwalRound = round(danaAwal, 2)

# Langkah 5.
print("Nilai investasi awal yang dibutuhkan, jika,")
print("Nilai Akhir Investasi yang dibutuhkan sebesar : Rp.", nilaiInvestasiAkhir)
print("Suku Bunga :", bungaTahunan, "%")
print("Jangka waktu :", jangkaWaktuTahunan, "tahun.")
print("adalah : Rp.", danaAwalRound)

# --------------------------------------------------------------------------------------------------