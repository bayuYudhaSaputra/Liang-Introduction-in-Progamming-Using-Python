# ===================================================================================================
# Hitung nilai Investasi di akhir periode
# ---------------------------------------------------------------------------------------------------

# Langkah 1. Input dana investasi awal, imbal hasil tahunan dan jangka waktu investasi (dalam tahun)
danaInvestasiAwal = eval(input("Input dana investasi awal (dalam Rp) : "))
imbalHasilTahunan = eval(input("Input imbal hasil tahunan (dalam persen) : "))
jangkaWaktuTahunan = eval(input("Input jangka waktu investasi (dalam tahun) : "))

# Langkah 2. Hitung imbal hasil bulanan dengan rumus :
imbalHasilBulanan = imbalHasilTahunan / 1200

# Langkah 3. Hitung jangka waktu dalam satuan bulan dengan rumus :
jangkaWaktuBulanan = jangkaWaktuTahunan * 12

# Langkah 4. Hitung total investasi di akhir periode dengan rumus :
nilaiAkhirInvestasi = danaInvestasiAwal * ( 1 + imbalHasilBulanan ) ** jangkaWaktuBulanan

# Langkah 5. Bulatkan dana investasi awal menjadi 2 angka dibelakang titik
roundDanaInvestasiAwal = round(danaInvestasiAwal, 2)

# Langkah 6. Bulatkan total investasi di akhir periode menjadi 2 angka di belakang koma :
roundNilaiAkhirInvestasi = round(nilaiAkhirInvestasi, 2)

# Langkah 7. Tampilkan total investasi di akhir periode.
print("==========================================")
print("Nilai investasi di akhir periode, dengan :")
print("   nilai awal investasi : Rp.", roundDanaInvestasiAwal)
print("   imbal hasil tahunan", imbalHasilTahunan, "% ;")
print("   jangka waktu", jangkaWaktuTahunan, "tahun ;")
print("-------------------------------------------")
print ("adalah :")
print("Rp", roundNilaiAkhirInvestasi)
print("==========================================")

# ===================================================================================================