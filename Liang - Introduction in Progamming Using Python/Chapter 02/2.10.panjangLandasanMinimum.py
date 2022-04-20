# ======================================================================================================
# Hitung Panjang Landasan Minimum
# ------------------------------------------------------------------------------------------------------
# Langkah 1. Input data kecepatan (dalam m/s) dan percepatan (dalam m/s2) pesawat
# Langkah 2. Hitung panjang landasan minimal pesawat yang dibutuhkan untuk mendarat dengan rumus,
#               jarakMinimalLandasan = (kecepatan ** 2) / 2 * percepatan
# Langkah 3. Tampilkan hasil jarak minimal landasan yang dibutuhkan.
# ------------------------------------------------------------------------------------------------------

# Langkah 1
kecepatan, percepatan = eval(
                            input("Input kecepatan (dalam m/s) dan percepatan (dalam m/s2) pesawat : ")
                            )
# Langkah 2
jarakMinimalLandasan = (kecepatan ** 2) / (2 * percepatan)

# Langkah 3
print(
        "Panjang landasan minimal yang dibutuhkan oleh pesawat yang mendarat dengan kecepatan",
        kecepatan,
        "m/s",
        "dan percepatan ",
        percepatan,
        "adalah : ",
        jarakMinimalLandasan,
        "meter."
        )

# =======================================================================================================



