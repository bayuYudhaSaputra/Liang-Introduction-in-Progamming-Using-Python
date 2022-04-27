# ==================================================================================================
# Hitung percepatan rata-rata
# --------------------------------------------------------------------------------------------------

# Langkah 1. Input kecepatan awal dan kecepatan akhir (dalam m/s)
#           serta selang waktu (dalam sekon)
kecepatanAwal = eval(input("Berapa kecepatan awal (dalam satuan m/s) ?  "))
kecepatanAkhir = eval(input("Berapa kecepatan akhir (dalam satuan m/s) ? "))
selangWaktu = eval(input("Berapa jam waktu yang dibutuhkan dari kecepatan awal ke akhir ?  "))

# Langkah 2. Hitung percepatan rata-rata dengan rumus,
percepatan = ( kecepatanAkhir - kecepatanAwal ) / selangWaktu

# Langkah 3. Tampilkan percepatan rata-rata
print("==========================================")
print("Percepatan rata-rata suatu obyek dengan,")
print("------------------------------------------")
print("kecepatan awal", kecepatanAwal, "m/s,")
print("kecepatan akhir", kecepatanAkhir, "m/s,")
print("selang waktu", selangWaktu, "sekon")
print("-----------------------------------------")
print("adalah : ", percepatan, "m/s2")
print("==========================================")

# ==================================================================================================