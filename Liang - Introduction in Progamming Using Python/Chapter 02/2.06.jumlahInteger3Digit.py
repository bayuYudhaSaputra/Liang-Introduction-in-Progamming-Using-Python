# ===========================================================================================================================
# Menjumlahkan Digit Bilangan
# ---------------------------------------------------------------------------------------------------------------------------
# Langkah 1. Input bilangan 3 digit
# Langkah 2. Ambil digit satuan dari bilangan tersebut dengan rumus, digitSatuan = bilangan3Digit % 10
# Langkah 3. Ekstrak bilangan puluhan dari bilangan tersebut dengan rumus, ekstrakBilanganPuluhan = bilangan3Digit // 10
# Langkah 4. Ambil digit puluhan dari hasil ekstrakBilanganPuluhan dengan rumus, digitPuluhan = ekstrakBilanganPuluhan % 10
# Langkah 5. Ambil digit ratusan dengan rumus, digitRatusan = ekstrakBilanganPuluhan // 10
# Langkah 6. Hitung jumlah digit-digit tersebut dengan rumus, jumlahDigit = digitRatusan + digitPuluhan + digitSatuan
# Langkah 7. Tampilkan hasil jumlah ketiga digit tersebut
# ---------------------------------------------------------------------------------------------------------------------------

# Langkah 1.
bilangan3Digit = eval(input("Input bilangan 3 digit (misal. 100, 101, … , 999) :"))

# Langkah 2.
digitSatuan = bilangan3Digit % 10

# Langkah 3.
ekstrakBilanganPuluhan = bilangan3Digit // 10

# Langkah 4.
digitPuluhan = ekstrakBilanganPuluhan % 10

# Langkah 5.
digitRatusan = ekstrakBilanganPuluhan // 10

# Langkah 6.
jumlahDigit = digitRatusan + digitPuluhan + digitSatuan

# langkah 7.
print("Jumlah digit bilangan", bilangan3Digit, "adalah :", jumlahDigit)

# ===========================================================================================================================