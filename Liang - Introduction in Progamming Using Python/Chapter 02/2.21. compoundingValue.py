# ================================================================================
# Hitung compounding Value hingga bulan ke-6
# --------------------------------------------------------------------------------

# Langkah 1. Input nominal simpanan bulanan dan bunga tahunan (dalam persentase)
simpananKe0 = eval(input("Berapa rupiah tabungan yang disisihkan per bulan? "))
bungaTahunan = eval(input("Berapa persen imbal hasil yang diterima per tahun? "))
roundSimpananKe0 = round( simpananKe0, 2 )

# Langkah 2. Hitung bunga bulanan dengan rumus,
bungaBulanan = bungaTahunan / 1200

# Langkah 3. Hitung nominal simpanan pada bulan ke-1 dengan rumus
simpananKe1 = simpananKe0 * ( 1 + bungaBulanan )
roundSimpananKe1 = round(simpananKe1, 2)

# Langkah 4. Hitung nominal simpanan pada bulan ke-2 dengan rumus,
simpananKe2 = ( simpananKe0 + simpananKe1 ) *  ( 1 + bungaBulanan )
roundSimpananke2 = round(simpananKe2, 2)

# Langkah 5. Hitung nominal simpanan pada bulan ke-3 dengan rumus,
simpananKe3 = ( simpananKe0 + simpananKe2 ) * ( 1 + bungaBulanan )
roundSimpananke3 = round( simpananKe3, 2)

# Langkah 6. Hitung nominal simpanan pada bulan ke-4 dengan rumus,
simpananKe4 = ( simpananKe0 + simpananKe3 ) * ( 1 + bungaBulanan )
roundSimpananKe4 = round( simpananKe4, 2)

# Langkah 7. Hitung nominal simpanan pada bulan ke-5 dengan rumus,
simpananKe5 = ( simpananKe0 + simpananKe4 ) * ( 1 + bungaBulanan )
roundSimpananKe5 = round(simpananKe5, 2)

# Langkag 8. Hitung nominal simpanan pada bulan ke-6 dengan rumus,
simpananKe6 = ( simpananKe0 + simpananKe5 ) * ( 1 + bungaBulanan )
roundSimpananKe6 = round(simpananKe6, 2)

# Langkah 9. Tampilkan jumlah nominal simpanan ke-1, 2, ..., 6.
print("=========================================")
print("Tabel Hasil Investasi Bulanan")
print("Nominal tabungan bulanan : Rp.", roundSimpananKe0)
print("Imbal Hasil :", bungaTahunan, "% per tahun.")
print("-----------------------------------------")
print("||", "Bulan ke-", "|","Total Simpanan","   ||")
print("------------------------------------------")
print("||    ", 1, "    |", "Rp" ,roundSimpananKe1 ,"      ||")
print("||    ", 2, "    |", "Rp" ,roundSimpananke2 ,"     ||")
print("||    ", 3, "    |", "Rp" ,roundSimpananke3 ,"     ||")
print("||    ", 4, "    |", "Rp" ,roundSimpananKe4 ,"     ||")
print("||    ", 5, "    |", "Rp" ,roundSimpananKe5 ,"    ||")
print("||    ", 6, "    |", "Rp" ,roundSimpananKe6 ,"    ||")
print("-----------------------------------------")
print("=========================================")

# ================================================================================