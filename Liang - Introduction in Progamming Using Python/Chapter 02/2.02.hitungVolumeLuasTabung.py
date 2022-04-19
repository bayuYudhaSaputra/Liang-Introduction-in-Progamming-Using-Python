# =========================================================================================
# Hitung Volume dan Luas Tabung
# -----------------------------------------------------------------------------------------
# Langkah 1. Input jari-jari dan tinggi tabung
# Langkah 2. Mendefinisikan phi = 3.14
# Langkah 3. Hitung volume tabung
# Langkah 4. Hitung luas tabung
# Langkah 5. Tampilkan hasil volume dan luas tabung
# ------------------------------------------------------------------------------------------

# Langkah 1. Input jari-jari dan tinggi tabung
jari2, tinggi = eval(input("Input jari-jari dan tinggi tabung :"))

# Langkah 2. Mendefinisikan phi = 3.14
phi = 3.14

# Langkah 3. Hitung volume tabung
volume = phi * jari2 ** 2 * tinggi

# Langkah 4. Hitung luas tabung
luas = 2 * phi * jari2 * ( jari2 + tinggi )

# Langkah 5. Tampilkan hasil volume dan luas tabung
print("Volume tabung dengan jari-jari", jari2, "dan tinggi", tinggi, "adalah :", volume)
print("Luas tabung dengan jari-jari", jari2, "dan tinggi", tinggi, "adalah :", luas)
# =========================================================================================