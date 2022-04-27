# ========================================================================
# Hitung indeks BMI
# ------------------------------------------------------------------------

# Langkah 1. Input berat badan dalam Kg dan tinggi badan dalam sentimeter
beratBadan = eval(input("Berapa Kg berat badan anda?"))
tinggiBadanSentimeter = eval(input("Berapa cm tinggi badan anda?"))
tinggiBadanMeter = tinggiBadanSentimeter / 100

# Langkah 2. Hitung indeks BMI dengan rumus,
indeksBMI = beratBadan / tinggiBadanMeter ** 2

# Langkah 3. Tampilkan indeks BMI
print("==================================================")
print("Indeks BMI dengan berat badan",
        beratBadan,
        "Kg",
        tinggiBadanMeter,
        "cm adalah",
        indeksBMI
        )

# ========================================================================