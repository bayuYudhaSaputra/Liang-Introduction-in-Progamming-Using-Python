# ===========================================================================
# Hitung Bunga Bulanan
# ---------------------------------------------------------------------------

# Langkah 1. Input saldo (dalam Rp) dan persentase bunga tahunan
saldo = eval(input("Berapa saldonya (dalam Rp)? "))
persenBungaTahunan = eval(input("Berapa persentase bunga tahunan ?"))

# Langkah 2. Hitung nominal bunga bulanan dengan rumus,
nominalBungaBulanan = saldo * ( persenBungaTahunan / 1200 )

# Langkah 3. Bulatkan nominal saldo ke dua angka di belakang titik
roundSaldo = round(saldo,2)

# Langkah 4. Bulatkab nominal bunga bulanan ke dua angka di belakang titik
roundNominalBungaBulanan = round(nominalBungaBulanan, 2)

# Langkah 3. Tampilkan nominal bunga bulanan.
print("============================================")
print("Nominal bunga bulanan dengan :")
print("   saldo sebesar Rp.", roundSaldo, ";")
print("   persentase bunga", persenBungaTahunan, "% per tahun;")
print("---------------------------------------------")
print("adalah :")
print("Rp.", roundNominalBungaBulanan)
print("============================================")

# ===========================================================================