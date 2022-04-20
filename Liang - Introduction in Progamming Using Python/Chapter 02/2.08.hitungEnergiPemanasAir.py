# ============================================================================
# Energi yang dibutuhkan untuk memanaskan air
# ----------------------------------------------------------------------------
# Langkah 1. Input data berat air dalam kilogram
# Langkah 2. Input data suhu awal
# Langkah 3. Input data suhu akhir
# Langkah 4. Hitung energi yang dibutuhkan untuk memanaskan air dengan rumus,
#               Energi = beratAir * ( suhuAkhir - suhuAwal ) * 4184
# Langkah 5. Tampilkan data energi yang dibutuhkan untuk memanaskan air
# -----------------------------------------------------------------------------

# Langkah 1.
beratAir = eval(input("Input berat air yang akan direbus (mis. 3 Kg) : "))

# Langkah 2.
suhuAwal = eval(input("Input suhu awal dalam celsius (mis. 100 C) : "))

# Langkah 3.
suhuAkhir = eval(input("Input suhu akhir dalam celsius (mis. 312 C : "))

# Langkah 4.
energi = beratAir * ( suhuAkhir - suhuAwal ) * 4184

# Langkah 5.
print(
    "Energi yang dibutuhkan untuk memanaskan air", 
    beratAir, 
    "Kg dengan suhu awal", 
    suhuAwal,
    "derajat Celsius",
    "dan suhu akhir",
    suhuAkhir,
    "derajat celsius adalah : ",
    energi,
    "joule."
    )

# -----------------------------------------------------------------------------